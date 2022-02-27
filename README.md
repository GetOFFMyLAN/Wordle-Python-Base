# Python Wordle
This is a python implementation of the popular word guessing game 
Wordle. It uses a predefined list of words from a dictionary, generates
the index for the random word, and removes the word from the word
list so that no duplicate word is generated.

# Dependencies
- `Dictionary.py` - the module containing the list of words
- `tkinter` - used for GUI implementation

Tkinter is included in the standard python lib so no installation
should be required. You can read the docs [here](tkdocs.com/tutorial/install.html)

# Instructions
The original Wordle game (created by [Josh Wardle](https://powerlanguage.co.uk/)) 
is a simple word guessing game where a player has a maximum of
6 attempts to guess a single 5 letter word. If a letter is in
the word but not in the right spot, the letter has a yellow
background color. If a letter is both in the word **and** in the
right spot then it has a green background color. Otherwise, the 
letter does not have a background color.

In this version, cyan is used instead of yellow to signify a letter
being in the word but in the wrong spot. This is done to improve 
readability on windows terminals.

# Future Updates
These scripts will be modified to include:
- a timing system to generate a new word every day
- user statistics to keep track of streaks and attempts each day
- A GUI desktop app of the game
    - Includes themes (dark/light)
    - usernames
    - save files
- a multiplayer functionality where players all try to guess the
word the fastest
- a module to allow integration to web-based projects
