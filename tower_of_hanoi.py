from tkinter import *

main = Tk()
text1 = Label(main,text="Tower of Hanoi")

def updateGUI():
    plates = int(entry_plates.get())
    thickness = 100
    height = 50

    for i in range(plates):
     canvas.create_rectangle(200-thickness+i*10,990-i*50,200+thickness-i*10,990-height-i*50,fill="blue")


canvas = Canvas(main,width=1000,height=1000,bg="white")

# Base structure
canvas.create_rectangle(200,1000,210,400,fill="black")
canvas.create_rectangle(500,1000,510,400,fill="black")
canvas.create_rectangle(800,1000,810,400,fill="black")
canvas.create_rectangle(0,990,1000,1000,fill="black")

text2 = Label(main,text="Please enter amount of plates:")
entry_plates = Entry(main)
button = Button(main,text="confirm",command=updateGUI)

text1.pack()
text2.pack()
entry_plates.pack()
button.pack()
canvas.pack()
mainloop()