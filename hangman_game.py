import random

words = ['test', 'programming', 'word', 'hangman', 'administrator']
word = random.choice(words)
guessed_word = ["_"] * len(word)
guessed_letters = set()
lives = 6

print("Welcome to Hangman!")
print(" ".join(guessed_word))

while lives > 0 and "_" in guessed_word:
    guess = input("Guess: ").lower()

    if guess in guessed_letters:
        print("You already have typed that letter...")
        continue

    guessed_letters.add(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess   
        print("Correct guess")
    else:
        lives -= 1
        print(f"Wrong! Lives remaining: {lives}")

    print(" ".join(guessed_word))

if "_" not in guessed_word:
    print("Congratulations! You found the word")
    print(word)
else:
    print("Game over! The word was:", word)