from flask import Flask

app = Flask(__name__)

def home():
    response1 = requests.get('https://service2:5001')
    response2 = requests.get('https://service3:5002')
    return response1 +" "+ response2