## Hot or Cold ##
#################

# Basically there are 2 different rulesets:

# Ruleset 1:

# For every letter recieved, there are 3 possible outcomes:

# Correct (Green)
# Hot (Red)
# Cold (Blue)


# Main Constants:

import numpy as np
from string import ascii_lowercase

alphabet = ascii_lowercase

# numpy


# Main Functions:


def letter_score(guessed_letter, correct_letter, ruleset):
    """ Function that returns if given letter is either corret, hot or cold

            There are 2 different rulesets for determining wether a letter is hot or cold:

            - Closeness ruleset
            - Height ruleset

        - Closeness :

            - The letter is hot (resp. cold) if the index of the correct letter is closer than not from the index of the given letter.  

            Example:

                If the correct letter is "G". 

                    The guessed letter was "H". 
                        It returns 'Hot'. 

                    The guessed letter was "F":
                        It returns 'Hot'.


                    The guessed letter was "Z":
                        It returns 'Cold'.

        - Height:

            - The letter is hot (resp. cold) if the index is higher than the index of the correct letter

            Example:

                If the correct letter is "G". 

                    The guessed letter was "H". 
                        It returns 'Hot'. 

                    The guessed letter was "F":
                        It returns 'Cold'.

            """

    # Ruleset if valid
    try:
        assert ruleset in ['closeness', 'height']
    except:
        print("Ruleset must be either closeness or height.")

    if guessed_letter == correct_letter:
        # Correct guess.
        return 'Green'

    if ruleset == 'height':

        if ord(guessed_letter) > ord(correct_letter):
            return 'Hot'

        else:
            return 'Cold'

    if ruleset == 'closeness':

        if abs(ord(guessed_letter) - ord(correct_letter)) <= 6:
            return 'Hot'

        else:
            return 'Cold'


def get_new_word(size):

    # Size in string please
    size = str(size)

    with open('word_size_' + size + '.txt', 'r') as f:
        X = f.readlines()
    random_word = np.random.randint(len(X))

    return X[random_word]


def new_game(size, ruleset):
    """
    Main Function.

    Ruleset \in ('height', 'closeness')
    """

    TARGET_WORD = get_new_word(size)

    GAME_OVER = False

    Current_turn = 0
    print('The current ruleset is ' + ruleset)
    print('The word lenght is ' + str(size))
    while not GAME_OVER:

        print('Type your guess.')
        Current_Guess = input()

        Current_Score = []
        Current_turn += 1

        for i, j in zip(Current_Guess, TARGET_WORD):
            score_i = letter_score(i, j, ruleset)

            Current_Score.append(score_i)
        print(Current_Score)

        if Current_turn > 5:

            GAME_OVER = True

    return 'Game Over'


# if __name__ ==

new_game(5, 'height')
