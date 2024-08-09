from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import os
import cv2
import numpy as np
from time import strftime
from datetime import datetime
import tkinter


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1320x735")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="darkblue",fg="yellow")
        title_lbl.place(x=0,y=0,width=1400,height=50)

        # Back to Home Button
        back_button = Button(title_lbl,text="Exit",cursor="hand2",command=self.exit_page,font=("times new roman",15,"bold"),bg="silver",fg="green")
        back_button.place(x=1255,y=18,width=65,height=30)

        #left image
        img_top=Image.open(r"pictures/left_face_recognition.jpg")
        img_top=img_top.resize((630,685),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=630,height=685)

        # right image
        img_right=Image.open(r"pictures/scanning_face_recognition.jpg")
        img_right=img_right.resize((770,685),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(self.root,image=self.photoimg_right)
        f_lbl.place(x=630,y=50,width=770,height=685)

        # Button
        b2 = Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",16,"bold"),bg="darkgreen",fg="Aqua")
        b2.place(x=285,y=605,width=200,height=35)
        
    # ============================================== Attendence =====================================================4
    def mark_attendence(self,i,r,n,d):
        # print(n)
        # print(i)
        # print(r)
        # print(d)
        with open("attendence_sheet.csv","r+",newline="\n") as f:
            my_data_list = f.readlines()
            name_list= []
            for line in my_data_list:
                entry = line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dt_string = now.strftime("%H:%M:%S")
                f.writelines("\n"+i+","+r+","+n+","+d+","+f"{dt_string},{d1},Present")
                # print("\n"+i+","+r+","+n+","+d+","+f"{dt_string},{d1},Present")

    # ============================================= Face Recognition ===================================================
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                # print(id)
                conn=mysql.connector.connect(host="localhost",username="root",password="20022004",database="saurabhcs")
                my_cursor=conn.cursor()
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                # n = "+".join(n)
                n = str(n)
                n = n[2:-3] 
                # print(n)
                
                # For fetching Roll No.
                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                # r = "+".join(r)
                r = str(r)
                r = r[2:-3] 
                # print(r)

                # For fetching Department
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                # d = "+".join(d)
                d = str(d)
                d = d[2:-3] 
                
                # For fetching Student id
                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i = my_cursor.fetchone()
                # i = "+".join(i)
                i = str(i)
                i = i[2:-3] 

                if confidence > 77:
                    self.mark_attendence(i,r,n,d)
                    cv2.putText(img,"ID:"+i,(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,255),2)
                    cv2.putText(img,"Roll:"+r,(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(151,240,200),2)
                    cv2.putText(img,"Name:"+n,(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),2)
                    cv2.putText(img,"Department:"+d,(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,185,125),2)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown Person Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)

                coord=[x,y,w,h]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

    def exit_page(self):
            self.exit_page = tkinter.messagebox.askyesno("Face Recognition System","Are you sure exit this page",parent=self.root)
            if self.exit_page > 0:
                self.root.destroy()
            else:
                return

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()