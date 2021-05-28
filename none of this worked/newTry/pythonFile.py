from flask import Flask
from flask import request
from flask import render_template
import stringComparison

app = Flask(__name__)


@app.route('/')
def my_form():
    # this should be the name of your html file
    return render_template("index.html")


@app.route('/', methods=['POST'])
def my_form_post():
    print("hi Sean")
    text1 = request.form['text1']
    text2 = request.form['text2']
    plagiarismPercent = stringComparison.extremelySimplePlagiarismChecker(
        text1, text2)
    if plagiarismPercent > 50:
        return "<h1>Plagiarism Detected !</h1>"
    else:
        return "<h1>No Plagiarism Detected !</h1>"


if __name__ == '__main__':
    app.run()
