import random

# Define a dictionary of pre-defined responses
responses = {
    "hi":"Hello there",
    "What's your name": "My name is Chatbot.",
    "How old are you": "I don't have an age. I'm a machine.",
    "Where do you live": "I live in the computer.",
    "What's your favorite color": "I don't have a favorite color.",
    "What's your favorite food": "I don't eat food. I'm a machine.",
    "Do you have any pets": "No, I don't have any pets.",
    "What's your hobby": "I don't have hobbies. I'm a chatbot.",
    "What's your job": "My job is to chat with people.",
    "What's your favorite movie": "I don't watch movies. I'm a machine.",
    "What's your favorite book": "I don't read books. I'm a chatbot.",
    "Do you like sports": "I don't have opinions about sports. I'm a machine.",
    "What's your favorite sport": "I don't have a favorite sport. I'm a chatbot.",
    "What's your favorite music genre": "I don't have preferences for music genres.",
    "Do you play any instruments": "No, I don't play any instruments.",
    "What's your favorite holiday": "I don't have a favorite holiday.",
    "What's your favorite place to visit": "I don't travel. I'm a machine.",
    "What's your favorite animal": "I don't have a favorite animal. I'm a chatbot.",
    "What's your favorite thing to do": "I like chatting with people.",
    "Do you prefer tea or coffee": "I don't drink beverages. I'm a machine.",
    "What's your favorite season": "I don't have a favorite season. I'm a chatbot.",
}

def chatbot_response(user_input):
    for question, response in responses.items():
        if user_input.lower() == question.lower():
            return response

    return "Sorry, I didn't understand. Can you please rephrase?"

print("ChatBot: Hello! I'm a chatbot. Ask me anything!")

while True:
    user_input = input("User: ")

    # Check if the user wants to quit
    if user_input.lower() == "quit":
        print("ChatBot: Goodbye!")
        break

    # Respond
    response = chatbot_response(user_input)
    print("ChatBot:", response)
