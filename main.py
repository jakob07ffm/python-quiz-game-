import time

# Question bank (questions, options, correct answer)
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
        "answer": "A"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A) Gold", "B) Oxygen", "C) Hydrogen", "D) Silver"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A) Charles Dickens", "B) Leo Tolstoy", "C) William Shakespeare", "D) Mark Twain"],
        "answer": "C"
    },
    {
        "question": "What is the largest planet in our Solar System?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "C"
    },
    {
        "question": "Which language is used to create this quiz game?",
        "options": ["A) Java", "B) C++", "C) Python", "D) Ruby"],
        "answer": "C"
    }
]

def start_quiz():
    score = 0
    total_questions = len(questions)
    question_time_limit = 10  # seconds

    print("Welcome to the Quiz Game!")
    print("You have 10 seconds to answer each question.")
    print("Let's start!\n")

    for i, question in enumerate(questions):
        print(f"Question {i + 1}: {question['question']}")
        for option in question['options']:
            print(option)
        
        start_time = time.time()
        answer = input("Your answer (A/B/C/D): ").upper()
        end_time = time.time()

        if end_time - start_time > question_time_limit:
            print("Time's up! You didn't answer in time.")
        elif answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
        print(f"The correct answer was: {question['answer']}")
        print("\n")

    print(f"Quiz Over! Your final score is {score} out of {total_questions}.")

# Start the quiz game
start_quiz()
