#!/usr/bin/env python3

from flask import (
    Flask,
    render_template,
)


app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test1')
def test_one():
    return render_template('test1.html')


@app.route('/test2')
def test_two():
    return render_template('test2.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
