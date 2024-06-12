from tkinter import *

main = Tk()
text1 = Label(main,text="Tower of Hanoi")

canvas = Canvas(main,width=1000,height=1000,bg="white")

# Base structure
canvas.create_rectangle(200,1000,210,400,fill="black")
canvas.create_rectangle(500,1000,510,400,fill="black")
canvas.create_rectangle(800,1000,810,400,fill="black")
canvas.create_rectangle(0,990,1000,1000,fill="black")


text1.pack()
canvas.pack()
mainloop()