from tkinter import *
import tkinter
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
import os
from time import strftime
from datetime import datetime

#  import module pages
from Student import student
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence
from developer import Developer
from help import Help_Desk

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1320x735")
        self.root.title("Face Recognition System")
        
        #first image
        img = Image.open(r"pictures/up_left_main.jpg")
        img = img.resize((440,150),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img) 
        
        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width=440,height=150)
        
        #second image
        img1 = Image.open(r"pictures/up_mid_main.jpg")
        img1 = img1.resize((440,150),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1) 
       
        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=440,y=0,width=440,height=150)
        
        #third image
        img2 = Image.open(r"pictures/up_right_main1.jpg")
        img2 = img2.resize((440,135),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2) 
        
        f_lbl = Label(self.root,image = self.photoimg2)
        f_lbl.place(x=880,y=0,width=440,height=135)
        
        #bg image
        img4 = Image.open(r"pictures/down_main_background.jpg")
        img4 = img4.resize((1730,620))
        self.photoimg4 = ImageTk.PhotoImage(img4) 
        
        bg_img = Label(self.root,image = self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=45)

        # ==================================== time ======================================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)
        
        lbl = Label(title_lbl, font=('time new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=10,y=0,width=150,height=45)
        time()

        #student button
        img5 = Image.open(r"pictures/button.jpg")
        img5 = img5.resize((220,190))
        self.photoimg5 = ImageTk.PhotoImage(img5)
          
        b1 = Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=90,width=220,height=190)
        
        b2 = Button(bg_img,text="Student Details",cursor="hand2",command=self.student_details,font=("times new roman",15,"bold"),bg="darkblue",fg="Aqua")
        b2.place(x=100,y=280,width=220,height=35)
        
        #Detect face button
        img6 = Image.open(r"pictures/facescan.jpg")
        img6 = img6.resize((220,190))
        self.photoimg6 = ImageTk.PhotoImage(img6)
          
        b1 = Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=90,width=220,height=190)
        
        b2 = Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="Aqua")
        b2.place(x=400,y=280,width=220,height=35)
        
        # Attandence face button
        img7 = Image.open(r"pictures/att.jpg")
        img7 = img7.resize((220,190))
        self.photoimg7 = ImageTk.PhotoImage(img7)
          
        b1 = Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendence_data)
        b1.place(x=700,y=90,width=220,height=190)
        
        b2 = Button(bg_img,text="Attandence",cursor="hand2",command=self.attendence_data,font=("times new roman",15,"bold"),bg="darkblue",fg="Aqua")
        b2.place(x=700,y=280,width=220,height=35)
        
        # Help face button
        img8 = Image.open(r"pictures/help.jpg")
        img8 = img8.resize((220,190))
        self.photoimg8 = ImageTk.PhotoImage(img8)
          
        b1 = Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.help_data)
        b1.place(x=1000,y=90,width=220,height=190)
        
        b2 = Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="Aqua")
        b2.place(x=1000,y=280,width=220,height=35)
        
        # Train face button
        img9 = Image.open(r"pictures/train.jpeg")
        img9 = img9.resize((220,185))
        self.photoimg9 = ImageTk.PhotoImage(img9)
          
        b1 = Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=350,width=220,height=185)
        
        b2 = Button(bg_img,text="Train",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="Aqua")
        b2.place(x=100,y=535,width=220,height=35)
        
        # Photo face button
        img10 = Image.open(r"pictures/photo.jpeg")
        img10 = img10.resize((220,185))
        self.photoimg10 = ImageTk.PhotoImage(img10)
          
        b1 = Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=350,width=220,height=185)
        
        b2 = Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="Aqua")
        b2.place(x=400,y=535,width=220,height=35)
        
        # Developer face button
        img11 = Image.open(r"pictures/developer.jpg")
        img11 = img11.resize((220,185))
        self.photoimg11 = ImageTk.PhotoImage(img11)
          
        b1 = Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=350,width=220,height=185)
        
        b2 = Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="Aqua")
        b2.place(x=700,y=535,width=220,height=35)
        
        # Exit face button
        img12 = Image.open(r"pictures/exit.jpg")
        img12 = img12.resize((220,210))
        self.photoimg12 = ImageTk.PhotoImage(img12)
          
        b1 = Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.exit_page)
        b1.place(x=1000,y=350,width=220,height=185)
        
        b2 = Button(bg_img,text="Exit",cursor="hand2",command=self.exit_page,font=("times new roman",15,"bold"),bg="darkblue",fg="Aqua")
        b2.place(x=1000,y=535,width=220,height=35)
        

        #==================Function Buttons=========================
          
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)
           
    def open_img(self):
        os.startfile('data')

    def exit_page(self):
        self.exit_page = tkinter.messagebox.askyesno("Face Recognition Attendence System","Are you sure exit this Project",parent=self.root)
        if self.exit_page > 0:
            self.root.destroy()
        else:
            return
          
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendence_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help_Desk(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop() 