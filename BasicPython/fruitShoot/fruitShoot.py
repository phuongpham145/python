import pgzero
from pgzero.builtins import Actor
from random import randint
import  pgzrun
apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")
def draw():
    screen.clear()
    screen.fill("violet")
    apple.draw()
    orange.draw()
    pineapple.draw()
def place_apple():
    apple.x = randint(10, 300)
    apple.y = randint(10, 200)
def place_orange():
    orange.x = randint(100, 800)
    orange.y = randint(100, 300)
def place_pineapple():
    pineapple.x = randint(90, 600)
    pineapple.y = randint(90, 400)
place_apple()
def on_mouse_down(pos):
    if(apple.collidepoint(pos)):
        print("Good Shot")
        place_apple()
    else:
        print("Bad Shot")
    if pineapple.collidepoint(pos):
        place_pineapple()
    if orange.collidepoint(pos):
        place_orange()
pgzrun.go()