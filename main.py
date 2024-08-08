import random
import time

# Question bank categorized by difficulty levels and topics
question_bank = {
    "General Knowledge": {
        "easy": [
            {
                "question": "What is the capital of France?",
                "options": ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
                "answer": "A",
                "hint": "It's known as the city of love."
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["A) Venus", "B) Saturn", "C) Mars", "D) Jupiter"],
                "answer": "C",
                "hint": "This planet is named after the Roman god of war."
            }
        ],
        "medium": [
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["A) Leonardo da Vinci", "B) Pablo Picasso", "C) Vincent van Gogh", "D) Michelangelo"],
                "answer": "A",
                "hint": "The artist is also known for his work on the Last Supper."
            },
            {
                "question": "In which year did the Titanic sink?",
                "options": ["A) 1912", "B) 1923", "C) 1905", "D) 1918"],
                "answer": "A",
                "hint": "The event occurred in April."
            }
        ],
        "hard": [
            {
                "question": "Which is the smallest country in the world?",
                "options": ["A) Monaco", "B) Vatican City", "C) San Marino", "D) Liechtenstein"],
                "answer": "B",
                "hint": "This country is located within the city of Rome."
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A) O", "B) A", "C) AB-negative", "D) B-negative"],
                "answer": "C",
                "hint": "This type is found in less than 1% of the world's population."
            }
        ]
    },
    "Science": {
        "easy": [
            {
                "question": "What is the chemical symbol for water?",
                "options": ["A) O2", "B) H2O", "C) CO2", "D) NaCl"],
                "answer": "B",
                "hint": "It's made of two hydrogen atoms and one oxygen atom."
            },
            {
                "question": "Which planet is closest to the Sun?",
                "options": ["A) Venus", "B) Mars", "C) Mercury", "D) Earth"],
                "answer": "C",
                "hint": "It's the smallest planet in our Solar System."
            }
        ],
        "medium": [
            {
                "question": "What is the most abundant gas in Earth's atmosphere?",
                "options": ["A) Oxygen", "B) Hydrogen", "C) Nitrogen", "D) Carbon Dioxide"],
                "answer": "C",
                "hint": "This gas makes up about 78% of the atmosphere."
            },
            {
                "question": "Which element has the atomic number 1?",
                "options": ["A) Helium", "B) Oxygen", "C) Hydrogen", "D) Carbon"],
                "answer": "C",
                "hint": "This element is the lightest and most abundant in the universe."
            }
        ],
        "hard": [
            {
                "question": "What is the powerhouse of the cell?",
                "options": ["A) Nucleus", "B) Ribosome", "C) Mitochondria", "D) Endoplasmic Reticulum"],
                "answer": "C",
                "hint": "This organelle produces energy in the form of ATP."
            },
            {
                "question": "Which planet has the most moons?",
                "options": ["A) Jupiter", "B) Saturn", "C) Uranus", "D) Neptune"],
                "answer": "B",
                "hint": "This planet has rings and more than 80 moons."
            }
        ]
    }
}

def start_quiz():
    high_score = 0
    print("Welcome to the Advanced Quiz Game!")
    print("Choose a category:")
    categories = list(question_bank.keys())
    for i, category in enumerate(categories):
        print(f"{i + 1}) {category}")
    category_choice = int(input("Enter the number of your choice: ")) - 1
    selected_category = categories[category_choice]
    
    print("Choose a difficulty level:")
    difficulties = ["easy", "medium", "hard"]
    for i, level in enumerate(difficulties):
        print(f"{i + 1}) {level.capitalize()}")
    difficulty_choice = int(input("Enter the number of your choice: ")) - 1
    selected_difficulty = difficulties[difficulty_choice]
    
    questions = question_bank[selected_category][selected_difficulty]
    random.shuffle(questions)
    
    score = 0
    lifelines = {"50-50": True, "Hint": True}
    
    for question_data in questions:
        print(f"Question: {question_data['question']}")
        for option in question_data['options']:
            print(option)
        
        if lifelines["50-50"] or lifelines["Hint"]:
            print("Available lifelines:")
            if lifelines["50-50"]:
                print("1) 50-50 (remove two incorrect answers)")
            if lifelines["Hint"]:
                print("2) Hint")
            use_lifeline = input("Would you like to use a lifeline? (Y/N): ").upper()
            if use_lifeline == "Y":
                lifeline_choice = int(input("Enter 1 for 50-50 or 2 for Hint: "))
                if lifeline_choice == 1 and lifelines["50-50"]:
                    correct_option = question_data['answer']
                    incorrect_options = [opt for opt in question_data['options'] if opt[0] != correct_option]
                    options_to_remove = random.sample(incorrect_options, 2)
                    print("Remaining options:")
                    print(correct_option)
                    for option in question_data['options']:
                        if option not in options_to_remove and option != correct_option:
                            print(option)
                    lifelines["50-50"] = False
                elif lifeline_choice == 2 and lifelines["Hint"]:
                    print(f"Hint: {question_data['hint']}")
                    lifelines["Hint"] = False
        
        start_time = time.time()
        answer = input("Your answer (A/B/C/D): ").upper()
        end_time = time.time()
        
        if end_time - start_time > 10:
            print("Time's up! You didn't answer in time.")
        elif answer == question_data['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
        print(f"The correct answer was: {question_data['answer']}\n")
    
    if score > high_score:
        high_score = score
        print(f"New high score: {high_score}")
    else:
        print(f"Your score: {score}")
    print(f"High score: {high_score}")

start_quiz()
