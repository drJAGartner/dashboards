#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template, request, session, abort
import sys, os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/services')



app = Flask(__name__)

@app.route('/')
def home():

        return render_template('index.html')


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=5000, debug=True)