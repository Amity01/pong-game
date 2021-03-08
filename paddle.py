from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def go_up(self):
        y_axis = self.ycor() + 20
        self.goto(self.xcor(), y_axis)

    def go_down(self):
        y_axis = self.ycor() - 20
        self.goto(self.xcor(), y_axis)
