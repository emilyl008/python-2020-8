import turtle
jeannie = turtle.Turtle()
jeannie.shape('turtle')
jeannie.pensize(2)
jeannie.color('pink')
jeannie.penup()
step = 20
for i in range(30):
    jeannie.forward(step)
    jeannie.left(24)
    jeannie.stamp()
    step = step + 3
    turtle.done()