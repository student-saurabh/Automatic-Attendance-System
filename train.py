from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import os
import cv2
import numpy as np
import tkinter


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1320x735")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="lightgrey",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=50)

        # Back to Home Button
        back_button = Button(title_lbl,text="Exit",cursor="hand2",command=self.exit_page,font=("times new roman",15,"bold"),bg="silver",fg="darkblue")
        back_button.place(x=1255,y=18,width=65,height=30)

        # top left image
        img_top=Image.open(r"pictures/left_face_train_data2.jpg")
        img_top=img_top.resize((440,250),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=440,height=250)

        # top mid image
        img_mid=Image.open(r"pictures/mid_face_train_data.jpg")
        img_mid=img_mid.resize((440,250),Image.Resampling.LANCZOS)
        self.photoimg_mid=ImageTk.PhotoImage(img_mid)
        
        f_lbl=Label(self.root,image=self.photoimg_mid)
        f_lbl.place(x=440,y=50,width=440,height=250)

        # top right image
        img_right=Image.open(r"pictures/r_face_train_data.jpg")
        img_right=img_right.resize((440,250),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(self.root,image=self.photoimg_right)
        f_lbl.place(x=880,y=50,width=440,height=250)
        
        # Button
        b2 = Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),bg="darkblue",fg="Aqua")
        b2.place(x=0,y=300,width=1320,height=50)

        # top right image
        img_down=Image.open(r"pictures/down_train_data.jpg")
        img_down=img_down.resize((1320,435),Image.Resampling.LANCZOS)
        self.photoimg_down=ImageTk.PhotoImage(img_down)
        
        f_lbl=Label(self.root,image=self.photoimg_down)
        f_lbl.place(x=0,y=350,width=1320,height=435)
         

    def train_classifier(self):
        data_dir = ('data')
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []
        for image in path:
            img=Image.open(image).convert('L') # Gray sclae image
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)

        # ========================== Train the Classifier and Save =================================
        clf = cv2.face.LBPHFaceRecognizer_create()
        # clf = cv2.face.LBPHFaceRecognizer()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed!!")

    def exit_page(self):
        self.exit_page = tkinter.messagebox.askyesno("TRAIN DATA SET","Are you sure exit this page",parent=self.root)
        if self.exit_page > 0:
            self.root.destroy()
        else:
            return

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()