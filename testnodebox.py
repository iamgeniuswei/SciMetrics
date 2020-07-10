from nodebox.graphics import *
from nodebox.graphics.physics import Flock

flock = Flock(40, 0, 0, 500, 500)
flock.sight = 300


def draw(canvas):
    canvas.clear()
    translate(250,250)
    rotate(canvas.frame)
    rect(x=-50,y=-50,width=100,height=200)


canvas.fps = 30
canvas.size = 600, 400
canvas.run(draw)