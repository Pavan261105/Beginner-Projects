import random

def choose_word():
    word_list = ['python', 'hangman', 'developer', 'programming', 'computer', 'keyboard', 'algorithm']
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    guessed_word = False
    word_len = len(word)

    print("Welcome to Hangman!")
    print(f"The word has {word_len} letters.")
    
    while attempts > 0 and not guessed_word:
        print(f"\nYou have {attempts} attempts left.")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print("Word: " + display_word(word, guessed_letters))
        
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'")
            continue
        
        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Oops! '{guess}' is not in the word.")
        
        if all(letter in guessed_letters for letter in word):
            guessed_word = True

    if guessed_word:
        print(f"\nCongratulations! You've guessed the word: {word}")
    else:
        print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    hangman()