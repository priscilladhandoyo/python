questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "B"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote 'Harry Potter and the Philosopher's Stone'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K Rowling", "D. Ernest Hemingway"],
        "answer": "C"
    }
]

#function to run the quiz
def run_quiz(questions):
    score = 0

    #for loop to run through the questions
    for question in questions: 
        print(question["prompt"])

        #for loop to run through the options to make a different lines for every option
        for option in question["options"]: 
            print(option) 

        #ask the user for the answer
        answer = input("Enter your anser(A, B, C, or D): ").upper()

        #check the answer
        if answer == question["answer"]:
            print("Correct, hooray!!\n")
            score += 1
        else:
            print("Wrong, LOSERRR!! The correct answer was ", question["answer"], "\n")

    print(f"You got {score} out of {len(questions)} questions correct.")

run_quiz(questions)