from VirtualAssistant import VirtualAssistant


# Start the chatbot

myChatBot = VirtualAssistant()
print("Welcome to the Virtual Assistant! Type 'exit' to end the conversation.")

# Loop to keep the conversation going until the user types 'exit'
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Assistant: Goodbye!")
        break
    response = myChatBot.get_response(user_input)
    print("Assistant:", response)