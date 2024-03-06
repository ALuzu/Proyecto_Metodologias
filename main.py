from tkinter import *

window = Tk()
window.title("Software")
window.minsize(width=500, height=450)

canvas = Canvas(width=300, height=300)
canvas.grid(column=1, row=0)

window.mainloop()