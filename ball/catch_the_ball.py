import tkinter

def click_ball(event):
    """
    Обработчик событий мышки игрового холста
    :param event: событие с координатами клика
    :return:
    """

    # event.x, event.y)

def create_random_ball():
    canvas.create_oval(x, y, x+2*R, y+2*R, width=2, fill=random_color())


root = tkinter.Tk()

canvas = tkinter.Canvas(root, background='orange', width=400, height=400)
canvas.bind("<Motion>", paint)
canvas.pack()



root.mainloop()
print("Эта строка будет достигнута при выходе")