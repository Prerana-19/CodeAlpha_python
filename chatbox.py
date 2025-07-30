def simple_chatbot():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input == 'hello' or user_input == 'hi':
            print("Chatbot: Hi!")
        elif 'how are you' in user_input:
            print("Chatbot: I'm fine, thanks!")
        elif user_input == 'bye' or user_input == 'goodbye':
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: I didn't understand that. Can you try something else?")

# Start the chatbot
simple_chatbot()
