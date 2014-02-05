import math
import time
import Tkinter
from Tkinter import Tk, Canvas, PhotoImage, mainloop

WIDTH, HEIGHT = 1024, 768

window = Tk()
canvas = Canvas(window, width = WIDTH, height = HEIGHT, bg="#ffffff")
canvas.pack()
img = PhotoImage(width = WIDTH, height = HEIGHT)
canvas.create_image((WIDTH/2,HEIGHT/2), image=img, state="normal")


G = 66.7
timestep = 0
timestepsize = 1.0 #higher timesteps result in less accuracy but faster speeds. I think.

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
    x = a.position[0] - b.position[0]
    y = a.position[1] - b.position[1]
    return math.atan(y/x)

def roundTuple((x, y)):
    return ((int)(round(x)), (int)(round(y)))

def paint_at((x, y), n):
    if n == 0 and x > 0 and y > 0:
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
        img.put("#ffffff", (x-1, y-2))
    elif x > 0 and y > 0:
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
        img.put("#000000", (x-1, y-2))
    
def task():
    while 1:
        paint_at(roundTuple(x.position), 0)
        paint_at(roundTuple(y.position), 0)
        window.update()

        x.velocity = ((x.velocity[0] + gravityVector(x, y)[0]/x.mass), (x.velocity[1] + gravityVector(x, y)[1]/x.mass));
        y.velocity = ((y.velocity[0] + gravityVector(y, x)[0]/y.mass), (y.velocity[1] + gravityVector(y, x)[1]/y.mass));
        
        x.position = ((x.position[0] + x.velocity[0]),(x.position[1] + x.velocity[1]))
        y.position = ((y.position[0] + y.velocity[0]),(y.position[1] + y.velocity[1]))
 
        paint_at(roundTuple(x.position), 1)
        paint_at(roundTuple(y.position), 1)
        window.update()
        print x.velocity
        time.sleep(0.01)



x = Body((0, 5),(800, 386), 1)
y = Body((0, -.01),(512, 386), 200)

task()
