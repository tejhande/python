import random
import re

# Use the regular expression library to define some common greetings
greetings = re.compile(r'(hi|hello|hey|hey there|greetings|good morning|good afternoon|good evening)', re.IGNORECASE)

# Use a list to store some possible chatbot responses
responses = [
    "Hi there!",
    "Hello!",
    "Hey!",
    "Greetings!",
    "Nice to meet you!",
    "How can I help you today?"
]

def chatbot(user_input):
    # Check if the user input matches one of the defined greetings
    if greetings.search(user_input):
        # If so, return a random response from the list of responses
        return random.choice(responses)
    elif user_input.lower() in ['support', 'help', 'assistance']:
        return "Would you like to contact support for assistance?"
    else:
        # If not, return a default response
        return "I'm sorry, I don't understand what you're saying."

# Continuously prompt the user for input
while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'quit', 'exit']:
        print("Chatbot: Goodbye! Have a great day.")
        break
    else:
        chatbot_response = chatbot(user_input)
        print(f"Chatbot: {chatbot_response}")
