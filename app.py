from flask import Flask, render_template, request, jsonify
from ollama import chat

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get("message", "")
    try:
        instruction = "you are a professional theropist, you listen to the user inputs and analyse the feeling and give a small quote to motivate them, give the three advise to recover, suggest some remedial measures from the therapist point of few, do not give it as a pharagraph, if the user say thank you respond welcome, try to add more emoji"
        response = chat(model='llama3.2', messages=[{'role': 'system', 'content': instruction},{'role': 'user', 'content': user_message}])
        chatbot_reply = response['message']['content'] if 'message' in response else "I'm sorry, I couldn't process your request. Please try again."
    except Exception as e:
        chatbot_reply = f"An error occurred: {str(e)}"

    return jsonify({"reply": chatbot_reply})

if __name__ == '__main__':
    app.run(debug=True)
 # type: ignore