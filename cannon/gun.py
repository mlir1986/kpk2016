from tkinter import *
from random import randint, choice

timer_delay = 100
screen_width = 400
screen_height = 400


class Ball:
    initial_number = 30
    min_radius = 15
    max_radius = 40
    available_colors = ['lightgreen', 'red', 'yellow', 'blue', 'white', '#FF00FF']

    def __init__(self):
        """
        Создание шарика в случайном месте игрового холста,
    при этом шарик не выходит за границы холста
        :return:
        """
        R = randint(Ball.min_radius, Ball.max_radius)
        x = randint(0, screen_width-1-2*R)
        y = randint(0, screen_height-1-2*R)
        self._R = R
        self._x = x
        self._y = y
        fillcolor = choice(Ball.available_colors)
        self._avatar = canvas.create_oval(x, y, x+2*R, y+2*R, width=2, fill=fillcolor)
        self._Vx = randint(-3, 3)
        self._Vy = randint(-3, 3)

    def fly(self):
        self._x += self._Vx
        self._y += self._Vy
        #отбиваемся от горизонтальных стенок
        if self._x < 0:
            self._x = 0
            self._Vx = -self._Vx
        elif self._x + 2*self._R >= screen_width:
            self._x = screen_width - 1 - 2*self._R
            self._Vx = -self._Vx
        #отбиваемся от вертикальных стенок
        if self._y < 0:
            self._y = 0
            self._Vy = -self._Vy
        elif self._y + 2*self._R >= screen_height:
            self._y = screen_height - 1 - 2*self._R
            self._Vy = -self._Vy
        canvas.coords(self._avatar, self._x, self._y, self._x + 2*self._R, self._y + 2*self._R)

class Gun:
    def __init__(self):
        x = 0
        y = screen_height - 1
        lx = 30
        ly = -30
        self._x = 0
        self._y = screen_height - 1
        self._lx = 30
        self._ly = -30
        self._avatar = canvas.create_line(self._x, self._y, self._x + self._lx,
                                          self._y + self._ly)

    def shoot(self):
        """
        :return: возвращает объект снаряда класса Ball
        """
        shell = Ball()
        shell._x = self._x + self._lx
        shell._y = self._y + self._ly
        shell._Vx = self._lx/15
        shell._Vy = self._ly/15
        shell.fly()
        shell._R = 5
        return shell


def init_game():
    """
    Создаем необходимое количество объектов-шариков, и объект-пушку
    :return:
    """
    global balls, gun, shells_on_fly
    balls = [Ball() for i in range (Ball.initial_number)]
    shells_on_fly = []
    gun = Gun()

def timer_event():
    #print('Tic-Tock')
    #все периодические подсчеты делаются здесь
    for ball in balls:
        ball.fly()
    for shell in shells_on_fly:
        shell.fly()
    canvas.after(timer_delay, timer_event)

def click_event_handler(event):
    global shells_on_fly
    shell = gun.shoot()
    shells_on_fly.append(shell)

def init_main_window():
    global root, canvas, score_text, score_value
    root = Tk()
    root.title("Пушка")
    score_value = IntVar()
    canvas = Canvas(root, background='orange', width=screen_width, height=screen_height)
    score_text = Entry(root,textvariable=score_value)
    canvas.grid(row=1, column=0, columnspan=3)
    score_text.grid(row=0, column=2)
    canvas.bind('<Button-1>', click_event_handler)
    #FIXME

if __name__ == "__main__":
    init_main_window()
    init_game()
    timer_event()
    root.mainloop()
    print("Приходите еще!")