"""
 Bounces a rectangle around the screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/-GmKoaX2iMs
"""
 
import pygame
from random import uniform
from math import sqrt
from math import atan2
from math import cos
from math import sin

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,255,150)

k = 1
 
pygame.init()
 
# Set the height and width of the screen
size = [1500, 1000]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("conway-cells")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

cellTypes = []

cells = []

class CellType:
    def __init__(self, color):
        self.color = color

cellTypes.append(CellType((200,5,135)))
cellTypes.append(CellType((0,255,120)))
cellTypes.append(CellType((20,200,205)))


class Cell:
    def __init__(self):
        self.x = uniform(0,1) * (size[0] - 50) + 25
        self.y = uniform(0,1) * (size[1] - 50) + 25
        self.vX = 0#uniform(0,1) * 5 - 2.5
        self.vY = 0#uniform(0,1) * 5 - 2.5
        self.radius = 10
        self.cellType = cellTypes[round(uniform(0,1) * (len(cellTypes) - 1))]
        self.cellID = uniform(0,10)

    def update_(self):
        self.x += self.vX
        self.y += self.vY

        if(self.x + self.radius >= size[0] or self.x - self.radius <= 0):
            self.vX *= -1

        if(self.y + self.radius >= size[1] or self.y - self.radius <= 0):
            self.vY *= -1

        fx = 0
        fy = 0
        for cell in cells:
            if(cell.cellID != self.cellID):
                distX = abs(cell.x - self.x)
                distY = abs(cell.y - self.y)

                forceAbs = k/(distX**2 + distY**2)

                angle = atan2(distY, distX)

                fx += cos(angle) * forceAbs
                fy += sin(angle) * forceAbs
        self.vX += fx
        self.vY += fy

    def render(self, screen):
        pygame.draw.circle(screen, self.cellType.color, (round(self.x), round(self.y)), self.radius)

        
for i in range(100):
    cells.append(Cell())


def update_():
    for cell in cells:
        cell.update_()

def render():
    screen.fill(BLACK)

    for cell in cells:
        cell.render(screen)

    pygame.display.flip() # update display with what has been drawn


# -------- Main Program Loop -----------
while not done:

    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    update_()
    render()
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    
 
# Close everything down
pygame.quit()