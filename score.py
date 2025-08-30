from turtle import Turtle

class score_board(Turtle):
    def __init__(self):
        super().__init__()

        with open("high_score.txt","r") as file1:
            self.high_score=int(file1.read())
        self.score=0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(310,270)
        self.write(f"High Score = {self.high_score}",align="center",font=("Courier", 15, "bold"))
        self.goto(-340,270)
        self.write(f"Score = {self.score}",align="center",font=("Courier", 15, "bold"))
        
    def update_score(self):
        self.score+=1
        self.clear()
        self.goto(310,270)
        self.write(f"High Score = {self.high_score}",align="center",font=("Courier", 15, "bold"))
        self.goto(-340,270)
        self.write(f"Score = {self.score}",align="center",font=("Courier", 15, "bold"))
    def lost(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file1:
                file1.write(str(self.high_score))

            self.clear()
            self.goto(310,270)
            self.write(f"High Score = {self.high_score}",align="center",font=("Courier", 15, "bold"))
            self.goto(-340,270)
            self.write(f"Score = {self.score}",align="center",font=("Courier", 15, "bold"))
        
        self.goto(0,100)
        self.color("blue")
        self.write("YOU LOST STUPID, PLAY AGAIN!! ",align="center",font=("Courier", 25, "bold"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file1:
                file1.write(str(self.high_score))

        
        self.goto(-340,270)
        
        self.color("white")
        self.score=0
        self.clear()
        self.write(f"Score = {self.score}",align="center",font=("Courier", 15, "bold"))
        self.goto(310,270)
        self.write(f"High Score = {self.high_score}",align="center",font=("Courier", 15, "bold"))


