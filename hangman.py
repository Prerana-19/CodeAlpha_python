import random

def hangman():
    # Predefined list of words
    words = ["python", "hangman", "program", "computer", "keyboard"]
    secret_word = random.choice(words).lower()
    guessed_letters = []
    attempts = 6
    
    print("Welcome to Hangman!")
    print(f"Guess the word. It has {len(secret_word)} letters.")
    
    while attempts > 0:
        # Display current progress
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word.strip())
        
        # Check if player won
        if "_" not in display_word:
            print(f"Congratulations! You guessed the word: {secret_word}")
            return
        
        # Get player's guess
        guess = input("Guess a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # Check if letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue
        
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in secret_word:
            print("Correct!")
        else:
            attempts -= 1
            print(f"Wrong! You have {attempts} attempts left.")
    
    # If we get here, player ran out of attempts
    print(f"Game over! The word was: {secret_word}")

# Start the game
hangman()
