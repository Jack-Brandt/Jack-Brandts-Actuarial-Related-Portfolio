'''
Author: Jack Brandt
Description: This is the main file for the flask web app
Notes: Run to start flask server
'''
from flask import Flask,render_template, request


app = Flask(__name__)

# Homepage
@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        return ''
    # If the request method is GET, return the home page
    return render_template('home.html')

@app.route("/exams", methods=["GET", "POST"])
def exams():
    if request.method == "POST":
        return ''
    # If the request method is GET, return the home page
    return render_template('exams.html')

@app.route("/skills", methods=["GET", "POST"])
def skills():
    if request.method == "POST":
        return ''
    # If the request method is GET, return the home page
    return render_template('skills.html')

@app.route("/coding", methods=["GET", "POST"])
def coding():
    if request.method == "POST":
        return ''
    # If the request method is GET, return the home page
    return render_template('coding.html')

@app.route("/resume", methods=["GET", "POST"])
def resume():
    if request.method == "POST":
        return ''
    # If the request method is GET, return the home page
    return render_template('resume.html')

@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "POST":
        return ''
    # If the request method is GET, return the home page
    return render_template('about.html')

@app.route("/contact_me", methods=["GET", "POST"])
def contact_me():
    if request.method == "POST":
        return ''
    # If the request method is GET, return the home page
    return render_template('contact_me.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)