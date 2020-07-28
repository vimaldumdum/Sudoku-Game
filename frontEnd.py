from flask import Flask, render_template
from backEnd import solve, findMissing
import copy
from flask_sqlalchemy import SQLAlchemy
import dbInterface


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gridsDB.db'

db = SQLAlchemy(app)

class grids(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grid = db.Column(db.String(81), nullable=False)

    def __repr__(self):
        return 'grid no. ' + str(self.id)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/play-board')
def play():
    grid = dbInterface.getGrid()
    miss = list()
    sol = copy.deepcopy(grid)
   # print(grid)
    miss = findMissing(sol)
    #print(len(miss))
    missing = len(miss)
    # print(grid)
    solve(sol)

   # print(grid)
   # print(sol)
    return render_template('board.html', grids = grid, solved = sol, total = missing)

@app.route('/exit')
def exit():
    return render_template('exit.html')

if __name__ == "__main__":
    app.run(debug = True)
