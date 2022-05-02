import tkinter as tk
from tkinter.ttk import *
import pandas as pd
from PIL import Image, ImageTk
root=tk.Tk()

root.title ("CSUMB APP")
root.geometry ('1000x1000')
root.resizable(0,0)
root.config(bg="light blue")

picture = Image.open("midtermlogo.PNG")
resizedpicture = picture.resize((100,100),Image.ANTIALIAS)
resizedpicture1 = ImageTk.PhotoImage(resizedpicture)
label= Label(root, image=resizedpicture1)
label.place (x=800, y=50)

def cat():
    data=pd.read_excel("exam1.xlsx")
    df=pd.DataFrame(data, columns=['CalendarDate'])
    lb.config(text=df)
b1=tk.Button(text="Calender", font=("Arial",15), bg="#CAFF70", command=cat)
b1.place(x=200, y=400)
lb=tk.Label(font=("Arial",10),text="", justify="left")
lb.place(x=300, y=500)

def cat2():
    data=pd.read_excel("exam1.xlsx")
    df=pd.DataFrame(data, columns=['Buildings'])
    lb.config(text=df)
b1=tk.Button(text="Buildings", font=("Arial",15), bg="#CAFF70", command=cat2)
b1.place(x=400, y=400)
lb=tk.Label(font=("Arial",10),text="", justify="left")
lb.place(x=300, y=500)

def cat3():
    data=pd.read_excel("exam1.xlsx")
    df=pd.DataFrame(data, columns=['FacultyName'])
    lb.config(text=df)
b1=tk.Button(text="Faculty", font=("Arial",15), bg="#CAFF70", command=cat3)
b1.place(x=600, y=400)
lb=tk.Label(font=("Arial",10),text="", justify="left")
lb.place(x=300, y=500)

tk.mainloop()