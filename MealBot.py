import os
from dotenv import load_dotenv
from openai import OpenAI

# Define a class for the meal recommendation chatbot
class MealRecommenderBot:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        api_key = os.getenv("OPENAI_API_KEY")
        # Create an OpenAI client instance 
        self.client = OpenAI(api_key=api_key)

        # Define the system prompt to guide the assistant's behaviour this will be used to set the context for the conversation
        self.system_prompt = (
            "You are a friendly, knowledgeable, and responsive meal planning assistant designed to engage in natural conversation with users."
            " Begin by greeting the user and asking if they have any dietary preferences, dislikes, allergies, or nutritional goals."
            " Recommend meals based on this information, ensuring that each response includes a specific dish name, a list of ingredients, and simple cooking instructions."
            " Always avoid any ingredients the user has indicated they dislike or are allergic to."
            " If a user's input is unclear or lacks detail, ask relevant follow-up questions to clarify their needs and guide the conversation."
            " Maintain a helpful, polite tone, and tailor responses to the user’s needs to enhance user experience."
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