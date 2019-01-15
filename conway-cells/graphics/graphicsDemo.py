'''Test animation and depth.
'''

from graphics import *
import time

cells = []
win = GraphWin('conway-cells', 800, 600)

class Cell:
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

    def render(self):
        circleRender = Circle(Point(self.x, self.y), self.radius)
        circleRender.setFill(color_rgb(self.color.r, self.color.g, self.color.b))
        circleRender.draw(win)

    def update_(self):
        

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

for i in range(10):
    cells.append(Cell(i*10,300,Color(255,0,0),20))

clearRect = Rectangle(Point(0,0), Point(800, 600))
clearRect.setFill(color_rgb(0,0,0))
clearRect.draw(win)

# update_():

def render():

    for i in range(len(cells)):
        cells[i].render()

def update_():
    for i in range(len(cells)):
        cells[i].update_()


while True:
    update_()
    render()
    time.sleep(0.01)