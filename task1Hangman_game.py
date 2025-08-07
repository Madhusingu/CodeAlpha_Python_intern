import random

words = ["python", "hangman", "college", "program", "debug"]
secret_word = random.choice(words)
guessed = []
tries = 6
hidden_word = ["_"] * len(secret_word)

print("🎮 Welcome to Hangman!")
print(f"The word has {len(secret_word)} letters.")

while tries > 0 and "_" in hidden_word:
    print("\nWord: ", " ".join(hidden_word))
    print(f"Guesses left: {tries}")
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Enter one valid letter.")
        continue
    if guess in guessed:
        print("😅 You already guessed that letter.")
        continue

    guessed.append(guess)

    if guess in secret_word:
        print("✅ Correct guess!")
        for i, letter in enumerate(secret_word):
            if letter == guess:
                hidden_word[i] = guess
    else:
        print("❌ Wrong guess.")
        tries -= 1

if "_" not in hidden_word:
    print("\n🎉 You won! The word was:", secret_word)
else:
    print("\n💥 Out of tries! The word was:", secret_word)
