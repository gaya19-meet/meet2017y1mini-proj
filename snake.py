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

#Intiialize lists
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


    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?
    #You're RIGHT!
    x_pos = x_pos + SQUARE_SIZE

    my_pos = (x_pos, y_pos) #Store position variables in the tuple
    snake.goto(x_pos,  ) #Move snake to new (x,y)

    #Append the new position tuple to pos_list
      .append(  )

      #save the stamp ID! you'll need to erase it later.then append
      #it to stamp_list
       = snake.stamp()
        .append( )
        
