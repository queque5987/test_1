import pgzrun
import pygame
import math
import sys


def updatecircle():
    tileposx = 50
    tileposy = 50
    tilecolour = white
    for i in tilestatus:
        for j in reversed(i):
            if j == 1: tilecolour = yellow
            elif j == 2: tilecolour = red
            else: tilecolour = white
            drawcircle(tileposx, tileposy, tilecolour)
            tileposy += 100
        tileposx += 100
        tileposy = 50
def drawcircle(x_pos, y_pos, color):
    pygame.draw.circle(screen, color, (x_pos, y_pos), 40)
def tileflip(x):
    settile = 0
    global tilestatus
    if isplayer1turn():
        settile = 1
    else:
        settile = 2

    tileindex = 0
    for findzero in tilestatus[x]:
        if findzero == 0:
            tilestatus[x][tileindex] = settile
            return True
        tileindex += 1
    # list out of index
    isplayer1turn()
    return False
def isplayer1turn():
    global player1turn
    if player1turn:
        player1turn = False
        return True
    else:
        player1turn = True
        return False
def isfull():
    for i in tilestatus:
        for j in l:
            if j == 0:
                return False
    return True
def checkwinner():
    for l in tilestatus:
        tetris = 0
        for i in l:
            if i == 1:
                tetris += 1
                tetris = tetris % 10
            elif i == 2:
                tetris += 10
                tetris = tetris - tetris % 10
            else:   # i == 0
                tetris = 0
                break
            if tetris == 4:
                return "player 1"
            elif tetris == 40:
                return "player 2"
    if isfull():
        return "draw"

width = 700
height = 600

white = (255, 255, 255)
red = (200, 35, 35)
yellow = (197, 186, 34)
bgcolor = (28, 28, 160)

player1turn = True

pygame.init()
pygame.display.set_caption("Simple PyGame Example")
screen = pygame.display.set_mode((width, height))


clock = pygame.time.Clock()
tilestatus = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]
while True:
    
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            tileflip(math.floor(event.pos[0]/100))

    screen.fill(bgcolor)
    updatecircle()
    checkwinner()
    pygame.display.update()

pgzrun.go()