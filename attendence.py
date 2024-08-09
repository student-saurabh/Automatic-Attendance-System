from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import cv2
import os
import csv
from tkinter import filedialog
from time import strftime
from datetime import datetime
import tkinter

mydata=[]
class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1370x730")
        self.root.title("Face Recognition System")

        # ================================== Variables ==================================
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendence = StringVar()

        #first image
        img = Image.open(r"pictures/up_left_attendence.jpg")
        img = img.resize((465,150),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img) 
        
        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width=465,height=150)
        
        #second image
        img1 = Image.open(r"pictures/up_mid_attendence.jpg")
        img1 = img1.resize((470,150),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1) 
       
        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=465,y=0,width=470,height=150)
        
        #third image
        img2 = Image.open(r"pictures/up_right_attendence1.png")
        img2 = img2.resize((465,135),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2) 
        
        f_lbl = Label(self.root,image = self.photoimg2)
        f_lbl.place(x=935,y=0,width=465,height=135)
        
        #bg image
        img4 = Image.open(r"pictures/down_main_background1.jpg")
        img4 = img4.resize((2000,620))
        self.photoimg4 = ImageTk.PhotoImage(img4) 
        
        bg_img = Label(self.root,image = self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl = Label(bg_img,text="STUDENT ATTENDENCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1400,height=45)

        # Back to Home Button
        back_button = Button(title_lbl,text="Exit",cursor="hand2",command=self.exit_page,font=("times new roman",15,"bold"),bg="white",fg="red")
        back_button.place(x=1290,y=14,width=65,height=30)

        # ==================================== time ======================================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)
        
        lbl = Label(title_lbl, font=('time new roman',14,'bold'),background='white',foreground='purple')
        lbl.place(x=5,y=0,width=115,height=40)
        time()

        main_frame=Frame(bg_img,bd=2,bg="silver")
        main_frame.place(x=0,y=55,width=1400,height=600)

        #left label frame         
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendence Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=5,y=5,width=740,height=525)

        img_left=Image.open(r"pictures/Students.jpg")
        img_left=img_left.resize((725,150),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=725,height=150)

        left_inside_frame=Frame(Left_frame,bd=2,bg="light grey")
        left_inside_frame.place(x=5,y=155,width=725,height=365)

        # Labels and Entry
        # attendence id
        attendence_ID_label=Label(left_inside_frame ,text="    Attendence ID:",font=("times new roman",13,"bold"),bg="light grey")
        attendence_ID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendence_ID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendence_ID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Roll
        rollLabel=Label(left_inside_frame, text="Roll:", bg="light grey", font="comicsansns 11 bold")
        rollLabel.grid(row=0,column=2, padx=4, pady=8)
        atten_roll=ttk.Entry(left_inside_frame, width=22,textvariable=self.var_atten_roll, font="comicsansns 11 bold")
        atten_roll.grid(row=0,column=3, pady=8)

        # Name
        nameLabel=Label(left_inside_frame, text="Name:",bg="light grey", font="comicsansns 11 bold")
        nameLabel.grid(row=1,column=0)
        atten_name=ttk.Entry(left_inside_frame, width=22,textvariable=self.var_atten_name, font="comicsansns 11 bold")
        atten_name.grid(row=1,column=1, pady=8)

        # Department
        depLabel=Label(left_inside_frame, text="    Department:    ", bg="light grey", font="comicsansns 11 bold")
        depLabel.grid(row=1,column=2)
        atten_dep=ttk.Entry(left_inside_frame, width=22,textvariable=self.var_atten_dep, font="comicsansns 11 bold")
        atten_dep.grid(row=1,column=3, pady=8)

        # time
        timeLabel=Label(left_inside_frame, text="Time:",bg="light grey", font="comicsansns 11 bold")
        timeLabel.grid(row=2,column=0)
        atten_time=ttk.Entry(left_inside_frame, width=22,textvariable=self.var_atten_time, font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1, pady=8)

        # Date
        dateLabel=Label(left_inside_frame, text="Date:",bg="light grey", font="comicsansns 11 bold")
        dateLabel.grid(row=2,column=2)
        atten_date=ttk.Entry(left_inside_frame, width=22,textvariable=self.var_atten_date, font="comicsansns 11 bold")
        atten_date.grid(row=2,column=3, pady=8)

        # attendance
        attendanceLabel=Label(left_inside_frame, text="    Attendance Status: ", bg="light grey", font="comicsansns 11 bold")
        attendanceLabel.grid(row=3,column=0)
        self.atten_status=ttk.Combobox(left_inside_frame, width=20,textvariable=self.var_atten_attendence, font="comicsansns 11 bold", state="readonly")
        self.atten_status ["values"]=("Status", "Present", "Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="light grey")
        btn_frame.place(x=2.5,y=250,width=715,height=35)
        
        save_btn=Button(btn_frame,text="Import CSV",command=self.import_csv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Export CSV",command=self.export_csv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        #Right label frame         
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=5,width=605,height=525)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="grey")
        table_frame.place(x=5,y=5,width=595,height=495)

        # ================================== Scroll Bar table ================================
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendenceReportTable = ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id",text="Attendence ID")
        self.AttendenceReportTable.heading("roll",text="Roll")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text="Department")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text="Attendence")

        self.AttendenceReportTable["show"]="headings"
        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll",width=100)
        self.AttendenceReportTable.column("name",width=100)
        self.AttendenceReportTable.column("department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendence",width=100)

        self.AttendenceReportTable.pack(fill=BOTH,expand=1)
        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # ====================================  Fetch Data ===================================
    def fetch_data(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)
    # import csv
    def import_csv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    def export_csv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(fln,"w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported","Your Data Exported to "+os.path.basename(fln)+" Successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row = self.AttendenceReportTable.focus()
        content = self.AttendenceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendence.set(rows[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendence.set("")

    def exit_page(self):
            self.exit_page = tkinter.messagebox.askyesno("STUDENT ATTENDENCE MANAGEMENT SYSTEM","Are you sure exit this page",parent=self.root)
            if self.exit_page > 0:
                self.root.destroy()
            else:
                return 

if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()