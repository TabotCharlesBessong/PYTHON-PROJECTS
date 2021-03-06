
import turtle
# import os
import winsound

# from numpy import pad

wn = turtle.Screen()
wn.title("PingPong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Adding paddles 
# paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5 , stretch_len=1)
paddleA.penup()
paddleA.goto(-350,0)
# paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5 , stretch_len=1)
paddleB.penup()
paddleB.goto(350,0)
# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = 1

# drawing the score on the screen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("palyer A: 0 Player B: 0 ", align="center", font=("Courier",24,"normal"))

# score variable
scoreA = 0
scoreB = 0


# functions to move ball and paddles 
def paddleAUp():
  y = paddleA.ycor()
  y += 20
  paddleA.sety(y)

def paddleADown():
  y = paddleA.ycor()
  y -= 20
  paddleA.sety(y)
  
def paddleBUp():
  y = paddleB.ycor()
  y += 20
  paddleB.sety(y)

def paddleBDown():
  y = paddleB.ycor()
  y -= 20
  paddleB.sety(y)

# Ball x movement 


# Keyboard events 
wn.listen()
wn.onkeypress(paddleAUp,"w")
wn.onkeypress(paddleADown,"s")
wn.onkeypress(paddleBUp,"Up")
wn.onkeypress(paddleBDown,"Down")


# main game loop
while True:
  wn.update()
  
  # lets move the ball
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)
  
  # border check
  if(ball.ycor() > 290):
    ball.sety(290)
    ball.dy *=-1
    # os.system("afplay bounce.wav&")
    winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
  if(ball.ycor() < -290):
    ball.sety(-290)
    ball.dy *=-1
    # os.system("afplay bounce.wav&")
    winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
  if(ball.xcor() > 390):
    ball.goto(0,0)
    ball.dx *=-1
    scoreA +=1
    pen.clear()
    pen.write("palyer A: {} Player B: {} ".format(scoreA , scoreB), align="center", font=("Courier",24,"normal"))

  if(ball.xcor() < -390):
    ball.goto(0,0)
    ball.dx *=-1
    scoreB +=1
    pen.clear()
    pen.write("palyer A: {} Player B: {} ".format(scoreA, scoreB), align="center", font=("Courier",24,"normal"))

    
  # Paddle and ball collision
  if (ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50 )):
    ball.setx(340)
    ball.dx *=-1
    # os.system("aplay bounce.wav")
    winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
  if (ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddleA.ycor() + 50 and ball.ycor() < paddleA.ycor() - 50 )):
    ball.setx(-340)
    ball.dx *=-1
    # os.system("aplay bounce.wav")
    winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)