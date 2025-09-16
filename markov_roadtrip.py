""" 
Charlotte Clements
CSCI 3725
M1
Date: 09/16/2025
This program uses a probability matrix, which represents the likelihood that 
one biome will naturally occur near another, to generate landscape. Users can
navigate through the landscape using the arrow keys

Dependencies: time, os, numpy, turtle, random
"""
import time
import os
import numpy as np
from turtle import Turtle, Screen
import random

MAGNIFICATION = 10
CAN_MOVE_CAR_RIGHT = True
CAN_MOVE_CAR_LEFT = False
MOVING_LEFT = False
MOVING_RIGHT = False
CAR_Y_COORD = -50
CAR_DISTANCE_ALLOWED_FROM_EDGE = 100
CAR = os.path.expanduser("/Users/cclements/Library/CloudStorage/OneDrive-" +
                         "BowdoinCollege/Desktop/car_drawing_smaller.gif")
FLIPPEDCAR = os.path.expanduser("/Users/cclements/Library/CloudStorage/" +
                                "OneDrive-BowdoinCollege/Desktop/car_drawing" + 
                                "_flipped.gif")
MARKOV_MATRIX = {
    "Small hill": {
        "Small hill": 0.2,
        "Big hill": 0.2,
        "Small mountain": 0.1,
        "Big mountain": 0,
        "Desert": 0.1,
        "Forest": 0.3,
        "Lake": 0.1
        },
    "Big hill": {
        "Small hill": 0.1,
        "Big hill": 0.1,
        "Small mountain": 0.5,
        "Big mountain": 0,
        "Desert": 0.1,
        "Forest": 0.2,
        "Lake": 0
        },
    "Small mountain": {
        "Small hill": 0.1,
        "Big hill": 0.1,
        "Small mountain": 0.1,
        "Big mountain": 0.5,
        "Desert": 0,
        "Forest": 0.2,
        "Lake": 0
        },
    "Big mountain": {
        "Small hill": 0.1,
        "Big hill": 0.1,
        "Small mountain": 0.3,
        "Big mountain": 0.2,
        "Desert": 0,
        "Forest": 0.2,
        "Lake": 0.1
        },
    "Desert": {
        "Small hill": 0.2,
        "Big hill": 0.1,
        "Small mountain": 0.5,
        "Big mountain": 0,
        "Desert": 0.2,
        "Forest": 0,
        "Lake": 0.0
        },
    "Forest": {
        "Small hill": 0.1,
        "Big hill": 0.1,
        "Small mountain": 0.3,
        "Big mountain": 0.1,
        "Desert": 0,
        "Forest": 0.1,
        "Lake": 0.3
        },
    "Lake": {
        "Small hill": 0.2,
        "Big hill": 0,
        "Small mountain": 0.1,
        "Big mountain": 0.1,
        "Desert": 0.0,
        "Forest": 0.5,
        "Lake": 0
        }
    }

# Screen and canvas initialization
screen = Screen()
canvas = screen.getcanvas()
WIDTH, HEIGHT = screen.screensize()
    
    
""" Draws a big mountain with a jagged peak
"""
def draw_big_mountain():
    turtle.color("gray")
    turtle.forward(10)
    turtle.right(-60)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(20)
    turtle.right(-120)
    turtle.forward(40)
    turtle.right(120)
    turtle.forward(120)
    turtle.right(-60)
    turtle.forward(10)
    
    
""" Draws a small, simple mountain
"""   
def draw_small_mountain():
    turtle.color("gray")
    turtle.forward(10)
    turtle.right(-45)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(-45)
    turtle.forward(10)
    
    
""" Draws an individual tree
"""    
def draw_tree():
    turtle.color("dark green")
    turtle.forward(5)
    turtle.right(-75)
    turtle.forward(5)
    turtle.right(150)
    turtle.forward(5)
    turtle.right(-75)
    turtle.forward(5)
    
    
""" Draws an individual sand dune
"""   
def draw_sand_dune():
    turtle.color("LightGoldenrod3")
    turtle.forward(5)
    turtle.right(-50)
    turtle.forward(10)
    turtle.right(100)
    turtle.forward(10)
    turtle.right(-50)
    turtle.forward(5)
    

""" Draws a small hill using a circle segment
"""    
def draw_small_hill():
    turtle.color("light green")
    turtle.forward(5)
    turtle.penup()
    turtle.right(90)
    turtle.forward(10)
    turtle.circle(20, 210)
    turtle.pendown()
    turtle.circle(20, 120)
    turtle.penup()
    turtle.circle(20, 30)
    turtle.right(180)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(40)
    turtle.pendown()
    turtle.forward(5)
    

""" Draws a big hill using a circle segment
"""    
def draw_big_hill():
    turtle.color("light green")
    turtle.forward(5)
    turtle.penup()
    turtle.back(4)
    turtle.right(90)
    turtle.forward(25)
    turtle.circle(50, 210)
    turtle.pendown()
    turtle.circle(50, 120)
    turtle.penup()
    turtle.circle(50, 30)
    turtle.right(180)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(96)
    turtle.pendown()
    turtle.forward(5)
    

""" Draws a collection of sand dunes
    Args:
         dune_num (int): the number of sand dunes to draw
""" 
def draw_desert(dune_num):
    for _ in range(dune_num):
        draw_sand_dune()
    
    
""" Draws a collection of sand dunes
    Args:
         tree_num (int): the number of trees to draw
"""
def draw_forest(tree_num):
    for _ in range(tree_num):
        draw_tree()
        
        
""" Draws a lake as a simple blue line
    Args:
         scale (int): use this value to modify the length of the lake
"""       
def draw_lake(scale):
    turtle.color("light blue")
    for _ in range(scale):
        turtle.forward(20)
       
       
""" Generates a list of biomes in a landscape
    Args:
         current_biome (string): the starting biome
    Return (string): 
         The next biome
"""          
def next_biome(current_biome):
    biomes = list(MARKOV_MATRIX.keys())
    weights = [MARKOV_MATRIX[current_biome][new_biome] 
                   for new_biome in biomes]       
    next_biome = random.choices(biomes, weights, k=1)[0]
    return next_biome


""" Draws each biome in a landscape
    Args:
         first_biome (string): the starting biome
"""  
def draw_biomes(first_biome):
    right_limit = screen.screensize()[0]/2
    current_biome = first_biome
    while(turtle.pos()[0] < right_limit):
        new_biome = next_biome(current_biome)
        if new_biome == "Small hill":
            draw_small_hill()
        elif new_biome == "Big hill":
            draw_big_hill()
        elif new_biome == "Small mountain":
            draw_small_mountain()
        elif new_biome == "Big mountain":
            draw_big_mountain()
        elif new_biome == "Desert":
            draw_desert(5)
        elif new_biome == "Forest":
            draw_forest(10)
        elif new_biome == "Lake":
            draw_lake(2)
        current_biome = new_biome
        

""" Chooses a random biome, and then uses it to generate a landscape
"""          
def generate_landscape():
    biomes = list(MARKOV_MATRIX.keys())
    first_biome = random.choice(biomes)
    screen.tracer(False)
    draw_biomes(first_biome)
    screen.update()
    screen.tracer(True)    

""" Adjusts screen and canvas settings
"""        
def start_screen_and_canvas():
    screen.addshape(CAR)
    screen.addshape(FLIPPEDCAR)
    screen.screensize(WIDTH * MAGNIFICATION, HEIGHT)
    canvas.config(xscrollincrement=1)    
       
       
""" Initializes settings and moves the turtle to the lefthand edge of the 
    canvas
""" 
def start_turtle():
    turtle.width(MAGNIFICATION/2)
    turtle.speed(10)    
    turtle.penup()
    start_pos = -(WIDTH * MAGNIFICATION)/2
    turtle.goto(start_pos, 0)
    turtle.pendown()   
    

""" Initializes settings, moves the car to the lefthand edge of the canvas, and 
    scrolls to that position
""" 
def start_car():
    car_turtle.shape(CAR)
    car_turtle.hideturtle()
    car_turtle.penup()
    car_initial_x = -(WIDTH * MAGNIFICATION)/2 + CAR_DISTANCE_ALLOWED_FROM_EDGE
    canvas.xview_scroll(int(car_initial_x), "units")
    car_turtle.goto(car_initial_x, CAR_Y_COORD)
    car_turtle.showturtle()    
        
     
""" Allows a user to start driving right by pressing the right arrow key
"""    
def right():
    global CAN_MOVE_CAR_RIGHT
    global CAN_MOVE_CAR_LEFT
    global MOVING_RIGHT
    if (CAN_MOVE_CAR_RIGHT is True and CAN_MOVE_CAR_LEFT is False and 
        MOVING_RIGHT is False):
        car_turtle.shape(CAR)
        right_limit = screen.screensize()[0]/2 - 100
        while(car_turtle.pos()[0] < right_limit):
            MOVING_RIGHT = True
            car_turtle.forward(5)
            scroll_length = 5
            canvas.xview_scroll(scroll_length, "units")        
            time.sleep(0.005)
        MOVING_RIGHT = False
        CAN_MOVE_CAR_RIGHT = False
        CAN_MOVE_CAR_LEFT = True


""" Allows a user to start driving left by pressing the left arrow key
"""   
def left():
    global CAN_MOVE_CAR_RIGHT
    global CAN_MOVE_CAR_LEFT  
    global MOVING_LEFT
    if (CAN_MOVE_CAR_LEFT is True and CAN_MOVE_CAR_RIGHT is False and 
        MOVING_LEFT is False):
        car_turtle.shape(FLIPPEDCAR)
        left_limit = -screen.screensize()[0]/2 + 100
        while(car_turtle.pos()[0] > left_limit):
            MOVING_LEFT = True
            car_turtle.back(5)
            scroll_length = -5
            canvas.xview_scroll(scroll_length, "units")        
            time.sleep(0.005)
        MOVING_LEFT = False
        CAN_MOVE_CAR_LEFT = False
        CAN_MOVE_CAR_RIGHT = True


# Adjust screen and canvas settings
start_screen_and_canvas()

# Turtle initialization
turtle = Turtle("turtle", visible=False)
start_turtle()

# Car initialization
car_turtle = Turtle()
start_car()

# Generate a landscape
generate_landscape()

# Lets us view the finished landscape for as long as we want
screen.onkeypress(right, "Right")
screen.onkeypress(left, "Left")
screen.listen()
screen.mainloop()