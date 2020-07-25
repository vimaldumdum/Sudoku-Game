from flask import Flask, render_template

a = [5, 8, 0, 2, 5, 89, -4, 4356, -365]

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('board.html')

@app.route('/home/<int:name>')
def hel(name):
    if name == 1:
        return "hello, vimal"
    else:
        return "hello"

if __name__ == "__main__":
    app.run(debug = True)
