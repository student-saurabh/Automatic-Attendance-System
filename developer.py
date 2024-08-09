from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import cv2
import webbrowser

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x720")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="DEVELOPER  DETAILS",font=("times new roman",35,"bold"),bg="lightgrey",fg="dark red")
        title_lbl.place(x=0,y=0,width=1350,height=50)

        # background image
        img_top=Image.open(r"pictures/dev2.jpg")
        img_top=img_top.resize((1350,670),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1350,height=670)

        # developer info frame
        main_frame=Frame(f_lbl,bd=2,bg="lavender")
        main_frame.place(x=850,y=7,width=490,height=630)

        # Saurabh Kuamar info
        saurabh_img=Image.open(r"pictures/saurabh.jpg")
        saurabh_img=saurabh_img.resize((170,170),Image.Resampling.LANCZOS)
        self.saurabh=ImageTk.PhotoImage(saurabh_img)
        
        f_lbl=Label(main_frame,image=self.saurabh)
        f_lbl.place(x=320,y=0,width=170,height=170)

        #info label
        info_main_frame=Frame(main_frame,bd=2,bg="lavender")
        info_main_frame.place(x=0,y=10,width=320,height=170)
        line1_label=Label(info_main_frame,text='''Hello, I am Saurabh Kumar''',font=("times new roman",18,"bold"),bg="lavender")
        line1_label.grid(row=0,column=0,padx=10,sticky=W)

        info_main_frame2=Frame(main_frame,bd=2,bg="lavender")
        info_main_frame2.place(x=0,y=40,width=320,height=170)
        line2_label=Label(info_main_frame2,text='''BCA(Appearing) from TMU, Moradabad''',font=("times new roman",13,),bg="lavender")
        line2_label.grid(row=0,column=0,padx=10,sticky=W)

        info_main_frame3=Frame(main_frame,bd=2,bg="lavender")
        info_main_frame3.place(x=0,y=80,width=320,height=170)
        line3_label=Label(info_main_frame3,text='''Email : ''',font=("times new roman",14,),bg="lavender")
        line3_label.grid(row=0,column=0,padx=10,sticky=W)

        # Add a link to the image
        link_url = "saurabh.039222@tmu.ac.in"  # Replace with your desired URL
        link_label = Label(root, text="saurabh.039222@tmu.ac.in", fg="blue", cursor="hand2",background="lavender",font=(14,))
        link_label.bind("<Button-1>", lambda e: webbrowser.open(link_url))
        link_label.place(x=928, y=144)  # Adjust the position as needed

        info_main_frame4=Frame(main_frame,bd=2,bg="lavender")
        info_main_frame4.place(x=0,y=105,width=320,height=170)
        line4_label=Label(info_main_frame4,text='''LinkedIn : ''',font=("times new roman",14,),bg="lavender")
        line4_label.grid(row=0,column=0,padx=10,sticky=W)

        # Add a link to the image
        link_url = "https://www.linkedin.com/in/saurabh-kumar-13aa20246"  # Replace with your desired URL
        link_label = Label(root, text="Click here", fg="blue", cursor="hand2",background="lavender",font=(14,))
        link_label.bind("<Button-1>", lambda e: webbrowser.open(link_url))
        link_label.place(x=950, y=169)  # Adjust the position as needed


        bottom_img=Image.open(r"pictures/dev8.jpeg")
        bottom_img=bottom_img.resize((550,370),Image.Resampling.LANCZOS)
        self.bottom=ImageTk.PhotoImage(bottom_img)
        
        f_lbl=Label(main_frame,image=self.bottom)
        f_lbl.place(x=0,y=330,width=550,height=300)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
