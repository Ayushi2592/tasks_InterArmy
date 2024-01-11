import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am good, thank you.', 'I am doing well. How about you?']),
    (r'(.*) your name?', ['I am a chatbot.', 'I go by the name ChatBot.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']),
    (r'(.*) (age|old) are you', ['I have no age.']),
    (r'(.*) (do|can) you (.*?)', ['I am a simple chatbot and can answer basic queries.']),
    (r'what is your purpose', ['My purpose is to assist and provide information.']),
    (r'who created you', ['I was created by a developer using Python.']),
    (r'(.*) (love|hate) you', [' I don\'t have feelings, but I\'m here to help!']),
    (r'(.*) help (.*)', ['I can assist you with various queries. Just ask!']),
    (r'(\d+) (plus|minus|times|divided by) (\d+)', ['Sure, let me calculate that for you.']),
]

# Create a chatbot using the patterns
chatbot = Chat(patterns, reflections)

# Function to perform arithmetic operations
def perform_calculation(match):
    num1 = float(match.group(1))
    operator = match.group(2)
    num2 = float(match.group(3))

    if operator == 'plus':
        result = num1 + num2
    elif operator == 'minus':
        result = num1 - num2
    elif operator == 'times':
        result = num1 * num2
    elif operator == 'divided by':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Cannot divide by zero."

    return f'The result of {num1} {operator} {num2} is {result}.'

# Add the custom action to the chatbot
chatbot._substitute('(\d+) (plus|minus|times|divided by) (\d+)', perform_calculation)

# Function to start the chat
def start_chat():
    print("Hello! I'm your chatbot. Ask me anything or type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Goodbye! Have a great day.")
            break
        else:
            response = chatbot.respond(user_input)
            print("ChatBot:", response)

# Start the chat when the script is run
if __name__ == "__main__":
    start_chat()
