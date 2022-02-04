import turtle
import random
import time
delay=0.1
score=0
highestscore=0
bodies=[]#snakebodycalculation
s=turtle.Screen()#for screen to show the game
s.title("Snake Game")
s.bgcolor("gray")
s.setup(width=600,height=600)
head=turtle.Turtle() #creating head of snake using Turtle
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup() #not move
head.goto(0,0)
head.direction="stop"
#snake food
food=turtle.Turtle() #creating head of snake using Turtle
food.speed(0)
food.shape("circle")
food.color("yellow")
food.fillcolor("green")
food.penup() #not move
food.ht()#for invisibility
food.goto(0,200)#x axis 0 and y axis 200
food.st()
#scrore board
sb=turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250,-250)
sb.write("Score:0 | Highest Score:0")
def moveup():
    if head.direction!="down":
     head.direction="up"
def movedown():
    if head.direction !="up":
     head.direction = "down"
def moveright():
    if head.direction != "left":
        head.direction = "right"
def moveleft():
    if head.direction != "right":
        head.direction = "left"
def movestop():
    head.direction="stop"
    def move():
        if head.direction=="up":
            y=head.ycor()
            head.sety(y+20)
        if head.direction=="down":
            y=head.ycor()
            head.sety(y-20)
        if head.direction == "right":
            x = head.xcor()
            head.setx(x+20)
        if head.direction == "left":
            x = head.xcor()
            head.setx(x-20)
            #Event Handling
            s.listen()
            s.onkey(moveup(),"Up")
            s.onkey(movedown(),"Down")
            s.onkey(moveright(),"Right")
            s.onkey(moveleft(),"Left")
            s.onkey(movestop(),"Space")
            #main loop
            s.update() #update the screen
            if head.xcor()>290:
                head.setx(-290)
            if head.xcor()<-290:
                head.setx(290)
            if head.ycor()>290:
                head.sety(-290)
            if head.ycor() >-290:
                head.sety(290)
                #collision with food
                if head.distance(food)<20:
                    x=random.randint(-290,290)
                    y=random.randint(-290,290)
                    food.goto(x,y)
                    #increase length of the snake
                    body=turtle.Turtle()
                    body.speed(0)
                    body.penup()
                    body.shape("square")
                    body.color("red")
                    body.fillcolor("black")
                    bodies.append(body) #append new body after eating food
                    score+=10
                    delay-=0.001
                if score>highestscore:
                    highestscore=score
sb.clear()
sb.write("Score:{} Highest Score:{}" .format(score,highestscore))
# Move Snake Body
for index in range (len (bodies) -1,0,-1):
    x = bodies[index-1].xcor()
    y = bodies[index-1].ycor()
    bodies[index].goto(x,y)
    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
        move()
        #checking collision of snake body
        for body in bodies:
            if body.distance(head)<20:
                time.sleep(1)
                head.goto(0,0)
                head.direction="stop"
                #hide bodies
                for body in bodies:
                    body.ht()
                    bodies.clear()
                    score=0
                    delay=0.1
                #update score board
                sb.clear()
                sb.write("Score:{} Highest Score:{}".format(score, highestscore))
                time.sleep(delay)
                s.mainloop()


