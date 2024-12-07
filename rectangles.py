import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 800

def draw():
    r=255
    g=0
    b=randint(120,255)
    w=WIDTH-100
    h=HEIGHT-200
    for i in range(20):
        rect = Rect((0, 0), (w,h))
        rect.center=150,150
        screen.draw.rect(rect, (r,g,b))
        w=w+10
        h=h-10
        r=r-10
        g=g+10
pgzrun.go()
 