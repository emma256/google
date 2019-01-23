
from flask import Flask,render_template
app = Flask(__name__)


@app.route("/") #this is how navigation routes are written in python
def main():#this a python function
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug="True")