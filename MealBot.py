import os
from dotenv import load_dotenv
from openai import OpenAI

# Define a class for the meal recommendation chatbot
class MealRecommenderBot:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        api_key = os.getenv("OPENAI_API_KEY")
        # Create an OpenAI client instance using the new SDK
        self.client = OpenAI(api_key=api_key)

        # Define the system prompt to guide the assistant's behaviour this will be used to set the context for the conversation
        self.system_prompt = (
            "You are a helpful and creative meal planning assistant."
            " Your job is to recommend meals based on user preferences, dietary needs, or specific constraints."
            " Always respond with a full meal suggestion, including the dish name, ingredients, and basic instructions."
            " Avoid any ingredients the user mentions as dislikes or allergies."
        )

    # Method to send a message to the OpenAI API and get a response
    def ask(self, user_input):
        # Construct full input to ensure task clarity
        full_prompt = (
            f"User input: {user_input}\n"
            "If the user is asking for a meal, Respond with a suitable meal recommendation based on the input above. If not, respond with a polite message asking for more details.\n"
        )

        # Send user input and system instructions to OpenAI using the new responses API
        response = self.client.responses.create(
            model="gpt-4o",
            instructions=self.system_prompt,
            input=full_prompt
        )

        # Return the response text
        return response.output_text