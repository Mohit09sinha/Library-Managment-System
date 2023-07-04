from msilib.schema import ListBox
from multiprocessing import parent_process
from multiprocessing.sharedctypes import Value
from operator import ge
from sqlite3 import connect
from tkinter import*
from tkinter import ttk
from turtle import width
from webbrowser import get
import mysql.connector
from mysqlx import Column
from tkinter import messagebox
import datetime
import tkinter

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Managment System")
        self.root.geometry("1550x800+0+0")
        
        
        # -------------------VARIABLES---------------------------------
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()
        
        
        
        
        
        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)
        
        # --------------------DATA FRAME LEFT---------------------------------
        
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",14,"bold"))
        DataFrameLeft.place(x=0,y=5,width=860,height=350)
        
        lblMember=Label(DataFrameLeft,text="Member Type:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)
        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("arial",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)
        
        lblPRN_No=Label(DataFrameLeft,text="PRN_Number:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_No.grid(row=1,column=1)
        
        lblTitle=Label(DataFrameLeft,text="Title:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)
        
        lblFirstName=Label(DataFrameLeft,text="First Name",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)
        
        
        
        lblLastName=Label(DataFrameLeft,text="Last Name",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)
        
        lblAddress1=Label(DataFrameLeft,text="Address 1",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)
        lblAddress2=Label(DataFrameLeft,text="Address 2",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)
        
        lblPostcode=Label(DataFrameLeft,text="Post Code",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblPostcode.grid(row=7,column=0,sticky=W)
        txtPostcode=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postcode_var,width=29)
        txtPostcode.grid(row=7,column=1)
        lblMobile=Label(DataFrameLeft,text="Mobile Number",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)
        
        lblBookId=Label(DataFrameLeft,text="Book ID:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.bookid_var,width=29)
        txtBookId.grid(row=0,column=3)
        
        
        lblBookTitle=Label(DataFrameLeft,text="Book Title:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)
        lblAuther=Label(DataFrameLeft,text="Author Name:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblAuther.grid(row=2,column=2,sticky=W)
        txtAuther=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.auther_var,width=29)
        txtAuther.grid(row=2,column=3)
        lblDateBorrowed=Label(DataFrameLeft,text="Date Borrowed:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=3,column=3,sticky=W)
        lblDateDue=Label(DataFrameLeft,text="Date Due:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=4,column=3,sticky=W)
        lblDaysOnBook=Label(DataFrameLeft,text="Days On Book:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.daysonbook_var,width=29)
        txtDaysOnBook.grid(row=5,column=3)
        lblLateReturnFine=Label(DataFrameLeft,text="Late Return Fine:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lateratefine_var,width=29)
        txtLateReturnFine.grid(row=6,column=3)
        
        
        lblDateOverDue=Label(DataFrameLeft,text="Date Over Due:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.dateoverdue_var,width=29)
        txtDateOverDue.grid(row=7,column=3)
        lblActualPrice=Label(DataFrameLeft,text="Actual Price:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.finalprice_var,width=29)
        txtActualPrice.grid(row=8,column=3)
        
        
        # --------------------DATA FRAME RIGHT---------------------------------
        
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",14,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)
        
        self.txtBox=Text(DataFrameRight,font=("times new roman",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
        
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
        
        listBooks=['Head First Book','Learn Python The Hard Way','Python Programming','Secrete Rahshy','Python CookBook','Intro To Machine Learning','Fluent Python','Machine Techno','My Python','Joss Ellif Guru','Elite Jungle Python','C Programming','C++ Introduction','Java','Machine Python','Advance Python','Anaconda','Tkinter','Database','Sqlite','My Coding']
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if(x=='Head First Book'):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Paul Berry")
          
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs 788")
        
            elif(x=='Learn Python The Hard Way'):
                self.bookid_var.set("BKID5455")
                self.booktitle_var.set("Basic Of Python")
                self.auther_var.set("Zed A.Shaw")
          
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs 25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs 725")
            
            elif(x=='Python Programming'):
                self.bookid_var.set("BKID5456")
                self.booktitle_var.set("Intro To Python Comp. Science")
                self.auther_var.set("John Zhelle")
          
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs 25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs 500")
            
            elif(x=='Secrete Rahshy'):
                self.bookid_var.set("BKID5457")
                self.booktitle_var.set("Secret Behind Life")
                self.auther_var.set("John Snow")
          
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs 75")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs 550")
            
            elif(x=='Python CookBook'):
                self.bookid_var.set("BKID5458")
                self.booktitle_var.set("Python Codebook")
                self.auther_var.set("David Snow")
          
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs 35")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs 450")
            
            
            
            
            
            elif(x=='Intro To Machine Learning'):
                self.bookid_var.set("BKID5459")
                self.booktitle_var.set("Introduction To Machine Learning")
                self.auther_var.set("Helly Berry")
          
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs 100")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs 888")
        
            elif(x=='Fluent Python'):
                self.bookid_var.set("BKID5460")
                self.booktitle_var.set("Fluency In Python")
                self.auther_var.set("Jolly Johnson")
          
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(45)
                self.lateratefine_var.set("Rs 200")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs 1000")
        
            elif(x=='Machine Techno'):
                self.bookid_var.set("BKID5461")
                self.booktitle_var.set("Introduction To Machine Technology")
                self.auther_var.set("Helly Berry")
          
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs 988")
        
            elif(x=='My Python'):
                self.bookid_var.set("BKID5462")
                self.booktitle_var.set("Enhancing Python Learning")
                self.auther_var.set("David Cameron")
          
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs 450")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs 1040")
        
            elif(x=='Joss Ellif Guru'):
                self.bookid_var.set("BKID5463")
                self.booktitle_var.set("Our Precious Life")
                self.auther_var.set("Joss Ellif")
          
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs 400")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs 2000")
        
            elif(x=='Elite Jungle Python'):
                self.bookid_var.set("BKID5464")
                self.booktitle_var.set("Introduction To Jungle World")
                self.auther_var.set("John John")
          
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs 700")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs 988")
        
            elif(x=='C Programming'):
                self.bookid_var.set("BKID5465")
                self.booktitle_var.set("Introduction To C Programming")
                self.auther_var.set("Cyper Smith")
          
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs 100")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs 788")
        
            elif(x=='C++ Introduction'):
                self.bookid_var.set("BKID5466")
                self.booktitle_var.set("Introduction To C++ Language")
                self.auther_var.set("David Hussey")
          
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs 10")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs 588")
        
            elif(x=='Java'):
                self.bookid_var.set("BKID5467")
                self.booktitle_var.set("Introduction To Java Language")
                self.auther_var.set("Colin Willey")
          
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs 200")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs 798")
        
            elif(x=='Machine Python'):
                self.bookid_var.set("BKID5468")
                self.booktitle_var.set("Introduction To Machine Python")
                self.auther_var.set("Mike Smith")
          
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs 100")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs 780")
        
            elif(x=='Advance Python'):
                self.bookid_var.set("BKID5469")
                self.booktitle_var.set("Introduction To Advance Python")
                self.auther_var.set("Lewis King")
          
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs 200")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs 905")
        
            elif(x=='Tkinter'):
                self.bookid_var.set("BKID5471")
                self.booktitle_var.set("Introduction To Tkinter Course")
                self.auther_var.set("Brenndom Taylor")
          
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs 400")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs 940")
        
            elif(x=='Database'):
                self.bookid_var.set("BKID5472")
                self.booktitle_var.set("Introduction To Database")
                self.auther_var.set("Taylor Swift")
          
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs 400")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs 1050")
            
            
            elif(x=='Sqlite'):
                self.bookid_var.set("BKID5473")
                self.booktitle_var.set("Introduction To Sqlite Course")
                self.auther_var.set("Ross Neesham")
          
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs 200")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs 650")
        
        
            elif(x=='My Coding'):
                self.bookid_var.set("BKID5474")
                self.booktitle_var.set("Introduction To My Coding")
                self.auther_var.set("Nicolos Bravo")
          
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs 600")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs 1050")
        
        
        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)
        
        
        
        
        
        # --------------------BUTTONS FRAME---------------------------------
        
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=60)
        
        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)
        
        btnAddData=Button(Framebutton,text="Show Data",command=self.showData,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)
        btnAddData=Button(Framebutton,text="Update",command=self.update,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)
        btnAddData=Button(Framebutton,text="Delete",command=self.delete,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)
        btnAddData=Button(Framebutton,text="Reset",command=self.reset,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)
        btnAddData=Button(Framebutton,text="Exit",command=self.iExit,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)
        
        
        
        
        
        
        # --------------------INFORMATION FRAME---------------------------------
        
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=590,width=1530,height=200)
        
        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)
        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        
        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","address1","address2","postid","mobile","bookid","booktitle","auther","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address 1")
        self.library_table.heading("address2",text="Address 2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Date Of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days On Book")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Over Due")
        self.library_table.heading("finalprice",text="Final Price")
        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        
        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)
        
        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        
        
        
    def adda_data(self):
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mohitsinha80@",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                      self.member_var.get(),
                                                                                                      self.prn_var.get(),
                                                                                                      self.id_var.get(),
                                                                                                      self.firstname_var.get(),
                                                                                                      self.lastname_var.get(),
                                                                                                      self.address1_var.get(),
                                                                                                      self.address2_var.get(),
                                                                                                      self.postcode_var.get(),
                                                                                                      self.mobile_var.get(),
                                                                                                      self.bookid_var.get(),
                                                                                                      self.booktitle_var.get(),
                                                                                                      self.auther_var.get(),
                                                                                                      self.dateborrowed_var.get(),
                                                                                                      self.datedue_var.get(),
                                                                                                      self.daysonbook_var.get(),
                                                                                                      self.lateratefine_var.get(),
                                                                                                      self.dateoverdue_var.get(),
                                                                                                      self.finalprice_var.get()
                                                                                                      ))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success","Member Has Been Inserted Successfully",parent=self.root)
        except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
    
            
    def update(self): 
        conn=mysql.connector.connect(host="localhost",username="root",password="Mohitsinha80@",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set member=%s,id=%s,firstname=%s,lastname=%s, address1=%s, address2=%s, postcode=%s, mobile=%s, bookid=%s, booktitle=%s, auther=%s, dateborrowed=%s, datedue=%s, daysonbook=%s, lateratefine=%s, dateoverdue=%s, finalprice=%s where prn_no=%s",(
            self.member_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.auther_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.lateratefine_var.get(),
            self.dateoverdue_var.get(),
            self.finalprice_var.get(),
            self.prn_var.get()
            ))
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success","Member Has Been Updated")
            
    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":  
            messagebox.showerror("Error","First Select The Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mohitsinha80@",database="mydata")
            my_cursor=conn.cursor()
            query="delete from library where prn_no=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)
            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()
            messagebox.showinfo("Success","Member Has Been Deleted")
        
                 
            
         
        
        
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mohitsinha80@",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
            
        
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content["values"]
        self.member_var.set(row[0])
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.lateratefine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])
        
        
    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get() + "\n")   
        self.txtBox.insert(END,"PRN No.:\t\t"+ self.prn_var.get() + "\n")   
        self.txtBox.insert(END,"ID No.\t\t"+ self.id_var.get() + "\n")   
        self.txtBox.insert(END,"First Name\t\t"+ self.firstname_var.get() + "\n")   
        self.txtBox.insert(END,"Last Name\t\t"+ self.lastname_var.get() + "\n")   
        self.txtBox.insert(END,"Address1\t\t"+ self.address1_var.get() + "\n")   
        self.txtBox.insert(END,"Address2\t\t"+ self.address2_var.get() + "\n")   
        self.txtBox.insert(END,"Post Code\t\t"+ self.postcode_var.get() + "\n")   
        self.txtBox.insert(END,"Mobile NO.\t\t"+ self.mobile_var.get() + "\n")   
        self.txtBox.insert(END,"Book Id\t\t"+ self.bookid_var.get() + "\n")   
        self.txtBox.insert(END,"Book Title\t\t"+ self.booktitle_var.get() + "\n")   
        self.txtBox.insert(END,"Author\t\t"+ self.auther_var.get() + "\n")   
        self.txtBox.insert(END,"Date Borrowed\t\t"+ self.dateborrowed_var.get() + "\n")   
        self.txtBox.insert(END,"Date Due\t\t"+ self.datedue_var.get() + "\n")   
        self.txtBox.insert(END,"Date On Book\t\t"+ self.daysonbook_var.get() + "\n")   
        self.txtBox.insert(END,"Late Rate Fine\t\t"+ self.lateratefine_var.get() + "\n")   
        self.txtBox.insert(END,"Date Over Due\t\t"+ self.dateoverdue_var.get() + "\n")   
        self.txtBox.insert(END,"Final Price\t\t"+ self.finalprice_var.get() + "\n")   
        
        
    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.lateratefine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set(""),
        self.txtBox.delete("1.0",END)
        
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Managment System","Do You Want To Exit")
        if iExit>0:
            self.root.destroy()
            return
        
               
        
         
        
if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()