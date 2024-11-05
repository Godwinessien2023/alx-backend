#!/usr/bin/env python3
"""Setup Flask App"""
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    """define route that renders home page
    as index.html
    """
    return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug=True)
