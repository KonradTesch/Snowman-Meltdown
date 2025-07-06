import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]
# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


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
    print(f"Word: {displayed_word}")



def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    mistakes = 0
    guessed_letters = []
    # TODO: Build your game loop here.

    display_game_state(mistakes, secret_word, guessed_letters)
    # For now, simply prompt the user once:
    guess = input("Guess a letter: ").lower()
    guessed_letters.append(guess)
    print("You guessed:", guess)


if __name__ == "__main__":
    play_game()