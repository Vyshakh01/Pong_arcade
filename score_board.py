from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self,):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.color("white")
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"{self.l_score}",align="center",font=("Arial", 70, "normal"))
        self.goto(100,200)
        self.write(f"{self.r_score}",align="center",font=("Arial", 70, "normal"))
    def l_point(self):
        self.l_score+=1
        self.update_score()
    def r_point(self):
        self.r_score+=1
        self.update_score()
    def gameover(self,player):
        self.goto(0,0)
        self.write(f"GAME OVER\n {player} wins  ", align="center", font=("Arial", 60, "normal"))
