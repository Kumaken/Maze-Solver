#MAZE TRAVERSAL PROGRAM BY
#Nixon Andhika - 13517059
#Abel Stanley - 13517068
#
#Traverse Maze using BFS and A* algorithm
#External library: Colorama
#Python Version Used: 3.7.0

#HEAP IMPORT:
from heapq import heappush, heappop, heapify
import copy
import colorama
from colorama import init
from colorama import Fore, Back, Style
from os import system, name
from time import sleep

#Method for clear screen
def clear():
    if(name == 'nt'): #Clear Windows shell screen
        _ = system('cls')
    else: #Clear Linux shell screen
        _ = system('clear')

#Method for printing the maze
def printMaze(maze):
<<<<<<< HEAD
    # clear()
=======

    #Print upper border
>>>>>>> 9b2eee7006d4af3330b4c5ad2c6e0a89c56f838a
    for i in range(len(maze[0])+2):
        print(Back.CYAN, end = ' ')

    print()

    #Print color for every row
    for i in range(len(maze)):

        #Print left border
        print(Back.CYAN, end = ' ')

        #Print color for every column
        for j in range(len(maze[i])):
            #Code 1 for wall
            if(maze[i][j] == 1):
                print(Back.BLACK, end = ' ')
            #Code 2 for traversed route
            elif(maze[i][j] == 2):
                print(Back.RED, end = ' ')
            #Code 3 for start tile
            elif(maze[i][j] == 3):
                print(Back.BLUE, end = ' ')
<<<<<<< HEAD
            elif(maze[i][j] == 4):
                print(Back.GREEN, end = ' ')
            elif(maze[i][j] == 5):
                print(Back.MAGENTA, end = ' ')
=======
            #Code 4 for final route
            elif(maze[i][j] == 4):
                print(Back.GREEN, end = ' ')
            #Code 5 for goal tile
            elif(maze[i][j] == 5):
                print(Back.MAGENTA, end = ' ')
            #Color for available tile to traverse
>>>>>>> 9b2eee7006d4af3330b4c5ad2c6e0a89c56f838a
            else:
                print(Back.WHITE, end = ' ')

        #Print right border
        print(Back.CYAN, end = ' ')
        print()

    #Print lower border
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
        if(targetTile.parent == None):
            self.h = targetTile.computeHeuristic()
        else:
            self.h = targetTile.computeHeuristic()+targetTile.parent.computeHeuristic()
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
<<<<<<< HEAD
        # printMaze(mazeMap)
=======
>>>>>>> 9b2eee7006d4af3330b4c5ad2c6e0a89c56f838a
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
    #Initialize empty queue
    q = []
    #Initialize visited list
    visited = []
    #Add current tile to queue and visited
    q.append((x,y))
    visited.append(((-1,-1),(x,y))) #tuple of tuples (first tuple is parent tile and second tuple is current tile)
    #Make the current tile value to 2 for traversed route
    maze[x][y] = 2
    #While queue not empty
    while(q):
        #If current tile is equal to goal tile, BFS is done
        if((x,y) == dest):
            break
        #Initialize list to store neighbors tile
        next = []
        #If there's a route below the current tile
        if(x+1 < mazeMaxRow):
            if(maze[x+1][y] == 0):
                if not (x+1,y) in visited:
                    next.append((x+1,y))
        #If there's a route above the current tile
        if(x-1 >= 0):
            if(maze[x-1][y] == 0):
                if not (x-1,y) in visited:
                    next.append((x-1,y))
        #If there's a route on the right of current tile
        if(y+1 < mazeMaxCol):
            if(maze[x][y+1] == 0):
                if not (x,y+1) in visited:
                    next.append((x,y+1))
        #If there's a route on the left of current tile
        if(y-1 >= 0):
            if(maze[x][y-1] == 0):
                if not (x,y-1) in visited:
                    next.append((x,y-1))
        #Remove first element of queue
        q.pop(0)
        #For every neighbors of current tile, add to queue and visited, and give code 2
        for i in next:
            if((visited[len(visited)-1][0], i) not in visited):
                q.append(i)
                visited.append(((x,y),i))
                maze[i[0]][i[1]] = 2

        #change current node to the first element in queue
        if(q):
            x = q[0][0]
            y = q[0][1]

    #After BFS traverse until goal tile is found, backtrack from goal tile to start tile
    idx = ((0,0),(0,0))

    #Search for index position in visited list where goal tile is found
    for i in reversed(visited):
        if(i[1] == dest):
            idx = i
            break

    #store parent tile of goal tile
    mark = visited[visited.index(idx)][0]
    #give goal tile Green color
    maze[visited[visited.index(idx)][1][0]][visited[visited.index(idx)][1][1]] = 4
    #loop from goal tile to start tile
    for i in reversed(visited):
        if(i[1] == mark):
            maze[i[1][0]][i[1][1]] = 4
            mark = i[0]

clear()
print(" .----------------.  .----------------.  .----------------.  .----------------. ")
print("| .--------------. || .--------------. || .--------------. || .--------------. |")
print("| | ____    ____ | || |      __      | || |   ________   | || |  _________   | |")
print("| ||_   \\  /   _|| || |     /  \\     | || |  |  __   _|  | || | |_   ___  |  | |")
print("| |  |   \\/   |  | || |    / /\\ \\    | || |  |_/  / /    | || |   | |_  \\_|  | |")
print("| |  | |\\  /| |  | || |   / ____ \\   | || |     .'.' _   | || |   |  _|  _   | |")
print("| | _| |_\\/_| |_ | || | _/ /    \\ \\_ | || |   _/ /__/ |  | || |  _| |___/ |  | |")
print("| ||_____||_____|| || ||____|  |____|| || |  |________|  | || | |_________|  | |")
print("| |              | || |              | || |              | || |              | |")
print("| '--------------' || '--------------' || '--------------' || '--------------' |")
print(" '----------------'  '----------------'  '----------------'  '----------------' ")
print("BY ABEL STANLEY & NIXON ANDHIKA")
print()

#External File Management:
filename = input("Input maze file: ")
print()
#read maze file
f= open(filename,"r")
#map for the maze
mazeMap = [ [int(x) for x in list(line) if x != '\n'] for line in f]
#total row of maze
mazeMaxRow = len(mazeMap)
<<<<<<< HEAD
mazeMaxCol = len(mazeMap[0])
startPos = (searchColumnForX(0,0), 0)
goalPos = (searchColumnForX(mazeMaxCol-1,0), mazeMaxCol-1)
=======
#total column of maze
mazeMaxCol = len(mazeMap[0])
#start index
startPos = (searchColumnForX(0,0), 0)
#goal index
goalPos = (searchColumnForX(mazeMaxCol-1,0), mazeMaxCol-1)
#start tile
>>>>>>> 9b2eee7006d4af3330b4c5ad2c6e0a89c56f838a
startTile = makeTile(startPos[0],startPos[1])
#goal tile
goalTile = makeTile(goalPos[0],goalPos[1])

def main():
    #Initialize colorama
    init()

<<<<<<< HEAD
    x = startPos[0]
    y = startPos[1]

    mazeMap[x][y] = 3
    mazeMap[goalPos[0]][goalPos[1]] = 5

=======
    #x is start row index
    x = startPos[0]
    #y is start col index
    y = startPos[1]

    #give different color for start and goal tile
    mazeMap[x][y] = 3
    mazeMap[goalPos[0]][goalPos[1]] = 5

    #print input maze
>>>>>>> 9b2eee7006d4af3330b4c5ad2c6e0a89c56f838a
    print("Maze Input: ")
    printMaze(mazeMap)
    print()

    #BFS
    print("Traversing Maze...")
    print()

<<<<<<< HEAD
    mazeMap[x][y] = 0
    mazeMap[goalPos[0]][goalPos[1]] = 0

=======
    #reset start tile and goal tile into available tile
    mazeMap[x][y] = 0
    mazeMap[goalPos[0]][goalPos[1]] = 0

    #copy the maze map and do BFS
>>>>>>> 9b2eee7006d4af3330b4c5ad2c6e0a89c56f838a
    maze_bfs = copy.deepcopy(mazeMap)
    BFS(x, y, goalPos, maze_bfs)

    print("RESULT(RED for traversed route, GREEN for final route): ")
    print()

<<<<<<< HEAD
    maze_bfs[x][y] = 3
    maze_bfs[goalPos[0]][goalPos[1]] = 5

=======
    #give different color for start and goal tile
    maze_bfs[x][y] = 3
    maze_bfs[goalPos[0]][goalPos[1]] = 5

    #print maze result with BFS
>>>>>>> 9b2eee7006d4af3330b4c5ad2c6e0a89c56f838a
    print("Result with BFS: ")
    printMaze(maze_bfs)
    print()

<<<<<<< HEAD
=======
    #reset start tile and goal tile into available tile
>>>>>>> 9b2eee7006d4af3330b4c5ad2c6e0a89c56f838a
    mazeMap[x][y] = 0
    mazeMap[goalPos[0]][goalPos[1]] = 0

    #A star:
    print("Result with A*: ")
    #Store the path from start tile to goal tile
    result = a_Star_Algorithm()
    #Color the final path with Green
    for i in result:
        mazeMap[i[0]][i[1]] = 4
<<<<<<< HEAD

    mazeMap[x][y] = 3
    mazeMap[goalPos[0]][goalPos[1]] = 5

    printMaze(mazeMap)
=======
>>>>>>> 9b2eee7006d4af3330b4c5ad2c6e0a89c56f838a

    #give different color for start and goal tile
    mazeMap[x][y] = 3
    mazeMap[goalPos[0]][goalPos[1]] = 5

    #print maze result with A*
    printMaze(mazeMap)

if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> 9b2eee7006d4af3330b4c5ad2c6e0a89c56f838a
