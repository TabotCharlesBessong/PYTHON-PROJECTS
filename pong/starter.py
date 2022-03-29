
import turtle

from numpy import pad

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
# main game loop
while True:
  wn.update()