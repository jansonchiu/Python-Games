import turtle

win = turtle.Screen()
win.title("Pong by @jansonchiu")
win.bgcolor("black")
win.setup(width=800, height=600)
 
# This stops the window from updating 
win.tracer(0)

# Paddle A 
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
# This stretches the width by 5 times 
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
#This starts the paddle on the left
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


# Main game loop 
while True: 
  win.update()
