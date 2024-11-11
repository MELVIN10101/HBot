import tkinter as tk
from tkinter import scrolledtext
from ollama import chat  # Ensure ollama is properly installed and configured

# Initialize the main application window
root = tk.Tk()
root.title("Mental Well-being Chatbot")
root.geometry("500x500")

# Set up a scrolling text widget for displaying the conversation
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, state='disabled')
chat_display.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

# Function to send a message to the Llama3.2 model and get a response
def send_message():
    user_message = user_input.get()
    user_input.set('')  # Clear the input field after sending

    if user_message.strip():
        # Display the user's message in the chat display
        chat_display.configure(state='normal')
        chat_display.insert(tk.END, "You: " + user_message + "\n")
        chat_display.configure(state='disabled')
        chat_display.see(tk.END)
        
        # Send the user's message to Llama3.2 for a response
        try:
            response = chat(model='llama3.2', messages=[{'role': 'user', 'content': user_message}])
            
            # Debugging: Print the response to see its structure
            print("Response from model:", response)

            # Retrieve the chatbot's response content from the dictionary
            if response and 'message' in response and 'content' in response['message']:
                chatbot_reply = response['message']['content']
            else:
                chatbot_reply = "I'm sorry, I couldn't process your request. Please try again."
        
        except Exception as e:
            # Handle any exceptions and display an error message
            chatbot_reply = f"An error occurred: {str(e)}"

        # Display the chatbot's response
        chat_display.configure(state='normal')
        chat_display.insert(tk.END, "Bot: " + chatbot_reply + "\n")
        chat_display.configure(state='disabled')
        chat_display.see(tk.END)

# Entry widget for user input
user_input = tk.StringVar()
entry_field = tk.Entry(root, textvariable=user_input, width=50)
entry_field.grid(column=0, row=1, padx=10, pady=10)

# Button to send the user input
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(column=1, row=1, padx=10, pady=10)

# Run the Tkinter main loop
root.mainloop()
