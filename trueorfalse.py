# Quiz Program: True/False Only

def true_false_question(question, correct_answer):
    print("\nTrue/False Question:")
    print(question)
    user_answer = input("Your answer (True/False): ").strip().capitalize()
    if user_answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print("Incorrect")
        return 0

# Quiz Questions
questions = [
    {
        "type": "true_false",
        "question": "The Sun rises in the East.",
        "answer": "True"
    },
    {
        "type": "true_false",
        "question": "Humans can breathe underwater without equipment.",
        "answer": "False"
    },
    {
        "type": "true_false",
        "question": "The Earth is round.",
        "answer": "True"
    },
]

# Run Quiz
score = 0
print("Welcome to the True/False Quiz!\n")

for q in questions:
    score += true_false_question(q["question"], q["answer"])

print(f"\nQuiz Over! Your Total Score: {score}/{len(questions)}")
