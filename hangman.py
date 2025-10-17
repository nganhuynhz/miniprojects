import random
stages = [
r'''    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
=========''',
r'''    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
=========''',
r'''    +---+
    |   |
    O   |
   /|\  |
        |
        |
=========''',
r'''    +---+
    |   |
    O   |
   /|   |
        |
        |
=========''',
r'''
        +---+
    |   |
    O   |
    |   |
        |
        |
=========''',
r'''    +---+
    |   |
    O   |
        |
        |
        |
=========''',
r'''    +---+
    |   |
        |
        |
        |
        |
=========''',]

# Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
print ("Welcome to the hangman game. You have in total 6 lives and our topic today is animals.")
print ("Here is a hint.")
chosen_word = random.choice(words)
display = ""
for letter in chosen_word:
    display += "_"
print(display)
lives = 6
guessed = []
while "_" in display:
    guess = input("What is your guess? ").lower()
    if guess in guessed:
        print(f"You've already guessed {guess}.")
        continue
    if guess in chosen_word:
        print(f"Hooray {guess} is in the word.")
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            guessed.append(letter)
        elif letter in guessed:
            display += letter
        else:
            display += "_"
    if guess not in chosen_word:
        lives -= 1
        print(f"Sorry, you've just lost 1 live. You have {lives} left.")
    print(stages[6 - lives])
    if lives == 0:
        break
    print(display)
if "_" not in display:
    print("You've won!")
else:
    print(f"You've lost. The word is {chosen_word}.")
