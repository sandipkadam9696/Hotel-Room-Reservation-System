from tkinter import *
from PIL import Image,ImageTk
from tkinter import  ttk
import mysql.connector
import random
from tkinter import messagebox
import tkinter as tk
from time import strftime
from datetime import datetime




class RoomBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Managment System ")
        self.root.geometry("1140x540+230+210")

        #=============================varabels=============

        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        self.serch_var=StringVar()        
        


           
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

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ROOMBOOKING Details",font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=417)


                #=========================labels and Entry And  "Customer Contact===============

        lbl_cust_Contact=Label(labelframeleft,text="Customer Contact",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_Contact.grid(row=0,column=0,sticky=W)

        entry_Contact=ttk.Entry(labelframeleft,width=20,textvariable=self.var_contact,font=("times new roman",12,"bold"),)
        entry_Contact.grid(row=0,column=1,sticky=W)

        #==============fetch data button==============================

        btnFetchData=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=300,y=4)
        

         #=========================labels and Entry and check_in_date===============

        check_in_date=Label(labelframeleft,text=" check in date:",font=("times new roman",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        txt_check_in_date=ttk.Entry(labelframeleft,width=25,textvariable=self.var_checkin,font=("times new roman",12,"bold"))
        txt_check_in_date.grid(row=1,column=1)
        

         #=========================labels and  check_out_date===============

        check_out_date=Label(labelframeleft,text=" check out date:",font=("times new roman",12,"bold"),padx=2,pady=6)
        check_out_date.grid(row=2,column=0,sticky=W)

        txt_check_out_date=ttk.Entry(labelframeleft,width=25,textvariable=self.var_checkout,font=("times new roman",12,"bold"))
        txt_check_out_date.grid(row=2,column=1)
        

         #=========================labels and Room Type box  combo box===============

        lbl_RoomType=Label(labelframeleft,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
        my_cursor=conn.cursor() 
        my_cursor.execute("select RoomType from details")
        rowss=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),state="readonly")
        combo_RoomType["value"]=rowss
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

      
        

         #=========================labels and Room Available===============

        lbl_RoomAvailable=Label(labelframeleft,text="Room Available:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_RoomAvailable.grid(row=4,column=0,sticky=W)

       # txtRoomAvailable=ttk.Entry(labelframeleft,width=25,textvariable=self.var_roomavailable,font=("times new roman",12,"bold"))
        #txtRoomAvailable.grid(row=4,column=1)
        conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
        my_cursor=conn.cursor() 
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)

      
        
        

         #=========================labels and Entry and Meal===============

        lbl_Meal=Label(labelframeleft,text="Meal:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_Meal.grid(row=5,column=0,sticky=W)

        txt_Meal=ttk.Entry(labelframeleft,width=25,textvariable=self.var_meal,font=("times new roman",12,"bold"))
        txt_Meal.grid(row=5,column=1)
        

           #=========================labels and Entry and No Of Days===============

        lbl_NoOfDays=Label(labelframeleft,text="No Of Days:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_NoOfDays.grid(row=6,column=0,sticky=W)

        txt_Meal=ttk.Entry(labelframeleft,width=25,textvariable=self.var_noofdays,font=("times new roman",12,"bold"))
        txt_Meal.grid(row=6,column=1)
        


   #=========================labels and Entry and Paid Tax==============

        lbl_Paid_Tax=Label(labelframeleft,text="Paid Tax:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_Paid_Tax.grid(row=7,column=0,sticky=W)

        txt_Meal=ttk.Entry(labelframeleft,width=25,textvariable=self.var_paidtax,font=("times new roman",12,"bold"),state="readonly")
        txt_Meal.grid(row=7,column=1)


   #=========================labels and Entry and _Sub_Total===============

        lbl_Sub_Total=Label(labelframeleft,text="Sub Total:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_Sub_Total.grid(row=8,column=0,sticky=W)

        txt_Meal=ttk.Entry(labelframeleft,width=25,textvariable=self.var_actualtotal,font=("times new roman",12,"bold"),state="readonly")
        txt_Meal.grid(row=8,column=1)
       
   #=========================labels and Entry and Total_Cost===============

        lbl_Total_Cost=Label(labelframeleft,text="Total cost:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_Total_Cost.grid(row=9,column=0,sticky=W)
    
        txt_Meal=ttk.Entry(labelframeleft,width=20,textvariable=self.var_total,font=("times new roman",12,"bold"),state="readonly")
        txt_Meal.grid(row=9,column=1,sticky=W)

        #================bill button================

  
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnBill.place(x=315,y=320)

        

#=============================Button=======================

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=350,width=412,height=40)
         

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)


        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)


        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)



       #===============Right side img============

       
        img3=Image.open(r"F:\Room Reasrvation  System\img\hotel.3.jpg")
        img3=img3.resize((367,300))
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=367,height=300)





#=======================Searche system  button=================

  
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"))
        Table_Frame.place(x=435,y=280,width=690,height=178)

        lblSearchBy=Label(Table_Frame,text="Search By  ",font=("times new roman",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.serch_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.serch_var,font=("arial",12,"bold"),state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=22,font=("times new roman",12,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnSearch.grid(row=0,column=3,padx=1)
        
        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnShowAll.grid(row=0,column=4,padx=1)


           #==================show data table ====================

        details_table=LabelFrame(Table_Frame,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"))
        details_table.place(x=0,y=40,width=680,height=115)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-In")
        self.room_table.heading("checkout",text="Check-Out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="No-Of-Days")
        
        self.room_table["show"]="headings"


        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)
      
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self. get_cuersor)

        self.fetch_data()

 #===========================add data==================       
    def add_data(self):
      if self.var_contact.get()=="" or self.var_checkin.get()=="":
             messagebox.showerror("Error","All fileds are requaired",parent=self.root)
      else:
                
            try:   
            
                conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
                my_cursor=conn.cursor() 
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(

                                                                                self.var_contact.get(),
                                                                                self.var_checkin.get(),
                                                                                self.var_checkout.get(),
                                                                                self.var_roomtype.get(),
                                                                                self.var_roomavailable.get(),
                                                                                self.var_meal.get(),
                                                                                self.var_noofdays.get()
                                                                                  
                                                                                    )) 
                conn.commit()
                self.fetch_data()
                conn.close()
        
                messagebox.showinfo("Success","Room Booked",parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

#============fetch data=========================
                
    def fetch_data(self):
         conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
         my_cursor=conn.cursor() 
         my_cursor.execute("select * from room")
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

        self.var_contact.set(row[0]), 
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])
        

        #=======================Updata data==================

        
    def update(self):
         if self.var_contact.get()=="":
             messagebox.showerror("Error","Plaease enter mobile number",parent=self.root)
         else:    
            conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
            my_cursor=conn.cursor() 
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(
                                                                                                                            
                                                                                                                                           
                                                                                                                                            self.var_checkin.get(),
                                                                                                                                            self.var_checkout.get(),
                                                                                                                                            self.var_roomtype.get(),
                                                                                                                                            self.var_roomavailable.get(),
                                                                                                                                            self.var_meal.get(),
                                                                                                                                            self.var_noofdays.get(),
                                                                                                                                            self.var_contact.get()
                                                                                                                                            
                                                                                                                                        ))

   



            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room Details Has Been Update Successfully",parent=self.root)

    # ===================Delete the Room Records==================

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Managment System ","DO you want delete this Room information",parent=self.root)
        if mDelete>0:
             conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
             my_cursor=conn.cursor() 
             query="delete from room where Contact=%s"
             value=(self.var_contact.get(),)
             my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close() 
#============================Reset the information Roomr===================

    def reset(self):
        
        self.var_contact.set("") 
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
        

       
      

            




    




       #=================================== all data fetch show data of costomer in right side====================

    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Plaese enter Contact Number",parent=self.root)
        else:
          conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
          my_cursor=conn.cursor() 
          query=("select Name from customer where Mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()

          if row==None:
              messagebox.showerror("Error","This Number Not Found",parent=self.root)
          else:
              conn.commit()
              conn.close()
#==================Name=======================
              showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
              showDataframe.place(x=435,y=55,width=300,height=225)     

              lblname=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
              lblname.place(x=0,y=0)   

              lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
              lbl.place(x=90,y=0)

#=================Gender======================
              conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
              my_cursor=conn.cursor() 
              query=("select Gender from customer where Mobile=%s")
              value=(self.var_contact.get(),)
              my_cursor.execute(query,value)
              row=my_cursor.fetchone()

              lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
              lblGender.place(x=0,y=30)   

              lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
              lbl2.place(x=90,y=30)

#=========================Email===========================
              conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
              my_cursor=conn.cursor() 
              query=("select Email from customer where Mobile=%s")
              value=(self.var_contact.get(),)
              my_cursor.execute(query,value)
              row=my_cursor.fetchone()

              lblEmail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
              lblEmail.place(x=0,y=60)   

              lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
              lbl3.place(x=90,y=60)

          
          #=========================Nationality===========================
              conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
              my_cursor=conn.cursor() 
              query=("select Nationality from customer where Mobile=%s")
              value=(self.var_contact.get(),)
              my_cursor.execute(query,value)
              row=my_cursor.fetchone()

              lblNationality=Label(showDataframe,text="Nationality: ",font=("arial",12,"bold"))
              lblNationality.place(x=0,y=90)   

              lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
              lbl4.place(x=90,y=90)
              


                   
          #=========================Address===========================
              conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
              my_cursor=conn.cursor() 
              query=("select Address from customer where Mobile=%s")
              value=(self.var_contact.get(),)
              my_cursor.execute(query,value)
              row=my_cursor.fetchone()

              lblAddress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
              lblAddress.place(x=0,y=120)   

              lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
              lbl5.place(x=90,y=120)

        #==============================searchinmg the Room data botton==============================

    # def search(self):
    #     conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
    #     my_cursor=conn.cursor() 

    #     my_cursor.execute("select * from room where "+str(self.serch_var.get())+"LIKE'%"+str(self.txt_search.get())+"%''")
    #     rows=my_cursor.fetchall()
    #     if len(rows)!=0:
    #         self.room_table.delete(*self.room_table.get_children())
    #         for i in rows:
    #             self.room_table.insert("",END,values=i)
    #     conn.commit()
    #     conn.close()    


    def search(self):
    # Establishing connection to MySQL
        conn = mysql.connector.connect(host="localhost", username="root", password="Sandip712", database="management")
        my_cursor = conn.cursor()

        # Fixing SQL injection vulnerability and correcting the query
        search_text = str(self.txt_search.get())
        search_field = str(self.serch_var.get())

        # Make sure your search field is safe to be used (e.g., only accept valid column names, etc.)
        query = f"SELECT * FROM room WHERE {search_field} LIKE %s"
        my_cursor.execute(query, ('%' + search_text + '%',))

        # Fetch the results
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())  # Clear previous data in the table
            for row in rows:
                self.room_table.insert("", "end", values=row)  # Insert each row into the table
        else:
            print("No results found")

        # Commit and close the connection
        conn.commit()
        conn.close()

      


     #===============calculation from days====================
         
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)
 
        if (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Laxary"):
            q1=float(300)
            q2=float(600)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Launch" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(600)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


        elif(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Duplex"):
            q1=float(500)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

            
       
    







if __name__ == " __ main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()

