import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def is_game_over(mistakes, guessed_letters, secret_word):
    if mistakes >= 3:
        return True

    for char in secret_word:
        if char not in guessed_letters:
            return False

    return True


def is_game_won(mistakes):
    """Checks if the game round is won"""
    return mistakes < 3


def display_win(secret_word):
    """Displays when the player wins the game."""
    display_word = ""

    for char in secret_word:
        display_word += char + " "

    print(f"\nWord: {display_word}")
    print("Congratulation, you saved the snowmen!")


def display_game_over(secret_word):
    """Displays when the player lost the game."""

    print(f"{STAGES[-1]}\n")
    print(f"Game Over! The word was: {secret_word}")


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Displays the current game state
    """
    print(f"{STAGES[mistakes]}\n")

    displayed_word = ""

    for char in secret_word:
        if char in guessed_letters:
            displayed_word += char + " "
        else:
            displayed_word += "_ "
    print(f"Word: {displayed_word}\n")


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")

    mistakes = 0
    guessed_letters = []

    while not is_game_over(mistakes, guessed_letters, secret_word):
        display_game_state(mistakes, secret_word, guessed_letters)
        # For now, simply prompt the user once:
        guess = input("Guess a letter: ").lower()
        guessed_letters.append(guess)
        if guess not in secret_word:
            mistakes += 1
        print("You guessed:", guess)

    if is_game_won(mistakes):
        display_win(secret_word)
    else:
        display_game_over(secret_word)


if __name__ == "__main__":
    play_game()