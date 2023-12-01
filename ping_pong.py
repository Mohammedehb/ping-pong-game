import turtle

wind = turtle.Screen()  #intializ screen
wind.title("ping pong")
wind.bgcolor("black")
wind.setup(width=1200,height=800)
wind.tracer(0)   #stops the window from updating automatically

#player 1
player1 = turtle.Turtle() #intializes turtle object
player1.speed(0) # set the speed of the animation
player1.shape("square") # set the shape of player1
player1.color("cyan") # set the color of the player1
player1.shapesize(stretch_wid=5,stretch_len=1) #stetches the shapeto meet the size
player1.penup() #stops the drawing lines
player1.goto(-550,0) #set the player1

#player 2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("pink")
player2.shapesize(stretch_wid=5,stretch_len=1)
player2.penup()
player2.goto(550,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
###to set the speed of dirction of x
ball.dx = 0.4
###to set the speed of dirction of y
ball.dy = 0.4

#score
score1=0
score2=0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,360)
score.write("player 1: 0 Player 2: 0",align="center", font=("Courier",24,"normal"))

def player1_moveUp():
    y=player1.ycor() #get the y cordinate
    y+=20 #set y and increase by 20
    player1.sety(y)#set y of player1 to the new y coordinate

def player1_moveDown():
    y = player1.ycor()
    y -= 20
    player1.sety(y)

# player 2 set
def player2_moveUp():
    x=player2.ycor()
    x+=20
    player2.sety(x)

def player2_moveDown():
    x = player2.ycor()
    x -= 20
    player2.sety(x)

#Keyboard bindings
wind.listen()
wind.onkeypress(player1_moveUp,"w")
wind.onkeypress(player1_moveDown,"s")
wind.onkeypress(player2_moveUp,"Up")
wind.onkeypress(player2_moveDown,"Down")

while True:
    wind.update() #update the screen
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor()>390:
        ball.sety(390)
        ball.dy *=-1
    if ball.ycor()<-390:
        ball.sety(-390)
        ball.dy *= -1
    #check the x coordinate
    if ball.xcor()>590:
        ball.goto(0,0)
        ball.dx *= -1
        score1 +=1
        score.clear()
        score.write("player 1: {} Player 2: {}".format(score1,score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor()<-590:
        ball.goto(0,0)
        ball.dx *= -1
        score2 +=1
        score.clear()
        score.write("player 1: {} Player 2: {}".format(score1,score2), align="center", font=("Courier", 24, "normal"))

    #players can hit the ball
    if(ball.xcor() > 540 and ball.xcor()<550) and (ball.ycor()<player2.ycor()+40 and ball.ycor()>player2.ycor()-40):
        ball.setx(540)
        ball.dx *=-1
    if (ball.xcor() < -540 and ball.xcor() > -550) and (ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor() - 40):
        ball.setx(-540)
        ball.dx *= -1



