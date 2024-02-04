from tkinter import*
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk
import os
from stegano import lsb #pip install stegano

root = Tk() # Windows Create
root.title("Steganography -Hide a secret massage") # Windows Title 
root.geometry("650x460+150+180") # Size of windows
root.resizable(False,False) # Not change windows size on runing code
root.configure(bg="#2f4155") # Windows display color

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title='Select Image File',
                                          filetype=(("PNG file","*.png"),
                                                    ("JPG file","*.jpg"),("All file","*.txt")))
    
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=230,height=220)
    lbl.image = img

def Hide():
    global secret
    massege = text1.get(1.0,END)
    secret = lsb.hide(str(filename), massege)

def Show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)

def save():
    secret.save("save.png")


# Icon
image_icon = PhotoImage(file="image/pic.jpg")
root.iconphoto(False,image_icon)

# Logo
logo = PhotoImage(file="image/logo.png")
Label(root,image=logo,bg="#2f4155").place(x=10,y=0)

# Icon side Text
Label(root,text="CYBER SCIENCE", bg="#2f4155", fg="white" ,font="arial 20 bold").place(x=100,y=20)

# First Frame
f = Frame(root, bd=3, bg="black", width=310, height=250, relief=GROOVE)
f.place(x=9,y=80)

lbl = Label(f,bg="black")
lbl.place(x=40,y=10)

# Second Frame
frame2 = Frame(root,bd=2, width=320, height=250, relief=GROOVE)
frame2.place(x=320,y=80)

text1 = Text(frame2,font="Robote 15", bg="White", fg="Black", relief=GROOVE)
text1.place(x=0,y=0,width=320,height=290)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320,y=0, height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Thired Frame
frame3 = Frame(root,bd=3, bg="#2f4155", width=310, height=100, relief=GROOVE)
frame3.place(x=10,y=350)

Button(frame3,text="Open Image",width=9,height=2,font="arial 14 bold",command=showimage).place(x=20,y=30)
Button(frame3,text="Save Image",width=9,height=2,font="arial 14 bold",command=save).place(x=180,y=30)
Label(frame3,text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20,y=5)

# Fourth Frame
frame4 = Frame(root,bd=3, bg="#2f4155", width=310, height=100, relief=GROOVE)
frame4.place(x=320,y=350)

Button(frame4,text="Hide Data",width=9,height=2,font="arial 14 bold",command=Hide).place(x=20,y=30)
Button(frame4,text="Show Data",width=9,height=2,font="arial 14 bold",command=Show).place(x=180,y=30)
Label(frame4,text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20,y=5)

root.mainloop()
