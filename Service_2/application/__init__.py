from flask import Flask

app = Flask(__name__)

def home():
    letters="abcdefghijklmnopqrstuvwxyz"
    word = ""
    for i in range (6):
        word += random.choice(letters)
    return word
