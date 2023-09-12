from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,postion):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(postion)

    def up(self):
        new_y = self.ycor()+30
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor()-30
        self.goto(self.xcor(), new_y)




