# imports
from Dictionary import words
from random import randrange
import os

# class definitions


class GuessManager:
    num_guesses = 0
    word = ""
    word_size = 0
    guess_list = []
    guess_values = []
    word_found = False

    def __init__(self, n, w, gl):
        self.num_guesses = n
        self.word = w
        self.word_size = len(w)
        self.guess_list = gl

    # static methods

    @staticmethod
    def print_green(char):
        out = u'\u001b[42;30m' + char + u'\u001b[0m'
        print(out, end="")

    @staticmethod
    def print_yellow(char):
        out = u'\u001b[46;30m' + char + u'\u001b[0m'
        print(out, end="")

    @staticmethod
    def print_default(char):
        out = u'\u001b[49;30m' + char + u'\u001b[0m'
        print(out, end="")

    # public methods

    def check_guess(self, guess):
        """
        checks the guess against the word and sees if each character in the guess is in the right
        spot or is even in the word at all
        :param guess: string, user inputted guess for the word
        :return: a list containing integers that represent correctness of guess: 0 = not in word, 1 = in word but
                wrong spot, 2 = in word right spot
        """
        if len(guess) != self.word_size:
            raise ValueError("User guess is not the same length as the word")
        self.guess_list.append(guess)

        correctness = []
        for i in range(self.word_size):
            if guess[i].lower() == self.word[i]:
                correctness.append(2)
            elif self.word.find(guess[i]) != -1:
                correctness.append(1)
            else:
                correctness.append(0)

        self.guess_values.append(correctness)
        return correctness

    def word_found(self):
        for i in self.guess_values[len(self.guess_values) - 1]:
            if i != 2:
                return False
        return True

    def display_guesses(self):
        for i in range(len(self.guess_list)):
            for j in range(5):
                char = self.guess_list[i][j]
                if self.guess_values[i][j] == 2:
                    self.print_green(char)
                elif self.guess_values[i][j] == 1:
                    self.print_yellow(char)
                else:
                    self.print_default(char)
            print()

    def get_guesses(self):
        return self.guess_values

# function definitions


def generate_word(words):
    if len(words) == 0:
        raise ValueError("empty word list passed in generate_word() call")

    key = randrange(0, len(words))
    return (words[key], key)


def init_game():
    def clear():
        os.system("cls")
    # allows for ansi escape chars to get processed correctly
    os.system("")
    # generate word and remove it from list so that it can't be used twice
    w_list = words
    word_key_pair = generate_word(w_list)
    word_to_guess = word_key_pair[0]
    word_index = word_key_pair[1]
    w_list.pop(word_index)

    # initialize controller to check guesses and start game
    num_guesses = 0
    controller = GuessManager(num_guesses, word_to_guess, [])
    word_found = False
    while num_guesses < 6 and not word_found:
        try:
            clear()
            controller.display_guesses()
            guess = str(input("Guess: "))
            controller.check_guess(guess)
            word_found = controller.word_found()
            num_guesses += 1
        except ValueError:
            print("invalid guess. try again")
            pass

    clear()
    controller.display_guesses()

    print("Guesses: {g}".format(g=num_guesses))
    if not word_found:
        print()
        print("The word was {word}".format(word=word_to_guess))

init_game()
