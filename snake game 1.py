

import turtle
import time
import random

#delay
delay=0.1#0.1 second time\

#scores
score=0
high_score=0

#creting window screen
wn = turtle.Screen()
wn.title('SNAKE GAME')
wn.bgcolor('white')


#width and height as user's choice
wn.setup(width=600,height=600)
wn.tracer(0)#0 means false. tracing is off

#head of the snake
head=turtle.Turtle() #getting the turtle (arrow)
head.shape('square')
head.color('black')
head.penup()# you can move turtle without leaving tracks
head.goto(0,100)# x and y axis position
head.direction='stop' # act as variable and changed below

#food
food=turtle.Turtle()
food.shape('triangle')
food.color('red')
food.speed(0)
food.penup()
food.goto(0,0)
food.shapesize(.5,.5)

#pen
pen=turtle.Turtle()
pen.shape('square')
pen.speed(0)
pen.color('red')
pen.penup()
pen.hideturtle()
pen.goto(0,260)

pen.write('score 0 high score {}'.format(score,high_score),font=('Courier'),align='center')

#snake body
segments=[]


#move function
def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)
    if head.direction=='down':
        y=head.ycor()
        head.sety(y-20)
    if head.direction=='right':
        x=head.xcor()
        head.setx(x+20)
    if head.direction=='left':
        x=head.xcor()
        head.setx(x-20)
#up & down not on same axis and want to turn it
def move_up():
    if head.direction!='down':
        head.direction='up'
    
def move_down():
    if head.direction!='up':
        head.direction='down'
def move_right():
    if head.direction!='left':
        head.direction='right'
def move_left():
    if head.direction!='right':
        head.direction='left'



# keyboard link
wn.listen()
wn.onkey(move_up, 'w')
wn.onkey(move_down, 's')
wn.onkey(move_right, 'd')
wn.onkey(move_left, 'a')

#colors
colors=['red','yellow','pink','purple','violet','brown']




while True:
    wn.update()
    if head.distance(food)<15:
        x= random.randint(-290,290)#getting random number between -290 and 290
        y= random.randint(-290,290)
        food.goto(x,y) # food after eating goes randomly
        new_segment=turtle.Turtle()
        new_segment.shape('square')
        new_segment.color(random.choice(colors))
        new_segment.penup()
        segments.append(new_segment)

        score+=10
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write('score {} high score {}'.format(score,high_score),font=('Courier'),align='center')





    
    for i in range(len(segments)-1,0,-1):
        x=segments[i-1].xcor()
        y=segments[i-1].ycor()
        segments[i].goto(x,y)

    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)#1 sec time
        head.goto(0,0)
        head.direction='stop'

        for segment in segments:
            segment.goto(1000,1000)# out of frame .so not seen
        segments=[]# segments are empty. so game starts again.

        #beforethis collinding takes place
        score=0
        pen.clear()
        pen.write('score {} high score {}'.format(score,high_score),font=('Courier'),align='center')



        
    move()

    for segment in segments:
        if segment.distance(head)<20: #segment collides with segment
            time.sleep(1)
            head.goto(0,0)
            head.direction='stop'
            
            for segment in segments:
                segment.goto(1000,1000)
            
    time.sleep(delay)

   
























