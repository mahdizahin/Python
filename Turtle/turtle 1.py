import turtle
turtle.bgcolor("black")
turtle.pensize(6)
turtle.speed(20)

for i in range(6) :
    for colours in [ "red" ,"green", "white","orange","skyblue","red"]:
     turtle.color(colours)
     turtle.circle(100)
     turtle.left(10)


turtle.hideturtle()
