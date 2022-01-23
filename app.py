from flask import Flask, render_template, request
from pyrsistent import v
from main import get_new_word, new_game, valid_word, get_letter_score


app = Flask(__name__)

secret_word = get_new_word(5)

GAME_START = False

Score = []
ruleset = 'closeness'


@app.route('/', methods=['GET', 'POST'])
def index():

    global ruleset
    global Score

    if request.method == 'POST':

        if len(request.form) > 1:

            # It was a guess
            #guessed_word = 'ponto'
            guessed_word = ''.join(request.form[key]
                                   for key in request.form.keys()).lower()

            print(guessed_word, secret_word)

            if valid_word(guessed_word) == True:

                Current_Score = []

                for i, j in zip(guessed_word, secret_word):

                    Current_Score += [[i, get_letter_score(i, j, ruleset)]]

                Score += [Current_Score]

                return render_template("index.html", score=Score)
        if len(request.form) == 1:

            ruleset = request.form['ruleset']

            print(" ")
            print(" RULESET CHANGED TO " + ruleset)
            print(" ")

    return render_template("index.html")
