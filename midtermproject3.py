from tkinter import *
root=Tk()

root.title ("Weight Converter")
root.geometry ('500x300')
root.resizable(0,0)
root.config(bg="white")

label=Label(root,text="Enter Weight in LBs")
label.place(x=150,y=150)

label2=Label(root,text="KG:")
label2.place(x=150,y=50)

typingbox= Entry(root,width=10)
typingbox.place(x=350,y=150)

def button1clicked():
    if typingbox.get()
        res=*0.45
    lbl.configure(text=res)

button1=Button(root,text="submit",
        fg="white",command=clicked())
button1.place(x=250,y=50)


