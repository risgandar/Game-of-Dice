from tkinter import *
import random, time

def bros():
    x=random.choice(['b1.png','b2.png',
    'b3.png','b4.png','b5.png','b6.png'])
    return x

def img(event):
    b1= PhotoImage (file=(bros()))
    b2= PhotoImage (file=(bros()))
    lab1 ['image']=b1
    lab2 ['image']=b2
    root.update()
    time.sleep(0.12)

root=Tk()
root.geometry('400x200')
root.title('Dices.Make a move!')
root.resizable(height=False, width=False)
root.iconphoto(True, Photoimage(file=('iconka.png')))
font = PhotoImage(file=('holst.png'))
Label(root, image=font).pack()
lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)
lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)
Button(root, text='Move', command=img).pack()
root.bind('<1>', img)
img('event')
root.mainloop()
#read me