import random
class VirtualAssistant:
    def __init__(self):
        # Initialise the virtual assistant with a set of predefined responses 
        self.responses = {
            "hello": ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Greetings! How may I help you?"],
            "bye": ["Goodbye! Have a great day!", "See you later!", "Take care!"],
            "default": ["I'm not sure how to respond to that. Can you ask something else?", "I don't have an answer for that right now. Please ask me something else", "Could you please rephrase your question?"],
            "support hours": ["Our support team is available from 9 AM to 6 PM, Monday to Friday.", "We’re open for support between 9am–6pm on weekdays.", "Support hours are 9AM–6PM, Mon to Fri."],
            "how are you": ["I'm just a program, but thanks for asking!", "Doing well, how about you?", "I'm here to assist you!"],
            "what is your name": ["I am a virtual assistant.", "You can call me Assistant.", "I'm your friendly AI assistant."],
            "what can you do": ["I can answer questions, provide information, and assist with tasks.", "I can help with a variety of inquiries.", "I'm here to assist you with whatever you need."],
            "return policy": ["You can return any item within 30 days of purchase.", "Our return policy allows returns within 30 days. Would you like the steps?", "Returns are accepted within 30 days — do you need help with one?"],
            "order status": ["You can check your order status on our website.", "To check your order status, please visit our order tracking page.", "Order status can be found in your account on our site."],
            "payment methods": ["We accept credit cards, PayPal, and bank transfers.", "You can pay using credit card, PayPal, or bank transfer.", "Payment options include credit card, PayPal, and bank transfer."],
        }
    # This method will return a response based on the user's input
    def get_response(self, user_input):
        user_input = user_input.lower()
        # Check if the user input matches any of the predefined responses
        for key in self.responses:
            # Check if the user input contains the key
            if key == user_input:
                # Return a random response from the list of responses for that key
                return random.choice(self.responses[key])
        # If no match is found, return a default response
        return random.choice(self.responses["default"])