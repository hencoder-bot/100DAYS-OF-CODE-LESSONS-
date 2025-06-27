word_list = ["ardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)

print(f"psss the solution is {chosen_word}")
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")

#CORRECTION
word_list = ["ardvark", "baboon", "camel"]
import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''']

chosen_word = random.choice(word_list)
print(f"psss the solution is {chosen_word}")
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    
    print(f"{' '.join(display)}")
    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win.")