import turtle
import random
import math

class Ball(turtle.Turtle):
    gravity = -0.05  # pixels/(time of iteration)^2
    energy_loss_ground = 0.8
    energy_loss_walls = 0.8
    energy_loss_balls = 0.99

    def __init__(self, x=0, y=0):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.y_velocity = random.randint(-50, 50) / 10
        self.x_velocity = random.randint(-50, 50) / 10
        self.setposition(x, y)
        self.size = int(random.gammavariate(25, 0.8))
        self.color((random.random(),
                    random.random(),
                    random.random())
                   )
    def draw(self):
        self.clear()
        self.dot(self.size)

    def move(self):
        self.y_velocity += self.gravity
        self.sety(self.ycor() + self.y_velocity)
        self.setx(self.xcor() + self.x_velocity)

    def bounce_floor(self, floor_y):
        if self.ycor() < floor_y:
            self.y_velocity = -self.y_velocity * self.energy_loss_ground
            self.sety(floor_y)

    def bounce_walls(self, wall_x):
        if abs(self.xcor()) > wall_x:
            self.x_velocity = -self.x_velocity * self.energy_loss_walls
            sign = self.xcor() / abs(self.xcor())
            self.setx(wall_x * sign)

    def bounce_others(self, otherBall):
        distBall = math.sqrt((otherBall.xcor()-self.xcor())**2 + (otherBall.ycor()-self.ycor())**2)
        totalRadii = self.size + otherBall.size
        angleBetweenBalls = math.atan2(otherBall.ycor()-self.ycor(), otherBall.xcor()-self.xcor())
        if abs(distBall - totalRadii) < 1E-1:
            self.x_velocity = -self.x_velocity * self.energy_loss_balls
            self.y_velocity = -self.y_velocity * self.energy_loss_balls

            # sign = self.xcor() / abs(self.xcor())
            # self.setx(otherBall.xcor() * sign)


# Simulation code
width = 1200
height = 800

window = turtle.Screen()
window.setup(width, height)
window.tracer(0)

balls = [Ball() for _ in range(6)]

def add_ball(x, y):
    balls.append(Ball(x, y))

window.onclick(add_ball)

while True:
    balls = [currBall for currBall in balls if currBall.y_velocity != 0]
    for ball in balls:
        ball.draw()
        ball.move()
        ball.bounce_floor(-height/2)
        ball.bounce_walls(width/2)
        for otherBall in balls:
            if ball != otherBall:
                ball.bounce_others(otherBall)

    window.update()