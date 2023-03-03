from tkinter import*
# root =Tk()
# root.mainloop()
p= Tk()
p.geometry("440x550+400+80")
p.maxsize(width=600,height=450)
p.title("priyo")
p.configure(bg = "pink")
def show():
    a1 =c.get()
    c.delete(0,END)
    c.insert(0,a1)
def erase():
    d.delete(0,END)    


# Entry box
c = Entry(p,font = 8,fg="Navy",bg = "white",borderwidth=2)
c.place(x=115,y=100,width=200,height=30)
d = Label(p,text="Name",font=8,fg="black",bg="white")
d.place(x=150,y=120)
b1 = Button(p,text="Copy",font = 6,bg ="white",fg="black",command=show)
b1.place(x=250,y=280,width=200,height=30)
b2 = Button(p,text="Clear Name",font = 6,bg ="white",fg="black",command=erase)
b2.place(x=115,y=150,width=200,height=30)


p.mainloop()