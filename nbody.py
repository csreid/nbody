import math
import time
import Tkinter
import random
from Tkinter import Tk, Canvas, PhotoImage, mainloop

WIDTH, HEIGHT = 1920, 1024

window = Tk()
canvas = Canvas(window, width = WIDTH, height = HEIGHT, bg="#ffffff")
canvas.pack()
img = PhotoImage(width = WIDTH, height = HEIGHT)
canvas.create_image((WIDTH/2,HEIGHT/2), image=img, state="normal")

G = 6.67
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

def paint_at((x, y), n):
    if n == 0 and x > 2 and y > 2:
        img.put("#ffffff", (x, y))
        img.put("#ffffff", (x+1, y))
        img.put("#ffffff", (x, y+1))
        img.put("#ffffff", (x-1, y))
        img.put("#ffffff", (x, y-1))
        img.put("#ffffff", (x+1, y+1))
        img.put("#ffffff", (x-1, y-1))
        img.put("#ffffff", (x+2, y+1))
        img.put("#ffffff", (x+1, y+2))
        img.put("#ffffff", (x-2, y-1))
        img.put("#ffffff", (x-1, y-1))
        img.put("#ffffff", (x-2, y-2))
    elif x > 2 and y > 2:
        img.put("#000000", (x, y))
        img.put("#000000", (x+1, y))
        img.put("#000000", (x, y+1))
        img.put("#000000", (x-1, y))
        img.put("#000000", (x, y-1))
        img.put("#000000", (x+1, y+1))
        img.put("#000000", (x-1, y-1))
        img.put("#000000", (x+2, y+1))
        img.put("#000000", (x+1, y+2))
        img.put("#000000", (x-2, y-1))
        img.put("#000000", (x-1, y-1))
        img.put("#000000", (x-2, y-2))
    
def task():
    while 1:
        for current in bodies:
            for each in bodies:
                if current != each:
                    if distance(current, each) < 2:
                        prevMass = current.mass
                        current.mass = current.mass + each.mass
                        current.velocity = ((current.velocity[0]*prevMass + each.velocity[0]*each.mass)/current.mass, (current.velocity[1]*prevMass + each.velocity[1]*each.mass)/current.mass)
                        bodies.remove(each)
                    else:
                        current.velocity = ((current.velocity[0] + gravityVector(current, each)[0]/current.mass), (current.velocity[1] + gravityVector(current, each)[1]/current.mass))
         
        for each in bodies:
            paint_at(roundTuple(each.position), 0)
        window.update()
        
        for each in bodies:
            each.position = ((each.position[0] + each.velocity[0]),(each.position[1] + each.velocity[1]))
        for each in bodies:
            paint_at(roundTuple(each.position), 1)
        window.update()
        time.sleep(0.01)



sun= Body((0, 0),(1000, 390), 400)
p1 = Body((0, 3),(700, 386), 4)
p2 = Body((0, 1.6), (685, 350), 2)
p3 = Body((0, 1.3), (600, 375), 3)
p4 = Body((0, 1), (500, 400), 8)

bodies.append(sun)
bodies.append(p1)
bodies.append(p2)
bodies.append(p3)
bodies.append(p4)

#for i in range(0, 100):
#    newBody = Body((0,0), (random.randint(0,1920), random.randint(0,768)), random.randint(1, 50))
#    bodies.append(newBody)

task()
