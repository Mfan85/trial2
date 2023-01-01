# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 20:22:08 2023

@author: D103918
"""

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form method="POST">
            <input type="text" name="input_string">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/', methods=['POST'])
def handle_form():
    input_string = request.form['input_string']
    return f'You entered: {input_string}'

if __name__ == '__main__':
    app.run()