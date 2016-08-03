import tkinter

def paint(event):
    """
    Обработчик событий для холста
    :param event:
    :return:
    """
    print(event.x, event.y)
    if event.widget != canvas:
        print ("Странно)")
        return
    canvas.coords(line, 0, 0, event.x, event.y)


root = tkinter.Tk()

canvas = tkinter.Canvas(root, background='orange', width=400, height=400)
canvas.bind("<Motion>", paint)
canvas.pack()

line = canvas.create_line(0, 0, 10, 10)
for i in range (10):
    canvas.create_oval(i*40, i*40,i*40-20, i*40+20, fill="green")

root.mainloop()
print("Эта строка будет достигнута при выходе")