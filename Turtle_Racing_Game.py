##Turtle Racing Game
##November Project

##The Purpose of this project is a simple horse racing game within Python
##Each race allows for a different number of racers
##Any Comments welcome please let me know what you think

from turtle import *
from random import randint

def main():
    races = race_set_up()
    for i in range(races):
        turtlelist = []
        turtles = turtle_set_up(turtlelist)    
        scr = Screen()
        scr.setup(720, 350)
        
        horse, jockey = one_horse_at_a_time_race(turtles)
        message = "The " + jockey + " jockey on the " + horse + " horse WINS!"
        if races > 1:
            scr.textinput(message, "Press Ok and Click the screen to begin the next race")
        else:
            scr.textinput(message, "Press Ok and Click the screen to exit")
        scr.exitonclick()
    
    print("Thanks For Playing")
def race_set_up():
    print("Please Enter the number of races you would like to have.")
    x = confirmed_positive_integer_input()
    while x > 20:
        print("Too many consecutive races")
        print("Max Consecutive Races: 20")
        print("Please Enter the number of races you would like to have.")
        x = confirmed_positive_integer_input()
    return int(x)

def one_horse_at_a_time_race(turtles):
    pos = 0
    y = len(turtles)
    while pos < 250:
        x = randint(0, y-1)
        turtles[x].forward(5)
        pos = turtles[x].xcor()
    jockey = str(turtles[x].fillcolor())
    horse = str(turtles[x].pencolor())
    turtles[x].right(1080)
    return horse, jockey
        

def turtle_set_up(_list):
    print("Please Enter a Number of Racers between 2 and 11 (inclusive)")
    num = confirmed_positive_integer_input()
    while num < 2 or num > 11:
        print("Please Enter a Number between 2 and 11 (inclusive)")
        num = confirmed_positive_integer_input()
    num = int(num)
    turtlelist = _list
    colorlist = ["black","red","hotpink","purple","blue","green","cyan"]
    for p in range(num):
        x = str(p)
        
        x = Turtle()
        
        if p == 0:
            x.up()
            x.setpos(-250,0)
            x.down()
        elif p%2 == 0:
            x.up()
            x.setpos(-250, 25*(p//2))
            x.down()
        elif p%2 == 1:
            x.up()
            x.setpos(-250, -(25*((p+1)//2)))
            x.down()
        pen = p
        fill = -(p+1)
        if pen > 6:
            pen = p - 5
            fill = fill+7
        x.color(colorlist[pen],colorlist[fill])
        turtlelist.append(x)
   
    return turtlelist
        



        
def confirmed_positive_integer_input():
    valid = False
    while not valid:
        user_input = input("Please enter an Positive Integer: ")
        num_c = is_number(user_input)
        if not num_c:
            print("Invalid Input: Not a Number, please try again...")
            continue
        user_number = float(user_input)
        if not is_whole_number(user_number):
            print("Invalid Input: Not a Whole Number, please try again...")
            continue
        if user_number <= 0:
            print("Invalid Input: Not a Positive Number, please try again...")
            continue
        valid = True

    return user_number


def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def is_whole_number(x):
    check = x%1
    if check == 0:
        return True
    else:
        return False


main()
