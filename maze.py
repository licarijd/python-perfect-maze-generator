from random import *
from graphics import *

win = GraphWin('PERFECT MAZE', 700, 700)

class Maze:

    #Constructor takes parameter N to create an N by N maze
    def __init__(self, N):

        self.visitedPoints = []
        self.path = []
        self.x = True
        self.n = N

        #Becomes True when the endpoint is reached in the maze.
        self.exitFound = False
        self.endrow = randrange(((-1)*self.n) +2, 1, 1)
        self.endcol = randrange(1,self.n, 1)
        if not (self.endrow==1 and self.endcol==1):
            print(self.endcol, self.endrow)
            #break

            self.movex = self.endcol -1
            self.movey = self.endrow -1

        #drawing final point

        
        pt = Point(self.movex*self.numLines+15,(0 -(self.movey*self.numLines))+15)
        pt.draw(win)
        rect = Rectangle(Point((self.movex+1)*self.numLines-15, (self.numLines-(self.movey*self.numLines))-15), pt)
        rect.setFill("red")        
        rect.draw(win)
        
        self.movex = 0
        self.movey = 0      

        #The perfect maze is generated.
        self.explore()

    #Basic stack operations such as pop and push are defined by the functions below.

    def push(self, item):
        if self.exitFound == False:
            self.path.append(item)
        else:
            return

            def pop(self):
                if self.exitFound == False:
                    self.path.pop()
                else:
                    return

                    def stackSize(self):
                        return len(self.path)        

    #Functions dealing with the list of visited points are below (only operations are adding to the array or checking array size.    
    def add(self, item):
        self.visitedPoints.append(item)

        def listSize(self):
            return len(self.visitedPoints)    

    #explore function is responsible for generating a perfect maze.
    def explore(self):        

        totalCells = self.n*self.n
        visitedCells = 1

        #The start point is pushed onto the visitedPoints stack.
        initialPoint = [1,1]
        self.add(initialPoint)
        
        """ North = 1
            South = 2
            West = 3
            East = 4"""

        #cntr2 represents backtracked moves.
        cntr2=0

        #cntr represents impossible moves.
        cntr = 0

        #All cells need to be accessible in a perfect maze.        
        while visitedCells < totalCells:

            cntr = 0       

            #Depth-First search chooses a direction at random.        
            num = randint(1, 4)

            #Moving beyond the maze's edges are impossible moves.
            if self.movex == 0:
                cntr = cntr + 1
                print("on edge")

                if self.movex == self.n-1:
                    cntr = cntr + 1
                    print("on edge")

                    if self.movey == 0:
                        cntr = cntr + 1
                        print("on edge")

                        if self.movey == (-1*self.n)+1:
                            cntr = cntr + 1
                            print("on edge")

            #Checks if there are no possible moves from the current position
            for i in range(len(self.visitedPoints)):

                if self.visitedPoints[i]== [self.curcol, self.currow + 1] or self.visitedPoints[i]== [self.curcol, self.currow - 1] or self.visitedPoints[i]== [self.curcol - 1, self.currow] or self.visitedPoints[i]== [self.curcol + 1, self.currow]:

                    cntr = cntr + 1
                    print("neighboir cell taken")

                    if cntr >= 4:
                        print("No possible moves")
                        
                        if self.stackSize() >= 1:
                            self.pop()
                            
                            cntr2 = cntr2 + 1
                            previous = self.visitedPoints[len(self.visitedPoints)-cntr2]
                            self.curcol = previous[0]
                            self.currow = previous[1]
                            self.movex = previous[0]-1
                            self.movey = previous[1]-1                            
                            cntr=0
                            cntr = 0
                            
            #If a North move is within the maze, continue.                
            if (num == 1) and (self.movey < 0):

                self.x = True

                #Checks if the point being checked has already been visited.
                for i in range(0, self.listSize()):
                    if self.visitedPoints[i]== [self.curcol, self.currow + 1]:
                        self.x = False
                        break
                        
                #If the space is free, the wall is broken down.    
                if self.x == True:

                    self.currow = self.currow + 1
                    newPoint = [self.curcol, self.currow]
                    self.add(newPoint)
                    self.push(newPoint)

                    #Exit found.
                    if newPoint == [self.endcol, self.endrow]:
                        self.exitFound = True
                        

                        self.movey = self.movey + 1
                        visitedCells = visitedCells + 1

                        pt = Point(self.movex*self.numLines, self.numLines-(self.movey*self.numLines))
                        pt.draw(win)
                        rect = Rectangle(Point((self.movex+1)*self.numLines, self.numLines-(self.movey*self.numLines)), pt)
                        rect.setFill("black")        
                        rect.draw(win)

                        cntr2=0
            #The same is done for South, West, and East.

            elif num == 2 and (self.movey > (-1*self.n)+1):

                self.x = True

                for i in range(0, self.listSize()):
                    if self.visitedPoints[i]== [self.curcol, self.currow - 1]:
                        self.x = False
                        break                        
                        
                        if self.x == True:

                            self.currow = self.currow - 1                    
                            newPoint = [self.curcol, self.currow]
                            self.add(newPoint)
                            self.push(newPoint)

                        #Exit found.
                        if newPoint == [self.endcol, self.endrow]:
                            self.exitFound = True

                            self.movey = self.movey - 1
                            visitedCells = visitedCells + 1

                            pt = Point(self.movex*self.numLines,0 -(self.movey*self.numLines))
                            pt.draw(win)
                            rect = Rectangle(Point((self.movex+1)*self.numLines, 0 -(self.movey*self.numLines)), pt)
                            rect.setFill("black")        
                            rect.draw(win)

                            cntr2=0                    

                        elif num == 3 and (self.movex > 0):

                            self.x = True

                            for i in range(0, self.listSize()):
                                if self.visitedPoints[i]== [self.curcol - 1, self.currow]:
                                    self.x = False
                                    break                        

                                    if self.x == True:

                                        self.curcol = self.curcol - 1
                                        newPoint = [self.curcol, self.currow]
                                        self.add(newPoint)
                                        self.push(newPoint)

                        #Exit found.
                        if newPoint == [self.endcol, self.endrow]:
                            self.exitFound = True

                            self.movex = self.movex - 1
                            visitedCells = visitedCells + 1

                            pt = Point((self.movex+1)*self.numLines,0 -(self.movey*self.numLines))
                            pt.draw(win)
                            rect = Rectangle(Point((self.movex+1)*self.numLines, self.numLines-(self.movey*self.numLines)), pt)
                            rect.setFill("black")        
                            rect.draw(win)

                            cntr2=0

                        elif num ==4 and (self.movex < self.n-1):

                            self.x = True

                            for i in range(0,self.listSize()):
                                if self.visitedPoints[i]== [self.curcol + 1, self.currow]:
                                    self.x = False
                                    break                        

                                    if self.x == True:

                                        self.curcol = self.curcol + 1
                                        newPoint = [self.curcol, self.currow]
                                        self.add(newPoint)
                                        self.push(newPoint)

                        #Exit found.
                        if newPoint == [self.endcol, self.endrow]:
                            self.exitFound = True

                            self.movex = self.movex + 1
                            visitedCells = visitedCells + 1

                            pt = Point(self.movex*self.numLines,0 -(self.movey*self.numLines))
                            pt.draw(win)
                            rect = Rectangle(Point(self.movex*self.numLines, self.numLines-(self.movey*self.numLines)), pt)
                            rect.setFill("black")        
                            rect.draw(win)

                            cntr2=0


                            self.x = True

            #These just keep track of current position, not necessary.
            print (cntr)
            print(self.curcol,self.currow, "          ", self.movex, self.movey)

        #Colours path, outputs correct sequence.   
        for i in range(0, self.stackSize()-1):
            print(self.path[i])

            current = self.path[i]

            self.movex = current[0] -1
            self.movey = current[1] -1

            pt = Point(self.movex*self.numLines+15,(0 -(self.movey*self.numLines))+15)
            pt.draw(win)
            rect = Rectangle(Point((self.movex+1)*self.numLines-15, (self.numLines-(self.movey*self.numLines))-15), pt)
            rect.setFill("green")        
            rect.draw(win)

        #Generates a key

        randomLocation = randrange(1, self.stackSize()-1)

        current = self.path[randomLocation]

        self.movex = current[0] -1
        self.movey = current[1] -1

        pt = Point(self.movex*self.numLines+15,(0 -(self.movey*self.numLines))+15)
        pt.draw(win)
        rect = Rectangle(Point((self.movex+1)*self.numLines-15, (self.numLines-(self.movey*self.numLines))-15), pt)
        rect.setFill("yellow")        
        rect.draw(win)

        #Not necessary.
        print(self.endcol, self.endrow)
