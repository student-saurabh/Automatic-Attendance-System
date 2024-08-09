from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import cv2
import webbrowser

class Help_Desk:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x720")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="light grey",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        # Load the image
        img_top2 = Image.open(r"pictures/help2.jpeg")
        img_top2 = img_top2.resize((580, 670), Image.Resampling.LANCZOS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)

        # Create a label with the image
        f_lbl_up = Label(root, image=self.photoimg_top2)
        f_lbl_up.place(x=360, y=50, width=580, height=670)

        # Add a link to the image
        link_url = "saurabh.039222@tmu.ac.in"  # Replace with your desired URL
        link_label = Label(root, text="saurabh.039222@tmu.ac.in", fg="blue", cursor="hand2")
        link_label.bind("<Button-1>", lambda e: webbrowser.open(link_url))
        link_label.place(x=635, y=318)  # Adjust the position as needed
''' 
        # Add a link to the image
        link_url = "himanshu.036061@tmu.ac.in"  # Replace with your desired URL
        link_label = Label(root, text="himanshu.036061@tmu.ac.in", fg="blue", cursor="hand2")
        link_label.bind("<Button-1>", lambda e: webbrowser.open(link_url))
        link_label.place(x=635, y=318)  # Adjust the position as needed

        # Add a link to the image
        link_url = "yagyansh.039406@tmu.ac.in"  # Replace with your desired URL
        link_label = Label(root, text="yagyansh.039406@tmu.ac.in", fg="blue", cursor="hand2")
        link_label.bind("<Button-1>", lambda e: webbrowser.open(link_url))
        link_label.place(x=635, y=345)  # Adjust the position as needed

'''

if __name__ == "__main__":
    root = Tk()
    obj = Help_Desk(root)
    root.mainloop()