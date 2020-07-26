from flask import Flask, render_template
from backEnd import getGrids, solve, isSafe, getGrid
import copy


app = Flask(__name__)

sol = getGrid()
grid = copy.deepcopy(sol)
#print(grid)
solve(sol)


#print(grid)
#print(sol)

@app.route('/')
def hello():
    return render_template('board.html', grids = grid, solved = sol)

@app.route('/home/<int:name>')
def hel(name):
    if name == 1:
        return "hello, vimal"
    else:
        return "hello"

if __name__ == "__main__":
    app.run(debug = True)
