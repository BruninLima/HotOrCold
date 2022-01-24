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


def get_letter_score(guessed_letter, correct_letter, ruleset):
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

    with open('app\data\word_size_' + size + '.txt', 'r') as f:
        X = f.readlines()
    random_word = np.random.randint(len(X))

    return X[random_word]


def valid_word(word):

    with open('app\data\word_size_5.txt', 'r') as f:
        X = f.readlines()

    if word+'\n' in X:
        return True
    else:
        return False
