

##############################3

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
RIGHT_ARROW = "Right" #pat attenion to upper and lower case.
TIME_STEP = 100 #update snake position after this many
                  #millisceonds.
SPACEBAR = "space"#careful, it's not supposed to be capitalized!.
UP = 0
#1. Make variables LEFT,DOWN, and RIGHT with values 1, 2 and 3
#####WRIGHT YOUR CODE HERE!!!
DOWN = 1
LEFT = 2
RIGHT = 3
direction = UP

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up ():
    global direction #snake direction is global (same everywhere)
    direction=UP     #change direction to up.
    print ("You pressed the up key!")
#2 make functions down(), left(), and right() that change direction

def down ():
    global direction
    direction=DOWN
    print ("You pressed the down key")

def left ():
    global direction
    direction=LEFT
    print ("You pressed the left key")

def right ():
    global direction
    direction=RIGHT
    print ("You pressed the right key")
    
turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

##def make_food():
##    #The screen positions go from -SIZE/2 to +SIZE/2
##    #But we need to make food pieces only appear on game squares
##    #So we cut up the game board into multiples of SQUARE_SIZE.
##    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
##    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
##    min_y=-int(SIZE_y/2/SQUARE_SIZE)-1
##    max_y=int(SIZE_y/2/SQUARE_SIZE)+1

    #Pick a position that is a random multiple os SQUARE_SIZE 
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction==RIGHT:
        snake.goto(x_pos +SQUARE_SIZE, y_pos)
        print ("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down!")
    elif direction==UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")

    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

    #If snake is on top of the food item
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #what does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print ("You have eaten the food!")
                         
    #Grab position of snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    #the next 3 lines check if the snake is hitting the right edge
    if new_x_pos >= RIGHT_EDGE:
        print ("You hit the right edge! Game over!")
        quit()
        
    if new_y_pos >= UP_EDGE:
        print ("You hit the up edge! Game over!")
        quit()

    if new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    if new_y_pos <= DOWN_EDGE:
        print ("You hit the down edge! Game over!")
        quit()

    turtle.ontimer(move_snake,TIME_STEP)  #<---------new line here
move_snake()



turtle.register_shape ("trash.gif")    # add trush picture
                                    # make sure you have downloaded this shape
                                    # from the google drive folder and save it
                                    # in the same folder as this python script
food = turtle.clone()
food.shape ("trash.gif")

#locations of food
food_pos =  [(100,100), (-100,100), (-100,-100), (100,-100) ]
food_stamps = []
food.hideturtle()


for xy in food_pos:
    food.goto(xy)
    f = food.stamp()
    food_stamps.append(f)
    


turtle.mainloop()
