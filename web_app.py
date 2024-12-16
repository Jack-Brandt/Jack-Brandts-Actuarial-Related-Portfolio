'''
Author:
Description:
Notes:
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

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)