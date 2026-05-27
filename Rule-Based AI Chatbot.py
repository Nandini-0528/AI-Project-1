# Rule-Based AI Chatbot

print("WELCOME TO AI Chatbot")
print("Type 'exit' to stop the chatbot")
print()

# loop continous
while True:

    # taking input from user
    user_input = input("You : ")
    user_input = user_input.lower()

    # greetings
    if user_input == "hi" or user_input == "hello":
        print("Bot : Hello!")

    elif user_input == "good morning":
        print("Bot : Good Morning")

    elif user_input == "good evening":
        print("Bot : Good Evening")

    # simple conversation
    elif user_input == "how are you":
        print("Bot : I am fine. Thank you!")

    elif user_input == "what is ai":
        print("Bot : AI stands for Artificial Intelligence.")

    elif user_input == "what is your name":
        print("Bot : I am a Rule-Based AI Chatbot.")

    elif user_input == "what can you do":
        print("Bot : I can reply to predefined user inputs.")

    elif user_input == "tell me a joke":
        print("Bot: Why do programmers love Python? Because it's easy to understand!")

    elif user_input == "Thankyou":
        print("Bot : you're welcome!")

    # exit command
    elif user_input == "exit":
        print("Bot : Goodbye! Have a nice day")
        break

    # default message
    else:
        print("Bot : Sorry, I don't understand your message.")

print()