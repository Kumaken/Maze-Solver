#HEAP IMPORT:
from heapq import heappush, heappop, heapify
import copy
import colorama
from colorama import init
from colorama import Fore, Back, Style
from os import system, name
from time import sleep

def clear():
    if(name == 'nt'):
        _ = system('cls')
    else:
        _ = system('clear')

def printMaze(maze):
    # clear()
    for i in range(len(maze[0])+2):
        print(Back.CYAN, end = ' ')

    print()

    for i in range(len(maze)):
        print(Back.CYAN, end = ' ')
        for j in range(len(maze[i])):
            if(maze[i][j] == 1):
                print(Back.BLACK, end = ' ')
            elif(maze[i][j] == 2):
                print(Back.RED, end = ' ')
            elif(maze[i][j] == 3):
                print(Back.BLUE, end = ' ')
            elif(maze[i][j] == 4):
                print(Back.GREEN, end = ' ')
            elif(maze[i][j] == 5):
                print(Back.MAGENTA, end = ' ')
            else:
                print(Back.WHITE, end = ' ')
        print(Back.CYAN, end = ' ')
        print()

    for i in range(len(maze[0])+2):
        print(Back.CYAN, end = ' ')

    print(Style.RESET_ALL)

#Get Start Pos:
def searchColumnForX(colPos, X):
    for x in enumerate([row[colPos] for row in mazeMap]):
        #x becomes tuple of (index, element)
        if x[1] == X:
            return x[0]

class Tile(object):
    """ In cases where in heapqueue, priority is the same and it needs to
        compare Tile object too, just sort according to insertion order """
    def __lt__(self, other):
        return self

    # Constructor:
    def __init__(self, _rowPos, _colPos, _parent, _cost):
        self.rowPos = _rowPos
        self.colPos = _colPos
        self.parent = _parent
        self.g = 0
        self.h = 0
        self.cost = _cost

    # Check if currentTile is already at the goal:
    def isGoal(self):
        global goalTile
        return (self.rowPos == goalTile.rowPos and self.colPos == goalTile.colPos)

    # Compute heuristic via manhattan distance:
    def computeHeuristic(self):
        global goalTile
        return (abs(self.rowPos - goalTile.rowPos ) + abs(self.colPos - goalTile.colPos))

    # Updates adjacent tiles and set their costs accordingly
    def modifyTile(self, targetTile):
        self.g = targetTile.g+1
        #poi:
        self.parent = targetTile
        self.h = targetTile.computeHeuristic()
        self.cost = int(self.h + self.g)

    # When goal is found, generate path back to the start point
    def generatePath(self):
        global startTile
        path = [(self.rowPos, self.colPos)]
        currentTile = self
        while currentTile.parent is not startTile:
            currentTile = currentTile.parent
            path.append((currentTile.rowPos, currentTile.colPos))
        # currentTile is at startTile:
        path.append((startTile.rowPos, startTile.colPos))
        # path is in reverse manner, need to reverse it
        path.reverse()
        return path

    def getNeighboringTiles(self):
        neighbors = []
        #north:
        if isValidTile(self.rowPos-1, self.colPos):
            neighbors.append(makeTile(self.rowPos-1, self.colPos))
            mazeMap[self.rowPos-1][self.colPos] = 2
        #east:
        if isValidTile(self.rowPos, self.colPos+1):
            neighbors.append(makeTile(self.rowPos, self.colPos+1))
            mazeMap[self.rowPos][self.colPos+1] = 2
        #south:
        if isValidTile(self.rowPos+1, self.colPos):
            neighbors.append(makeTile(self.rowPos+1, self.colPos))
            mazeMap[self.rowPos+1][self.colPos] = 2
        #west:
        if isValidTile(self.rowPos, self.colPos-1):
            neighbors.append(makeTile(self.rowPos, self.colPos-1))
            mazeMap[self.rowPos][self.colPos-1] = 2

        return neighbors

#construct a blank-slate Tile:
def makeTile(rowPos, colPos):
    newTile = Tile(rowPos, colPos, None, 0)
    return newTile

#check if a tile is valid for passing:
def isValidTile(rowPos, colPos):
    return (rowPos >= 0 and colPos >= 0 and rowPos < mazeMaxRow and colPos < mazeMaxCol and mazeMap[rowPos][colPos] == 0)


# MAIN A-STAR ALGORITHM
def a_Star_Algorithm():
    """
        Implements Heap Queue which is basically a faster priority queue with less locking overhead
        BUT BEWARE : NOT THREADING-SAFE, but not like we needed it here anyway lol
    """
    #Heap of tiles containing candidates for the final path
    """
        All tiles contained inside the heap are sorted by its cost:
        f(n) = g(n) + h(n).
        If by some chance priority is the same, sort by insertion order.
        Heap queue is a binary heap -> ALL operations on heap queue is
        O(log n)
        WHICH IS FAST!!!
    """
    liveTiles = []
    heapify(liveTiles)
    # Set of traversed tiles:
    traversed = set()
    #load Global variables:
    global startTile
    #push starting point:
    heappush(liveTiles, (startTile.cost,startTile))
    while len(liveTiles):
        # printMaze(mazeMap)
        # pop current Tile from heap q:
        currentCost, currentTile = heappop(liveTiles)
        # add to traversed set:
        traversed.add((currentTile.rowPos, currentTile.colPos))

        # check if goal is found:
        if currentTile.isGoal():
            return currentTile.generatePath()

        # check neighbor tiles:
        neighbors = currentTile.getNeighboringTiles()
        # iterate over neighbors:
        for tile in neighbors:
            # If that neighbor tile has not yet been traversed:
            if (tile.rowPos, tile.colPos) not in traversed:
                """
                    BUT! If that tile is already in expanded liveTiles, then check
                    whether the cost to that tile is more optimal or not.
                    If so, then we have to update it!
                """
                if (tile.cost, tile) in liveTiles:
                    if tile.g > currentTile.g + 1:
                        tile.modifyTile(currentTile)
                else:
                    tile.modifyTile(currentTile)
                    # add neighbor to liveTiles list:
                    heappush(liveTiles, (tile.cost, tile) )

def BFS(x, y, dest, maze):
    q = []
    visited = []
    q.append((x,y))
    visited.append(((-1,-1),(x,y)))
    before = (x,y)
    maze[x][y] = 2
    while(q):
        # print("curr idx: ", end = ' ')
        # print((x,y))
        # printMaze(maze)
        if((x,y) == dest):
            break
        next = []
        if(x+1 < mazeMaxRow):
            if(maze[x+1][y] == 0):
                if not (x+1,y) in visited and (x+1,y) != before:
                    next.append((x+1,y))

        if(x-1 >= 0):
            if(maze[x-1][y] == 0):
                if not (x-1,y) in visited and (x-1,y) != before:
                    next.append((x-1,y))

        if(y+1 < mazeMaxCol):
            if(maze[x][y+1] == 0):
                if not (x,y+1) in visited and (x,y+1) != before:
                    next.append((x,y+1))

        if(y-1 >= 0):
            if(maze[x][y-1] == 0):
                if not (x,y-1) in visited and (x,y-1) != before:
                    next.append((x,y-1))

        q.pop(0)

        for i in next:
            if((visited[len(visited)-1][0], i) not in visited):
                # print("di append: ", end = ' ')
                # print(i)
                q.append(i)
                visited.append(((x,y),i))
                before = i
                maze[i[0]][i[1]] = 2
        # print(q)
        # print(visited)

        if(q):
            x = q[0][0]
            y = q[0][1]


    idx = ((0,0),(0,0))

    for i in reversed(visited):
        if(i[1] == dest):
            idx = i
            break;

    mark = visited[visited.index(idx)][0]
    maze[visited[visited.index(idx)][1][0]][visited[visited.index(idx)][1][1]] = 4
    on_intersect = False
    search = (-2,-2)
    for i in reversed(visited):
        if(i[1] == mark and not on_intersect):
            maze[i[1][0]][i[1][1]] = 4
            mark = i[0]

#External File Management:
filename = input("Input maze file: ")
print()
f= open(filename,"r")
mazeMap = [ [int(x) for x in list(line) if x != '\n'] for line in f]
mazeMaxRow = len(mazeMap)
mazeMaxCol = len(mazeMap[0])
startPos = (searchColumnForX(0,0), 0)
goalPos = (searchColumnForX(mazeMaxCol-1,0), mazeMaxCol-1)
startTile = makeTile(startPos[0],startPos[1])
goalTile = makeTile(goalPos[0],goalPos[1])

def main():
    init()

    x = startPos[0]
    y = startPos[1]

    mazeMap[x][y] = 3
    mazeMap[goalPos[0]][goalPos[1]] = 5

    print("Maze Input: ")
    printMaze(mazeMap)
    print()

    #BFS
    print("Traversing Maze...")
    print()

    mazeMap[x][y] = 0
    mazeMap[goalPos[0]][goalPos[1]] = 0

    maze_bfs = copy.deepcopy(mazeMap)
    BFS(x, y, goalPos, maze_bfs)

    print("RESULT(Green for traversed route, Red for final route): ")
    print()

    maze_bfs[x][y] = 3
    maze_bfs[goalPos[0]][goalPos[1]] = 5

    print("Result with BFS: ")
    printMaze(maze_bfs)
    print()

    mazeMap[x][y] = 0
    mazeMap[goalPos[0]][goalPos[1]] = 0

    #A star:
    print("Result with A*: ")
    result = a_Star_Algorithm()
    for i in result:
        mazeMap[i[0]][i[1]] = 4

    mazeMap[x][y] = 3
    mazeMap[goalPos[0]][goalPos[1]] = 5

    printMaze(mazeMap)

# main()

if __name__ == "__main__":
    main()