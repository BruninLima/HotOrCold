# File for parsing the raw_word_list


# Global Variable

BLACKLIST = '0123456789+=-/;.[]{}()~^`'


def generate_word_size_n(filename, n):
    "Generates a file named filename containing the words of length n"

    with open('br_word_list.txt', 'r') as f:
        X = f.readlines()

    with open(filename, 'w') as f:

        for word in X[:-1]:
            if len(word) == n + 2:
                if ' ' in word:
                    word = word[:-2] + word[-1]
            if len(word) == n + 1:
                if ' ' not in word:
                    Flag = 1
                    for i in BLACKLIST:
                        if i in word:
                            Flag = -1

                    if Flag == 1:
                        f.write(word.lower())


def get_largest_word():
    with open('br_word_list.txt', 'r') as f:
        X = f.readlines()

    maxsize = 0
    maxwords = []
    for word in X:
        if len(word) > maxsize:
            maxwords = [word]
            maxsize = len(word)
        if len(word) == maxsize:
            maxwords.append(word)

    return maxsize, maxwords
