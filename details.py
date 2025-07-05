from tkinter import *
from PIL import Image,ImageTk
from tkinter import  ttk
import mysql.connector
import random
from tkinter import messagebox
import tkinter as tk
from time import strftime
from datetime import datetime




class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Room Reaservation System ")
        self.root.geometry("1140x540+230+210")

            
        #========================titele======================

        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=3,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1140,height=50)

        #======================Logo==========================
        
        img2=Image.open(r"F:\Room Reasrvation  System\img\1st.jpg")
        img2=img2.resize((100,40))
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        
        # =============================label frame-====================

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=540,height=350)

        #Floor

        lbl_floor=Label(labelframeleft,text="Floor",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)
         
        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,width=20,textvariable=self.var_floor,font=("times new roman",12,"bold"),)
        entry_floor.grid(row=0,column=1,sticky=W)
 
        #Room 

        lbl_RoomNo=Label(labelframeleft,text="Room No",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)

        self.var_RoomNo=StringVar()
        entry_RoomNo=ttk.Entry(labelframeleft,width=20,textvariable=self.var_RoomNo,font=("times new roman",12,"bold"),)
        entry_RoomNo.grid(row=1,column=1,sticky=W)

          #Room Type

        lbl_RoomType=Label(labelframeleft,text="Room Type",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)

        self.var_RoomType=StringVar()
        entry_RoomType=ttk.Entry(labelframeleft,width=20,textvariable=self.var_RoomType,font=("times new roman",12,"bold"),)
        entry_RoomType.grid(row=2,column=1,sticky=W)

        #=============================Button=======================

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)
         

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)


        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)


        btnReset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        #=================Right side frame and Search System ==================

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Detailes",font=("times new roman",12,"bold"))
        Table_Frame.place(x=600,y=55,width=515,height=350)

        
        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_Frame,column=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor",)
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomtype",text="Room Type")
        
        self.room_table["show"]="headings"


        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomtype",width=100)
       
      
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self. get_cuersor)

        self.fetch_data()

#===========================add data==================       
    def add_data(self):
      if self.var_floor.get()=="" or self.var_RoomType.get()=="":
             messagebox.showerror("Error","All fileds are requaired",parent=self.root)
      else:
                
            try:   
            
                conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
                my_cursor=conn.cursor() 
                my_cursor.execute("insert into details values(%s,%s,%s)",(

                                                                                self.var_floor.get(),
                                                                                self.var_RoomNo.get(),
                                                                                self.var_RoomType.get()
                                                                            
                                                                                  
                                                                                    )) 
                conn.commit()
                self.fetch_data()
                conn.close()
        
                messagebox.showinfo("Success","New Room Added Successfully ",parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

#============fetch data=========================
                
    def fetch_data(self):
         conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
         my_cursor=conn.cursor() 
         my_cursor.execute("select * from details")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.room_table.delete(*self.room_table.get_children())
             for i in rows:
                 self.room_table.insert("",END,values=i)
             conn.commit()
             conn.close()


#==========goto the cursor and display the data========

    def get_cuersor(self,event=""):
        cusrsor_row=self.room_table.focus()
        content=self.room_table.item(cusrsor_row)
        row=content["values"]

        self.var_floor.set(row[0]), 
        self.var_RoomNo.set(row[1]),
        self.var_RoomType.set(row[2])



        #=======================Updata data button ==================

        
    def update(self):
         if self.var_floor.get()=="":
             messagebox.showerror("Error","Plaease enter Floor number",parent=self.root)
         else:    
            conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
            my_cursor=conn.cursor() 
            my_cursor.execute("update details set Floor=%s,RoomType=%s  where RoomNo=%s",(
                                                                                                                            
                                                                                                                                           
                                                                                                                                            self.var_floor.get(),
                                                                                                                                            self.var_RoomType.get(),
                                                                                                                                            self.var_RoomNo.get()
                                                                                                                                            
                                                                                                                                        ))

   



            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New Room Details Has Been Update Successfully",parent=self.root)
        

   # ===================Delete the Room Records==================

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Managment System ","DO you want delete this Room information",parent=self.root)
        if mDelete>0:
             conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
             my_cursor=conn.cursor() 
             query="delete from details where RoomNo=%s"
             value=(self.var_RoomNo.get(),)
             my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close() 




    def reset_data(self):
        self.var_floor.set(""), 
        self.var_RoomNo.set(""),
        self.var_RoomType.set("")



















if __name__ == " __ main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()

