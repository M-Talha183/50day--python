from tkinter import Tk ,Label,Button
from tkinter.messagebox import showinfo
def func():
  showinfo(message="Hello world ")

r= Tk()
b=Button(r,text="click it !",command=func)
b.pack()
r.mainloop()