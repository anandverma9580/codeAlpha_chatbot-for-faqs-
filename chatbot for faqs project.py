import re

# Define FAQs as a dictionary: key is a regex pattern for matching questions, value is the answer.
faqs = {
    r"(?i)what is this project": "This is a chatbot for answering FAQs about [Your Topic]. It's designed to be helpful and efficient.",
    r"(?i)how do I get started": "Simply ask a question! For example, type 'help' or a specific query like 'What is this project?'",
    r"(?i)can I customize": "Yes, you can add more FAQs, integrate APIs, or tweak the logic in the code.",
    r"(?i)help": "I'm here to answer FAQs. Try asking about the project, getting started, or customization.",
    r"(?i)quit|exit": "Goodbye! Feel free to come back anytime."
}

def match_faq(user_input):
    for pattern, answer in faqs.items():
        if re.search(pattern, user_input):
            return answer
    return "I'm sorry, I don't have info on that. Try rephrasing or contact support at support@example.com."

def main():
    print("Hi! I'm the FAQ Bot for [Your Project]. How can I help today? (Type 'quit' to exit)")
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        response = match_faq(user_input)
        print(f"Bot: {response}")
        if "Goodbye" in response:
            break

if __name__ == "__main__":
    main()
