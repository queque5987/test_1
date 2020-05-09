import pgzrun
import math

width = 700
height = 620
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

def updatecircle():
    tileposx = 50
    tileposy = 50
    tilecolour = white
    for i in reversed(tilestatus):
        for j in i:
            if j == 1: tilecolour = yellow
            elif j == 2: tilecolour = red
            else: tilecolour = white    #init
            drawcircle(tileposx, tileposy, tilecolour)
            tileposx += 100
        tileposy += 100
        tileposx = 50
def drawcircle(x_pos, y_pos, color):
    screen.draw.circle(color, (x_pos, y_pos), 40)
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
def settext(check):
    global textsurface
    global endgame
    if check == 1 and endgame == False:
        textsurface = myfont.render('Winner is Yellow', False, (0, 0, 0))
        endgame = True
    elif check == 2 and endgame == False:
        textsurface = myfont.render('Winner is Red', False, (0, 0, 0))
        endgame = True
    elif endgame:
        textsurface = myfont.render('Game Finished -- Try new Game', False, (0, 0, 0))


def draw():
    # background set
    screen.fill(bgcolor)
    # tile set
    tileposx = 50
    tileposy = 50
    for i in reversed(tilestatus):
        for j in i:
            if j == 1: tilecolour = yellow
            elif j == 2: tilecolour = red
            else: tilecolour = white    # 0 == init
            screen.draw.circle((tileposx,tileposy),40,tilecolour)
            tileposx += 100
        tileposy += 100
        tileposx = 50    
    # text
    screen.draw.filled_rect(0,600,width,20,white)
    screen.draw.text("no",(5,600))
def update():
    pass

def on_mouse_down(pos):
    if endgame:
        settext(0)
    else:
        settext(checkwinner(tileflip(math.floor(event.pos[0]/100)),math.floor(event.pos[0]/100))

pgzrun.go()