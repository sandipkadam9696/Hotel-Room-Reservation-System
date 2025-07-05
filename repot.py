from tkinter import *
from PIL import Image,ImageTk
from tkinter import  ttk
import mysql.connector
import random
from tkinter import messagebox
import tkinter as tk
from time import strftime
from datetime import datetime




class Repot:
    def __init__(self,root):
        self.root=root
        self.root.title("Room Reaservation System ")
        self.root.geometry("1140x540+230+220")

        
        lbl_title=Label(self.root,text="Add Repot",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=3,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1140,height=50)
#======================================== add Left Frame=================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Repot",font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=400,height=250)


        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        self.var_ref=StringVar()
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=25,font=("times new roman",12,"bold"))
        entry_ref.grid(row=0,column=1)


        lblroomNO=Label(labelframeleft,text="Room Number",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblroomNO.grid(row=1,column=0,sticky=W)

        self.var_roomNumber=StringVar()
        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomNumber,font=("arial",12,"bold"),state="readonly")
        combo_RoomNo["value"]=("","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25")
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=1,column=1)


        self.var_floorNumber=StringVar()
        lblroomFloor=Label(labelframeleft,text="Floor Number",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblroomFloor.grid(row=9,column=0,sticky=W)


        combo_RoomFloor=ttk.Combobox(labelframeleft,textvariable=self.var_floorNumber,font=("arial",12,"bold"),state="readonly")
        combo_RoomFloor["value"]=("","floor 1","floor 2","floor 3")
        combo_RoomFloor.current(0)
        combo_RoomFloor.grid(row=9,column=1)


        self.var_report=StringVar()
        lblroomRepot=Label(labelframeleft,text="Room Report",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblroomRepot.grid(row=10,column=0,sticky=W)


        combo_RoomRepot=ttk.Combobox(labelframeleft,textvariable=self.var_report,font=("arial",12,"bold"),state="readonly")
        combo_RoomRepot["value"]=("","Noise","Low Water Pressure in Bathroom ","Food Issue","Dim Lighting","Flickering Lights","Hot Water Problems","Room Cleaning Issues","WiFi Issues","A/C Not Work","Service Issue")
        combo_RoomRepot.current(0)
        combo_RoomRepot.grid(row=10,column=1)

        self.var_feedback=StringVar()
        feedback=Label(labelframeleft,text="FeedBack",font=("times new roman",12,"bold"),padx=2,pady=6)
        feedback.grid(row=13,column=0,sticky=W)

        txt_feedback=ttk.Entry(labelframeleft,width=25,textvariable=self.var_feedback,font=("times new roman",12,"bold"))
        txt_feedback.grid(row=13,column=1)



        # btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        # btn_frame.place(x=0,y=350,width=412,height=40)
        

        btnAdd=Button(labelframeleft,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.place(x=0,y=190)

        btnReset=Button(labelframeleft,text="Reset",command=self.reset_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.place(x=110,y=190)

        btnDelete=Button(labelframeleft,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.place(x=220,y=190)






        #=================Right side frame and Search System ==================

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Detailes",font=("times new roman",12,"bold"))
        Table_Frame.place(x=600,y=55,width=515,height=350)

        
        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.report_table=ttk.Treeview(Table_Frame,column=("ref","roomNumber","floorNumber","report","feedback"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.report_table.xview)
        scroll_y.config(command=self.report_table.yview)

        self.report_table.heading("ref",text="ref")
        self.report_table.heading("roomNumber",text="roomNumber")
        self.report_table.heading("floorNumber",text="floorNumber")
        self.report_table.heading("report",text="report")
        self.report_table.heading("feedback",text="feedback")
        
        self.report_table["show"]="headings"

        self.report_table.column("ref",width=100)
        self.report_table.column("roomNumber",width=100)
        self.report_table.column("floorNumber",width=100)
        self.report_table.column("report",width=100)
        self.report_table.column("feedback",width=100)
       
      
        
        self.report_table.pack(fill=BOTH,expand=1)
        self.report_table.bind("<ButtonRelease-1>",self. get_cuersor)

        self.fetch_data()






    def add_data(self):
      if self.var_roomNumber.get()=="" or self.var_floorNumber.get()=="":
             messagebox.showerror("Error","All fileds are requaired",parent=self.root)
      else:
                
            try:   
            
                conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
                my_cursor=conn.cursor() 
                my_cursor.execute("insert into report1 values(%s,%s,%s,%s,%s)",(
                                                                                self.var_ref.get(),
                                                                                self.var_roomNumber.get(),
                                                                                self.var_floorNumber.get(),
                                                                                self.var_report.get(),
                                                                                self.var_feedback.get()
                                                                            
                                                                                  
                                                                                    )) 
                conn.commit()
                self.fetch_data()
                conn.close()
        
                messagebox.showinfo("Success","Report  Added Successfully ",parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)








    def fetch_data(self):
         conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
         my_cursor=conn.cursor() 
         my_cursor.execute("select * from report1")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.report_table.delete(*self.report_table.get_children())
             for i in rows:
                 self.report_table.insert("",END,values=i)
             conn.commit()
             conn.close()





    #==========goto the cursor and display the data========

    def get_cuersor(self,event=""):
        cusrsor_row=self.report_table.focus()
        content=self.report_table.item(cusrsor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_roomNumber.set(row[1]), 
        self.var_floorNumber.set(row[2]),
        self.var_report.set(row[3]) ,
        self.var_feedback.set(row[4])             
               





 # ===================Delete the Report Records==================

    def mDelete(self):
        mDelete=messagebox.askyesno("Room Reservation System ","DO you want delete this Report information",parent=self.root)
        if mDelete>0:
             conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
             my_cursor=conn.cursor() 
             query="delete from report1 where ref=%s"
             value=(self.var_ref.get(),)
             my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close() 
    #               

    # def mDelete(self):
    #     mDelete = messagebox.askyesno("Room Reservation System", "Do you want to delete this Report information?", parent=self.root)
    #     if mDelete:
    #         try:
    #             conn = mysql.connector.connect(host="localhost", username="root", password="Sandip712", database="management")
    #             my_cursor = conn.cursor()

    #             # Construct the DELETE query
    #             query = "DELETE FROM report WHERE roomNumber = %s AND floorNumber = %s AND report = %s AND feedback = %s"
    #             values = (self.var_roomNumber.get(), self.var_floorNumber.get(), self.var_report.get(), self.var_feedback.get())

    #             # Execute the query
    #             my_cursor.execute(query, values)

    #             # Commit the transaction
    #             conn.commit()

    #             # Fetch updated data (assuming this method exists)
    #             self.fetch_data()

    #         except mysql.connector.Error as err:
    #             messagebox.showerror("Error", f"Error deleting data: {err}")
    #         finally:
    #             if conn.is_connected():
    #                 my_cursor.close()
    #                 conn.close()
    #     else:
    #         return




    def reset_data(self):
        self.var_ref.set(""),
        self.var_roomNumber.set(""), 
        self.var_floorNumber.set(""),
        self.var_report.set(""),
        self.var_feedback.set("")













if __name__ == " __ main__":
    root=Tk()
    obj=Repot(root)
    root.mainloop()