from turtle import Turtle
class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,-300)
        self.draw()

    def draw(self):
        self.setheading(90)
        while self.ycor()<300:
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)

