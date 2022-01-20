# File for parsing the raw_word_list


# Global Variable

BLACKLIST = '0123456789+=-/;.[]{}()~^`'


def generate_word_size_n(filename, n):
    "Generates a file named filename containing the words of length n"

    with open('raw_word_list.txt', 'r') as f:
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


generate_word_size_n('word_size_5.txt', 5)
