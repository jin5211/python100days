from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return '<div style="text-align: center; margin-top: 100px">\
        <h1>Guess a number between 0 and 9</h1>\
        <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGlsdXg4djMxMzdqZWRtcXBhdWR4bjhrN3hhOXE5YTkxc3RpYmh2MCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/6OyrnAKxd46Rfall6K/giphy.gif"/>\
            </div>'


"""
Create a route that can detect the number entered by the user e.g "URL/3" or "URL/9" and checks that number against the generated random number. If the number is too low, tell the user it's too low, same with too high or if they found the correct number. try to make the <h1> text a different colour for each page.  e.g. If the random number was 5:
"""

import random

random_num = random.randint(0, 9)


@app.route("/<int:num>")
def detect_number(num):
    # too low
    if num < random_num:
        return f'<div style="text-align: center; margin-top: 100px; color: red">\
        <h1>Too low, try again!</h1>\
        <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>\
            </div>'

    # too high
    elif num > random_num:
        return f'<div style="text-align: center; margin-top: 100px; color: purple">\
        <h1>Too high, try again!</h1>\
        <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>\
            </div>'

    # correct
    else:
        return f'<div style="text-align: center; margin-top: 100px; color: green">\
            <h1>You found me!</h1>\
            <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>\
                </div>'


if __name__ == "__main__":
    app.run(debug=True)
