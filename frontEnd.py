from flask import Flask, render_template
from backEnd import solve, getGrid, findMissing
import copy


app = Flask(__name__)

sol = getGrid()
grid = copy.deepcopy(sol)
miss = findMissing(grid)
missing = len(miss)
#print(grid)
solve(sol)


#print(grid)
print(sol)

@app.route('/')
def hello():
    return render_template('board.html', grids = grid, solved = sol, total = missing)

@app.route('/home/<int:name>')
def hel(name):
    if name == 1:
        return "hello, vimal"
    else:
        return "hello"

if __name__ == "__main__":
    app.run(debug = True)
