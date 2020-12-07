import random
import time
import string


class Hangman:
    def __init__(self, correct_word):
        self.n_tries = 8
        self.word = correct_word
        self.attempt = "-" * len(correct_word)

    def play(self):
        guesses = []
        while True:
            print(self.attempt)
            char = input("Input a letter: ").strip()
            if len(char) != 1:
                print("You should input a single letter")
            elif char not in string.ascii_lowercase:  # not an lower case character
                print("Please enter a lowercase English letter")
            else:
                if char in self.word and char not in self.attempt:  # correct and never guessed before
                    self.attempt = "".join(char if x == char else self.attempt[i] for i, x in enumerate(self.word))
                    if self.attempt == self.word:  # guessed the whole word
                        print(f"You guessed the word {self.word}!\nYou survived!")
                        break
                elif char in guesses:  # guessed before
                    print("You've already guessed this letter")
                else:  # wrong guess
                    print("That letter doesn't appear in the word")
                    self.n_tries -= 1
                guesses.append(char)
            if self.n_tries == 0:  # if player out of attempts
                print("You lost!")
                break
            else:
                print("")


# Write your code here
print("H A N G M A N\n")
random.seed(time.time())
word = random.choice(['python', 'java', 'kotlin', 'javascript'])
while True:
    in_put = input("Type \"play\" to play the game, \"exit\" to quit: ")
    if in_put == "play":
        Hangman(word).play()
    elif in_put == "exit":
        break
