from tkinter import *
root = Tk()
root.title("main")
root.geometry("200x300")
def topwindow():
    top = Toplevel()
    top.geometry("120x100")
    top.title("top level  ")
    l1= Label (top,text = " This is the top level  window ")
    l1.pack()
    top.mainloop()
l2 = Label(root,text= "this is root level window")
l2.pack()
b1=Button(root,text="click to open the top level window",command=topwindow)
b1.pack()
root.mainloop()


