import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you today?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm good, thanks for asking.", "All good here!"]
    ],
    [
        r"what is your name ?",
        ["You can call me ChatBot.", "I'm ChatBot.", "Just call me ChatBot."]
    ],
    [
        r"what can you do ?",
        ["I can answer your questions and engage in a conversation with you."]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "Bye!", "Take care!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that. Can you please rephrase?", "I'm not sure I follow. Could you say that again?"]
    ]
]

# Create a ChatBot instance
chatbot = Chat(pairs, reflections)

# Function to start the conversation
def start_chat():
    print("Hello! I'm ChatBot. How can I help you today?")
    print("Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    start_chat()
