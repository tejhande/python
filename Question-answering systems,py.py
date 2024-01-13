import re

# Define a dictionary to store some sample questions and answers
qa_dict = {
    "What is the capital of France?": "Paris",
    "Who is the current President of the United States?": "Joe Biden",
    "What is the currency of Japan?": "Yen",
    "What is the population of India?": "Approximately 1.366 billion"
}

def answer_question(question):
    for q, a in qa_dict.items():
        if re.search(q, question, re.IGNORECASE):
            return a
    return "I'm sorry, I don't have the answer to that question."

# Continuously prompt the user for a question
while True:
    user_question = input("You: ")
    if user_question.lower() in ['bye', 'quit', 'exit']:
        print("QA system: Goodbye! Have a great day.")
        break
    else:
        answer = answer_question(user_question)
        print(f"QA system: {answer}")
