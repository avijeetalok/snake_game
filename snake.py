import turtle
import random
import time

delay = 0.30
score = 0
highestscore = 0
bodies = []

s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("gray")
s.setup(width=800, height=800)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0, 200)
food.st()

sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250, -250)
sb.write("Score: 0 | Heighest Score: 0")

def moveup():
    if head.direction != "down":
        head.direction = "up"

def movedown():
    if head.direction != "up":
        head.direction = "down"

def moveleft():
    if head.direction != "right":
        head.direction = "left"

def moveright():
    if head.direction != "left":
        head.direction = "right"

def movestop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()  # Corrected typo here
        head.setx(x - 20)  # Corrected typo here
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")
s.onkey(movestop, "space")

def generate_food():
    x = random.randint(-290, 290)  # Corrected typo here
    y = random.randint(-290, 290)  # Corrected typo here
    food.goto(x, y)

def restart_game():
    global score, delay, highestscore
    head.goto(0, 0)
    head.direction = "stop"
    for body in bodies:
        body.goto(1000, 1000)
    bodies.clear()
    score = 0
    delay = 0.1
    sb.clear()
    sb.write("Score: {} Highest Score: {}".format(score, highestscore))

generate_food()

while True:
    s.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        restart_game()

    if head.distance(food) < 20:
        generate_food()
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("red")
        new_body.penup()
        bodies.append(new_body)
        score += 10
        if score > highestscore:
            highestscore = score
        sb.clear()
        sb.write("Score: {} Highest Score: {}".format(score, highestscore))

    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    for body in bodies:
        if body.distance(head) < 20:
            restart_game()

    move()
    time.sleep(delay)

s.mainloop()
