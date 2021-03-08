from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_step = 10
        self.x_step = 10

    def move(self):
        new_x = self.xcor()+self.x_step
        new_y = self.ycor()+self.y_step
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_step = - self.y_step

    def bounce_x(self):
        self.x_step = -self.x_step

    def start(self):
        self.goto(0,0)
        self.x_step *= -1
