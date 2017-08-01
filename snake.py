import turtle
import random #we'll need this later in the lab

turtle.tracer(1,0) #this help the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's help the turtle window
                             #size.
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6

#Intialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()


#draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces in the
#snake (i.e. START_LENGHT)
for i in range(START_LENGTH):
    x_pos=snake.pos()[0] #get x-position with snake.pos() [0]
    y_pos=snake.pos()[1]
    # add SQUARE_SIZE
    x_pos = x_pos + SQUARE_SIZE
    my_pos = (x_pos, y_pos)
    snake.goto(x_pos, y_pos)
    pos_list.append(my_pos)
    stamp_id = snake.stamp()
    stamp_list.append(stamp_id)

UP_ARROW = "Up" #make sure you pay attention to upper and lower
                #case.
LEFT_ARROW = "Left" #pay attention to upper and lower case.
DOWN_ARROW = "Down" #pay attention to upper and lower case.
RIGHE_ARROW = "Right" #pat attenion to upper and lower case.
TIME_STEP = "100" #update snake position after this many
                  #millisceonds.
SPACEBAR - "Space"#careful, it's not supposed to be capitalized!.
UP = 0
#1. Make variables LEFT,DOWN, and RIGHT with values 1, 2 and 3
#####WRIGHT YOUR CODE HERE!!!
DOWN = 1
LEFT = 2
RIGHT = 3
direction = UP

def up ():
    global direction #snake direction is global (same everywhere)
    direction=UP #change direction to up.
    move_snake() #update the snake drawing <- remember me later
    print ("You pressed the up key!")
#2 make functions down(), left(), and right() that change direction
def down ():
    global direction
    direction=DOWN
    move_snake()
    print ("You pressed the down key")
def left ():
    global direction
    direction=LEFT
    move_snake()
    print ("You pressed the left key")
def right ():
    global direction
    direction=RIGHT
    move_snake()
    print ("You pressed the right key")
    
turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos [0]
    y_pos = my_pos[1]

    if direction==RIGHT:
        snake.goto(x_pos +SQUARE_SIZE, y_pos)
        print ("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")

        my_pos=snake.pos()
        pos_list.append
