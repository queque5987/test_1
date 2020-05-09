import pgzrun
import math

WIDTH = 700
HEIGHT = 620
white = (255, 255, 255)
red = (200, 35, 35)
yellow = (197, 186, 34)
bgcolor = (28, 28, 160)
stage = 0
_COL = 7
_ROW = 6
tilestatus = [
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]
]
endgame = False
text = ''

def drawCircle(x, y,color):
    screen.draw.filled_circle((x,y), 40, color)

def updatecircle():
    tileposx = 50
    tileposy = 50
    tilecolour = white
    for i in reversed(tilestatus):
        for j in i:
            if j == 1: tilecolour = yellow
            elif j == 2: tilecolour = red
            else: tilecolour = white    #init
            drawCircle(tileposx, tileposy, tilecolour)
            tileposx += 100
        tileposy += 100
        tileposx = 50

def tileflip(x):
    settile = 0
    global tilestatus
    global stage
    if (stage % 2) == 0:    #Yellow - 1
        settile = 1
        stage += 1
    else:   #Red - 2
        settile = 2
        stage += 1
    for findrow in range(0,_ROW):   #get Y axis -> set/return
        if tilestatus[findrow][x] == 0 or findrow == _ROW-1:
            tilestatus[findrow][x] = settile
            return findrow

def checkwinner(ro, co):
    winner = tilestatus[ro][co] #inherited player
    lcount = 0
    rcount = 0
    k = 0
    while ro >= 3 and ro - lcount >= 0: #downward check
        if tilestatus[ro-lcount][co] == winner:
            lcount += 1
            k += 1
            if k == 4: return winner
        else: break
    lcount = 0
    k = 0
    #up-right, down-leftward check
    while ro + rcount < _ROW and co + rcount < _COL: #up-rightward
        if tilestatus[ro+rcount][co+rcount] == winner:
            rcount += 1
            k += 1
            if k == 4: return winner
        else: break
    k -= 1  #duplicate self count--
    while ro - lcount >= 0 and co - lcount >= 0:  #down-leftward
        if tilestatus[ro-lcount][co-lcount] == winner:
            lcount += 1
            k += 1
            if k == 4: return winner
        else: break
    lcount = 0
    rcount = 0
    k = 0
    #horizontal check
    while co - lcount >= 0: #leftward check
        if tilestatus[ro][co-lcount] == winner:
            lcount += 1
            k += 1
            if k == 4: return winner
        else: break
    k -= 1 #duplicate self count--
    while co + rcount < _COL: #rightward check
        if tilestatus[ro][co + rcount] == winner:
            rcount += 1
            k += 1
            if k == 4: return winner
        else: break
    lcount = 0
    rcount = 0
    k = 0
    #up-left, down-rightward check
    while ro + lcount < _ROW and co - lcount >= 0: #up-leftward
        if tilestatus[ro+lcount][co-lcount] == winner:
            lcount += 1
            k += 1
            if k == 4: return winner
        else: break
    k -= 1 #duplicate self count--
    while ro - rcount >= 0 and co + rcount < _COL: #down-rightward check
        if tilestatus[ro-rcount][co+rcount] == winner:
            rcount += 1
            k += 1
            if k == 4: return winner
        else: break
    return 0    #no winner yet

def setText(who_won):
    global endgame
    global text
    if endgame:
        text = 'Game Finished -- Try new Game'
    elif who_won == 1 and endgame == False:
        text = 'Winner is Yellow'
        endgame = True
    elif who_won == 2 and endgame == False:
        text = 'Winner is Red'
        endgame = True


def draw():
    screen.fill(white)
    tilebgrct = Rect((0,0),(WIDTH,HEIGHT-20))
    screen.draw.filled_rect(tilebgrct,bgcolor)
    updatecircle()
    screen.draw.text(text, (0, 600), color=(0, 0, 0), background="white")

def update():
    pass

def on_mouse_down(pos):
    global endgame
    if endgame:
        setText(0)
    else:
        xpos = math.floor(pos[0]/100)
        to_check_ypos = tileflip(xpos)
        who_won = checkwinner(to_check_ypos,xpos)
        setText(who_won)

pgzrun.go()