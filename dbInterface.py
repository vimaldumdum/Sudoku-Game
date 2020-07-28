import frontEnd
import random
from copy import deepcopy

def addGridToDB(grid):
    flat = list()
    res = ''
    for ele in grid:
        for e in ele:
            flat.append(str(e))

    res = res.join(flat)
    print(res)
    db.session.add(grids(grid=res))
    db.session.commit()

def displayDB():
    print(grids.query.all())


def getGrid():
    length = len(frontEnd.grids.query.all())
    randomNumer = random.randint(0, length-1)
    str = frontEnd.grids.query.all()[randomNumer].grid
    retGrid = list()
    temp = list()
    k = 0
    for i in range(9):
        for j in range(9):
            temp.append(int(str[k]))
            k = k+1
        addList = deepcopy(temp)
        retGrid.append(addList)
        temp.clear()
    return retGrid


