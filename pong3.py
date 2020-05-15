import pgzrun

WIDTH = 800
HEIGHT = 600

Paddle_WIDTH = 15
Paddle_HEIGHT = 80

WHITE = (255,255,255)

class Paddle(Rect):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y, Paddle_WIDTH, Paddle_HEIGHT)
        self.moveSpeed = 5
        self.center_pos = start_y

    def up(self):
        if self.y - self.moveSpeed > 0:
            self.y -= self.moveSpeed

    def down(self):
        if self.y + self.moveSpeed < HEIGHT - Paddle_HEIGHT:
            self.y += self.moveSpeed

    def isPonged(self, y_pos):
        if self.y <= y_pos <= self.y + Paddle_HEIGHT:
            return True
        else: return False

    def movingTo(self, pos):    #move to designated position
        if self.y > pos[1] - Paddle_HEIGHT/2:
            self.up()
        elif self.y < pos[1] - Paddle_HEIGHT/2:
            self.down()

    def draw(self):
        screen.draw.filled_rect(self, WHITE)

class Ball():
    def __init__(self, start_xpos, start_ypos, bspeed = 10):
        self.x = start_xpos
        self.y = start_ypos
        self.ballradius = 10
        self.ballSpeed = (bspeed, bspeed)

        self.recent_direction = 0

    #   direction  
    #   0: upleft       1: upright
    #   2: downleft     3: downright
    def move(self, direction):
        if direction == 0:
            self.x -= self.ballSpeed[0]
            self.y -= self.ballSpeed[1]
        elif direction == 1:
            self.x += self.ballSpeed[0]
            self.y -= self.ballSpeed[1]
        elif direction == 2:
            self.x -= self.ballSpeed[0]
            self.y += self.ballSpeed[1]
        elif direction == 3:
            self.x += self.ballSpeed[0]
            self.y += self.ballSpeed[1]
        self.recent_direction = direction

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.ballradius , WHITE)
    
class Game():
    def __init__(self):
        self.paddle_left = Paddle(0,300)
        self.paddle_right = Paddle(WIDTH-15,300)
        self.ball = Ball(WIDTH/2, HEIGHT/2)

        self.left_in_progress = False
        self.right_in_progress = False

        self.left_score = 0
        self.right_score = 0
        self.left_missed = 0
        self.right_missed = 0

        self.direction = 0

    #draw part

    def draw_game(self):
        screen.fill((0,0,0))
        self.paddle_left.draw()
        self.paddle_right.draw()
        self.ball.draw()
        self.draw_score()
        self.draw_line()

    def draw_score(self):
        screen.draw.text(
            'Score AI - Left = {0}\nBall Missed = {1}'.format(self.left_score,self.left_missed),
            color = WHITE,
            center = (WIDTH/4,25),
            fontsize = 32
        )
        screen.draw.text(
            'Score AI - Right = {0}\nBall Missed = {1}'.format(self.right_score,self.right_missed),
            color = WHITE,
            center = (WIDTH/4*3,25),
            fontsize = 32
        )
    def draw_line(self):
        screen.draw.line(
            (WIDTH/2, 0),
            (WIDTH/2, HEIGHT),
            color=WHITE
        )

    #update part

    def artificialInteligenceLeft(self):    #pong3's AI
        # If ball is moving away from paddle, center bat
        if self.ball.recent_direction in (1, 3):
            if (self.paddle_left.y + 50) < self.paddle_left.center_pos:
                self.paddle_left.down()
            elif (self.paddle_left.y + 50) > self.paddle_left.center_pos:
                self.paddle_left.up()
        # if ball moving towards bat, track its movement. 
        elif self.ball.recent_direction in (0, 2):
            if (self.paddle_left.y + 50) < self.ball.y:
                self.paddle_left.down()
            elif (self.paddle_left.y + 50) > self.ball.y:
                self.paddle_left.up()

    def artificialInteligenceRight(self):   #new AI
        self.paddle_right.movingTo(self.predict(self.ball.x, self.ball.y, self.direction,self.ball.ballSpeed))
        #predict -> get future_position
        #movingTo -> move paddle to future_position

    def predict(self, x, y, direction, speed):  #calculate posible pong position
        xpos, ypos = x, y
        if direction == 1:
            while True:
                if (ypos-speed[1]) <= 0:  #hit the top = recirsive call, until ball reaches right-side
                    (xpos, ypos) = self.predict(xpos,ypos,3,speed)  #w/ changed direction 1->3
                    break
                if (xpos+speed[0]) >= WIDTH:
                    break
                xpos += speed[0]
                ypos -= speed[1]
        elif direction == 3:
            while True: #calculate posible pong position
                if (ypos-speed[1]) >= HEIGHT:  #hit the bottom = recirsive call, until ball reaches right-side
                    (xpos, ypos) = self.predict(xpos,ypos,1,speed)  #w/ changed direction 3->1
                    break
                if (xpos+speed[0]) >= WIDTH:
                    break
                xpos += speed[0]
                ypos += speed[1]
        return xpos, ypos   #possible posision of the ball
        

    def ball_move(self):
        xspeed = self.ball.ballSpeed[0]
        yspeed = self.ball.ballSpeed[1]
        if self.direction == 0: #moving up-leftward
            if self.ball.x - xspeed <= 0 and self.ball.y - yspeed <= 0: #hit the top left corner
                self.direction = 3
                if self.paddle_left.isPonged(self.ball.y):  #hit the paddle +1
                    self.left_score += 1
                else: self.left_missed += 1 #missed +1
            elif self.ball.x - xspeed <= 0: #hit the left
                self.direction = 1
                if self.paddle_left.isPonged(self.ball.y):  #hit the paddle +1
                    self.left_score += 1
                else: self.left_missed += 1 #missed +1
            elif self.ball.y - yspeed <= 0: #hit the top
                self.direction = 2

        elif self.direction == 1:   #moving up-rightward
            if self.ball.x + xspeed >= WIDTH and self.ball.y - yspeed <= 0: #hit the top right corner
                self.direction = 2
                if self.paddle_right.isPonged(self.ball.y):  #hit the paddle +1
                    self.right_score += 1
                else: self.right_missed += 1 #missed +1
            elif self.ball.x + xspeed >= WIDTH: #hit the right
                self.direction = 0
                if self.paddle_right.isPonged(self.ball.y):  #hit the paddle +1
                    self.right_score += 1
                else: self.right_missed += 1 #missed +1
            elif self.ball.y - yspeed <= 0: #hit the top
                self.direction = 3

        elif self.direction == 2:   #moving down-leftward
            if self.ball.x - xspeed <= 0 and self.ball.y + yspeed >= HEIGHT:    #hit the bottom left corner
                self.direction = 1
                if self.paddle_left.isPonged(self.ball.y):  #hit the paddle +1
                    self.left_score += 1
                else: self.left_missed += 1 #missed +1
            elif self.ball.x - xspeed <= 0: #hit the left
                self.direction = 3
                if self.paddle_left.isPonged(self.ball.y):  #hit the paddle +1
                    self.left_score += 1
                else: self.left_missed += 1 #missed +1
            elif self.ball.y + yspeed >= HEIGHT:    #hit the bottom
                self.direction = 0

        elif self.direction == 3:   #moving down-rightward
            if self.ball.x + xspeed >= WIDTH and self.ball.y + yspeed >= HEIGHT:    #hit the bottom right corner
                self.direction = 0
                if self.paddle_right.isPonged(self.ball.y):  #hit the paddle +1
                    self.right_score += 1
                else: self.right_missed += 1 #missed +1
            elif self.ball.x + xspeed >= WIDTH: #hit the right
                self.direction = 2
                if self.paddle_right.isPonged(self.ball.y):  #hit the paddle +1
                    self.right_score += 1
                else: self.right_missed += 1 #missed +1
            elif self.ball.y + yspeed >= HEIGHT:    #hit the bottom
                self.direction = 1
        self.ball.move(self.direction)

gg = Game()

def update():
    gg.artificialInteligenceLeft()
    gg.artificialInteligenceRight()
    gg.ball_move()
def draw():
    gg.draw_game()
    
pgzrun.go()