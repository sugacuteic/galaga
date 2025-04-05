import pgzrun, random
HEIGHT = 600
WIDTH = 1200
TITLE = "galaga"
ship = Actor("galaga.png")
ship.pos = WIDTH /2, HEIGHT - 50
bug = Actor("bug.png")
bug.pos = WIDTH / 2, 50

bullets = []
enemies = []
score = 0

def draw():
    screen.blit("space.png", (0,0))
    ship.draw()
    bug.draw()
    
    
def update():
    global score
    if keyboard.left:
        ship.x-=5
        if ship.x < 0:
            ship.x = 50
    if keyboard.right:
        ship.x+=5
        if ship.x > WIDTH:
            ship.x = WIDTH - 50
    bug.y += 5
    if bug.y > HEIGHT:
        bug.y = -50
        bug.x = random.randint(50, WIDTH - 50)
        




pgzrun.go()