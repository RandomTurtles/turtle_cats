import turtle
import random


def circle(turtle):
    for i in range(30):
        turtle.forward(10)
        turtle.left(25)


def spiral(turtle):
    # small loop
    for i in range(100):
        turtle.forward(10)
        turtle.left(i)


def random_color(my_turtle):
    r = random.random()
    g = random.random()
    b = random.random()
    my_turtle.color(r, g, b)


def random_spirals(turtle):
    r = random.random()
    if r < 0.5:
        # small loop
        for i in range(100):
            turtle.forward(10)
            turtle.left(i)
    else:
        # big loop
        for i in range(50):
            turtle.forward(i)
            turtle.left(15)


def make_spirals(my_turtle):
    odie.forward(10)
    for i in range(13):
        size = random.randint(1, 10)
        random_color(my_turtle)
        my_turtle.pensize(size)
        random_spirals(odie)


def make_flower(t, func):
    # Makes a flower by drawing circles
    petals = 7
    for i in range(petals):
        random_color(t)
        t.home()
        t.left(360/petals * i)
        t.forward(15)
        #circle(t)
        func(t)

if __name__ == '__main__':
    ## Set up our turtle
    odie = turtle.Turtle()
    odie.shape('turtle')
    odie.speed(0)
    odie.hideturtle()

    ## Make a starter circle
    # circle(odie)
    # odie.forward(10)

    ## Make some random spirals
    # make_spirals(odie)

    ## Make 1 spiral
    #spiral(odie)

    ## Make a flower
    make_flower(odie, spiral)
    make_flower(odie, circle)

    odie.showturtle()
    odie.home()
    print 'Thanks for watching!'
    turtle.exitonclick()