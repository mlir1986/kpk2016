from turtle import Turtle

def init_drawman():
    global t, x_current, y_current, dm_scale
    t=Turtle()
    t.penup()
    x_current=0
    y_current=0
    t.goto(x_current, y_current)
    dm_scale = 10


def test_drawman():
    """
    Тестирование работы Чертежника
    :return: none
    """
    pen_down()
    for i in range(5):
        on_vector(10,20)
        on_vector(0,-20)
    pen_up()
    to_point(0,0)


def pen_down():
    t.pendown()

def pen_up():
    t.penup()

def on_vector(dx,dy):
    to_point(x_current + dx, y_current + dy)

def to_point(x,y):
    global x_current, y_current
    x_current = x
    y_current = y
    t.goto(dm_scale*x,dm_scale*y)

init_drawman()
if __name__ == '__main__':
    import time
    test_drawman()
    time.sleep(10)