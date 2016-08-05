import tkinter
from random import randint, choice

ball_initial_number = 30
ball_min_radius = 15
ball_max_radius = 40
ball_available_colors = ['lightgreen', 'red', 'yellow', 'blue', 'white', '#FF00FF']


def click_ball(event):
    """
    Обработчик событий мышки игрового холста
    :param event: событие с координатами клика
    по клику мышкой нужно удалять объект, на который мышь указывает
    А также засчитывать его в очки
    """
    obj = canvas.find_closest(event.x, event.y)
    print(canvas.coords(obj))
    x1, y1, x2, y2 = canvas.coords(obj)
    if x1<event.x<x2 and y1<event.y<y2:
        canvas.delete(obj)
        # FIXME: нужно учесть объект в очках
        create_random_ball()

def move_all_balls(event):
    for obj in canvas.find_all():
        dx = randint(-2,2)
        dy = randint(-2,2)
        canvas.move(obj, dx, dy)

def create_random_ball():
    """
    Создает шарик в случайном месте игрового холста,
    при этом шарик не выходит за границы холста
    :return:
    """
    R = randint(ball_min_radius, ball_max_radius)
    x = randint(0, int(canvas['width'])-1-2*R)
    y = randint(0, int(canvas['height'])-1-2*R)
    canvas.create_oval(x, y, x+2*R, y+2*R, width=2, fill=random_color())

def random_color():
    """
    Возвращает случайный цвет из некоторого набора
    :return:
    """
    return choice(ball_available_colors)

def init_game():
    """
    Создает необходимое для игры количество шариков, по которым нужно кликать
    :return:
    """
    for i in range(ball_initial_number):
        create_random_ball()

def init_main_window():
    global root, canvas
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, background='orange', width=400, height=400)
    canvas.bind("<Button>", click_ball)
    canvas.bind("<Motion>", move_all_balls)
    canvas.pack()


if __name__ == "__main__":
    init_main_window()
    init_game()
    root.mainloop()
    print("Приходите еще!")