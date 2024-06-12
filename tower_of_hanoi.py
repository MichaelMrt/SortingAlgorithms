from tkinter import *

main = Tk()
text1 = Label(main,text="Tower of Hanoi")

def load_plates():
    global rect_a 
    global rect_b
    global rect_c
    global plates 
    rect_a = []
    rect_b = []
    rect_c = []

    plates = int(entry_plates.get())
    thickness = 100
    height = 50
    for i in range(plates):
     myrect= canvas.create_rectangle(200-thickness-(plates-i)*10,990-i*50,200+thickness+(plates-i)*10,990-height-i*50,fill="blue")
     rect_a.append(myrect)
     

def start_algorithm():
    global plates
    a = [1,[]]
    b = [2,[]]
    c = [3,[]]

    for i in range(plates):
       a[1].append(plates-i)

    move(plates,a,b,c)

def move(plates,a,b,c):
   if(plates>0):
      move(plates-1,a,c,b)
      c[1].append(a[1].pop())   
      updateGUI(a,b,c)
      move(plates-1,b,a,c)     


def draw_stacks(stack):
   global rect_a
   global rect_b
   global rect_c

   thickness = 100
   height = 50

   if(stack[0]==1):
      for i in range(len(stack[1])):
       x=200
       rect_a.append(canvas.create_rectangle(x-thickness-stack[1][i]*10,990-i*50,x+thickness+stack[1][i]*10,990-height-i*50,fill="blue"))

   if(stack[0]==2):
      for i in range(len(stack[1])):
       x=500
       rect_b.append(canvas.create_rectangle(x-thickness-stack[1][i]*10,990-i*50,x+thickness+stack[1][i]*10,990-height-i*50,fill="blue"))

   if(stack[0]==3):
      for i in range(len(stack[1])):
       x=800
       rect_c.append(canvas.create_rectangle(x-thickness-stack[1][i]*10,990-i*50,x+thickness+stack[1][i]*10,990-height-i*50,fill="blue"))
   


def updateGUI(a,b,c):
    global rect_a
    global rect_b
    global rect_c

    for rectangle in rect_a:
       canvas.delete(rectangle)

    for rectangle in rect_b:
       canvas.delete(rectangle)

    for rectangle in rect_c:
       canvas.delete(rectangle)

    stacks = [a,b,c]
    ordered_stacks = sorted(stacks,key=lambda x: x[0])

    for i in ordered_stacks:
       draw_stacks(i)

    main.after(1000,main.update())

canvas = Canvas(main,width=1000,height=1000,bg="white")

# Base structure
canvas.create_rectangle(200,1000,210,400,fill="black")
canvas.create_rectangle(500,1000,510,400,fill="black")
canvas.create_rectangle(800,1000,810,400,fill="black")
canvas.create_rectangle(0,990,1000,1000,fill="black")

text2 = Label(main,text="Please enter amount of plates:")
entry_plates = Entry(main)
button = Button(main,text="confirm",command=load_plates)
button2 = Button(main,text="start",command=start_algorithm)

text1.pack()
text2.pack()
entry_plates.pack()
button.pack()
button2.pack() 
canvas.pack()
mainloop()
