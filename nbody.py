import math
import time
import Tkinter
import random
import pygame
from Tkinter import Tk, Canvas, PhotoImage, mainloop

size = WIDTH, HEIGHT = 640, 480
black = 0,0,0
white = 255,255,255
#window = Tk()

pygame.init()
window = pygame.display.set_mode(size)
window.fill(white)

G = .667
timestep = 0
timestepsize = 1.0 #higher timesteps result in less accuracy but faster speeds. I think.
bodies = []

class Body:
    velocity = (0, 0)
    position = (0, 0)
    mass = 0
    def __init__(self, v, p, m):
        self.position = p
        self.velocity = v
        self.mass = m

def distance(a, b):
    x = a.position[0] - b.position[0]
    y = a.position[1] - b.position[1]
    return math.sqrt(x**2+y**2)

def gravityForce(a, b):
    rsquared = distance(a, b) ** 2
    return G * (a.mass*b.mass)/rsquared

def gravityVector(a, b):
    """computes the force of gravity exerted ON 'a' BY 'b'"""

    gravVector = (math.cos(angle(a,b))*gravityForce(a,b), math.sin(angle(a,b))*gravityForce(a,b))
    if a.position[0] > b.position[0]:
        gravVector = (-gravVector[0], -gravVector[1])
    return gravVector

def angle(a, b):
    if a.position[0] != b.position[0] and a.position[1] != b.position[1]:
        x = a.position[0] - b.position[0]
        y = a.position[1] - b.position[1]
        return math.atan(y/x)
    else:
        return 0

def roundTuple((x, y)):
    return ((int)(round(x)), (int)(round(y)))

    
def task():
    while 1:
        for current in bodies:
            for each in bodies:
                if current != each:
                    if distance(current, each) < 10:
                        prevMass = current.mass
                        current.mass = current.mass + each.mass
                        current.velocity = ((current.velocity[0]*prevMass + each.velocity[0]*each.mass)/current.mass, (current.velocity[1]*prevMass + each.velocity[1]*each.mass)/current.mass)
                        pygame.draw.circle(window, white, roundTuple(each.position), 2, 0)
                        bodies.remove(each)
                    else:
                        current.velocity = ((current.velocity[0] + gravityVector(current, each)[0]/current.mass), (current.velocity[1] + gravityVector(current, each)[1]/current.mass))
         
        for each in bodies:
            #paint_at(roundTuple(each.position), 0)
            pygame.draw.circle(window,white,roundTuple(each.position), 2, 0)
#        pygame.display.flip()
        
        for each in bodies:
            each.position = ((each.position[0] + each.velocity[0]),(each.position[1] + each.velocity[1]))
        for each in bodies:
            #paint_at(roundTuple(each.position), 1)
            pygame.draw.circle(window, black, roundTuple(each.position), 2, 0)
        pygame.display.flip()
        #time.sleep(0.01)



p3 = Body((0, 2.583), (612, 386), .001)
p4 = Body((0, 0), (512, 386), 100)
p7 = Body((0, 2.11), (662, 386), .001)
p5 = Body((0, 1.826), (712, 386), .001)
p6 = Body ((0,1.29), (912, 386), 1)
p8 = Body((0, 5.774946), (532, 386), .001)
bhole = Body((-10, 0), (5000, 586), 500);
#asteroid = Body((0, 3), (562, 386), .0000001);
moon1 = Body((0, 1.867494589), (932, 386), .00001)

#bodies.append(p3)
#bodies.append(p4)
#bodies.append(p5)
#bodies.append(p6)
#bodies.append(p7)
#bodies.append(p8)
#bodies.append(moon1)
#bodies.append(bhole)
#bodies.append(asteroid);

for i in range(0, 250):
    newBody = Body((0,0), (random.randint(0,640), random.randint(0,480)), random.randint(1, 10))
    bodies.append(newBody)

task()
