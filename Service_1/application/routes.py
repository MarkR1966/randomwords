from application import app
from flask import render_template

@app.route('/', methods = ['GET'])
def home():
    response = requests.get('https:service4:5003')
    return render_template('index.html', data = response)