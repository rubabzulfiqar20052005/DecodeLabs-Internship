# Rule-Based AI Chatbot - Project 1 (DecodeLabs Internship)
import random
responses = {
    ("hello", "hi", "hey", "hii", "helo"): "Hey there! How's it going?",
    ("how are you", "how're you","what are you doing", "how you doing"): "I'm just a bunch of code but I'm doing great, thanks for asking!",
    ("what is your name", "your name", "who are you"): "I'm your friendly rule-based chatbot, built at DecodeLabs.",
    ("who made you", "who created you", "who built you"): "I was built as part of an AI internship project. Pretty cool huh?",
    ("what can you do", "your abilities", "your features"): "Right now, I can only chat based on fixed rules - no deep learning yet!",
    ("help", "commands", "options"): "You can say hi, ask my name, ask how I'm doing, or just say bye to leave.",
    ("thanks", "thank you", "thnx"): "You're welcome! Happy to help.",
    ("what time is it", "current time"): "Sorry, I don't have a clock inside me yet.",
    ("are you real", "are you a bot", "are you human"): "As real as lines of code can be!",
    ("i am sad", "i am not happy", "feeling low"): "Aww, I'm sorry to hear that. Hope your day gets better!",
    ("i am happy", "feeling good", "i am great"): "That's awesome to hear! Keep that energy up.",
    ("good morning", "gm"): "Good morning! Hope you have a productive day ahead.",
}

exit_commands = ["bye", "exit", "quit", "goodbye"]
last_topic = None
flat_responses = {}
for keywords, reply in responses.items():
    for word in keywords:
        flat_responses[word] = reply

print("Chatbot: Hello! I'm your DecodeLabs chatbot. Type 'bye' anytime to end the chat.")

while True:
    raw_input = input("You: ")
    user_input = raw_input.lower().strip()

    if user_input in exit_commands:
        print("Chatbot: Goodbye! Take care.")
        break

    if user_input == "why" and last_topic == "mood":
        print("Chatbot: Just having one of those days, I guess. What about you, everything okay?")
        continue

    if user_input in flat_responses:
        reply = flat_responses[user_input]
    else:
        reply = None
        for keyword in flat_responses:
            if keyword in user_input:
                reply = flat_responses[keyword]
                break
        if reply is None:
            reply = "Hmm, I don't quite understand that yet."

    if user_input in ("i am sad", "i am not happy", "feeling low"):
        last_topic = "mood"
    else:
        last_topic = None

    print("Chatbot:", reply)