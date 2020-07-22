from flask import Flask

app = Flask(__name__)

def home():
    numbers="0123456789"
    word = ""
    for i in range (4):
        word += random.choice(numbers)
    return word