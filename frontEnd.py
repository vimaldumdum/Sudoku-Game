from flask import Flask, render_template
from backEnd import getGrid, solve, isSafe

a = [5, 8, 0, 2, 5, 89, -4, 4356, -365]
grid =  getGrid()
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('board.html', grids = grid)

@app.route('/home/<int:name>')
def hel(name):
    if name == 1:
        return "hello, vimal"
    else:
        return "hello"

if __name__ == "__main__":
    app.run(debug = True)
