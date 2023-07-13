import random

def get_user_input(options):
    while True:
        try:
            # Try to get user input
            choice = int(input("Your choice: ")) - 1
            if 0 <= choice < len(options):
                return choice
            else:
                print("Invalid choice. Please choose a number between 1 and {}.".format(len(options)))
        except (EOFError, NotImplementedError):
            # If input() is not supported, simulate user input
            choice = simulate_user_input(options)
            print(f"Simulated user's choice: {choice + 1}")
            return choice

def vocabulary_training(vocabulary):
    word, translations = random.choice(list(vocabulary.items()))
    print(f"Translate the word '{word}' to Ukrainian:")
    
    options = [translations] + random.sample([v for k, v in vocabulary.items() if k != word], 3)
    random.shuffle(options)
    
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    # Get user input
    answer = get_user_input(options)
    
    if options[answer] == translations:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is: {translations}")

vocabulary = {
    "apple": "яблуко",
    "car": "автомобіль",
    "house": "будинок",
    "boy": "хлопець",
    "girl": "дівчина"
}

vocabulary_training(vocabulary)
