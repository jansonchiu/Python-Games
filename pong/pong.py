import turtle

win = turtle.Screen()
win.title("Pong by @jansonchiu")
win.bgcolor("black")
win.setup(width=800, height=600)
 
# This stops the window from updating 
win.tracer(0)

# Score
score_a = 0
score_b = 0 

# Paddle A 
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
# This stretches the width by 5 times 
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
# This starts the paddle on the left
# Since the center is 0,0
paddle_a.goto(-350, 0)

# Paddle B 
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
# This stretches the width by 5 times 
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
#This starts the paddle on the right
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
#This starts the paddle on the right
ball.goto(0, 0)
# How much the ball moves 
ball.dx = 2
ball.dy = -2

# Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))
#Function to move paddle a up
def paddle_a_up(): 
  # find current y coordinate 
  y = paddle_a.ycor()
  # This adds 20 pixels to y
  y += 20 
  paddle_a.sety(y)

#Function to move paddle a down
def paddle_a_down(): 
  # find current y coordinate 
  y = paddle_a.ycor()
  # This adds 20 pixels to y
  y -= 20 
  paddle_a.sety(y)

#Function to move paddle d up
def paddle_b_up(): 
  # find current y coordinate 
  y = paddle_b.ycor()
  # This adds 20 pixels to y
  y += 20 
  paddle_b.sety(y)

#Function to move paddle b down
def paddle_b_down(): 
  # find current y coordinate 
  y = paddle_b.ycor()
  # This adds 20 pixels to y
  y -= 20 
  paddle_b.sety(y)


# Keyboard Binding
# This calls the y coordinate 
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
# This moves the paddle b up and down using up and down arrow keys
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main game loop 
while True: 
  win.update()

  # Move the ball 
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

  # Border checking 
  if ball.ycor() > 290:
    ball.sety(290)
    # This reverses the direction 
    ball.dy *= -1

  if ball.ycor() < -290:
    ball.sety(-290)
    # This reverses the direction 
    ball.dy *= -1

  if ball.xcor() > 390: 
    # Ball gets put to center
    ball.goto(0, 0)
    ball.dx *= -1
    score_a += 1
    pen.clear()
    pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

  if ball.xcor() < -390: 
    # Ball gets put to center
    ball.goto(0, 0)
    ball.dx *= -1
    score_b += 1
    pen.clear()
    pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
  # Paddle and ball collisions
  if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
    ball.setx(340)
    ball.dx *= -1

  if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
    ball.setx(-340)
    ball.dx *= -1