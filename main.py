from MealBot import MealRecommenderBot  # Import the MealRecommenderBot class from the MealBot module



# Example usage when the script is run directly
if __name__ == "__main__":
    bot = MealRecommenderBot()  # Create an instance of the bot
    print("Hi! I'm your personal meal assistant. Ask me what to eat, or tell me your preferences. Type 'exit' to quit.")

    # Loop to keep the conversation going
    while True:
        user_input = input("You: ")  # Get user input
        if user_input.lower() == "exit":  # Exit condition
            print("MealBot: Enjoy your meal! See you next time.")
            break

        # Get and print the bot's response
        response = bot.ask(user_input)
        print("\n MealBot:", response)
