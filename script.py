def run_quiz():
    questions = {
        "What is the capital of France?": {
            "a": "Paris",
            "b": "London",
            "c": "Berlin",
            "d": "Madrid",
            "correct": "a"
        },
        "Which language is primarily spoken in Brazil?": {
            "a": "Spanish",
            "b": "Portuguese",
            "c": "French",
            "d": "English",
            "correct": "b"
        },
        "What is the chemical symbol for gold?": {
            "a": "Au",
            "b": "Ag",
            "c": "Pb",
            "d": "Fe",
            "correct": "a"
        }
    }

    score = 0

    for question, info in questions.items():
        print(question)
        for option, answer in info.items():
            if option in {'a', 'b', 'c', 'd'}:
                print(f"{option}) {answer}")

        # Get user response
        user_answer = input("Enter your answer (a, b, c, or d): ")
        if user_answer == info["correct"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer is", info[info["correct"]], "\n")

    print(f"Your final score is {score}/{len(questions)}.")


if __name__ == "__main__":
    run_quiz()
