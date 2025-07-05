from tkinter import *
from PIL import Image,ImageTk
from tkinter import  ttk
import mysql.connector
import random
from tkinter import messagebox
import tkinter as tk





class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Room Reservation System ")
        self.root.geometry("1140x540+230+220")

        #======================Varibles=======================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
       


        
        #========================titele======================

        lbl_title=Label(self.root,text="ADD COUSTEMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=3,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1140,height=50)

        #======================Logo==========================
        
        img2=Image.open(r"F:\Room Reasrvation  System\img\1st.jpg")
        img2=img2.resize((100,40))
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)


        # =============================label frame-====================

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=417)

        #=========================labels and Entry And  Cust Ref===============

        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,width=25,textvariable=self.var_ref,font=("times new roman",12,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

         #=========================labels and Entry and Cust Name===============

        c_name=Label(labelframeleft,text="Customer Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        c_name.grid(row=1,column=0,sticky=W)

        txt_c_name=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=25,font=("times new roman",12,"bold"))
        txt_c_name.grid(row=1,column=1)
        

         #=========================labels and Entry mother===============

        lbl_m__name=Label(labelframeleft,text="Customer Father name",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_m__name.grid(row=2,column=0,sticky=W)

        txt_m_name=ttk.Entry(labelframeleft,width=25,textvariable=self.var_mother,font=("times new roman",12,"bold"))
        txt_m_name.grid(row=2,column=1)
        

         #=========================labels and Gender box combo box===============

        lbl_gender=Label(labelframeleft,text="Gender",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),state="readonly")
        combo_gender["value"]=("Male","Female","other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

      
        

         #=========================labels and Post Code===============

        lblPostCode=Label(labelframeleft,text="Addhar No",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)

        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_post,width=25,font=("times new roman",12,"bold"))
        txtPostCode.grid(row=4,column=1)
        

         #=========================labels and Entry and Mobile Number===============

        lblMobile=Label(labelframeleft,text="Mobile No",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)

        txtMobile=ttk.Entry(labelframeleft,width=25,textvariable=self.var_mobile,font=("times new roman",12,"bold"))
        txtMobile.grid(row=5,column=1)
        

           #=========================labels and Entry and Email===============

        lblEmail=Label(labelframeleft,text="Email",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)

        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_email,width=25,font=("times new roman",12,"bold"))
        txtMobile.grid(row=6,column=1)


   #=========================labels and Entry and  Nationality==============

        lblNationality=Label(labelframeleft,text="Nationality",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)


        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),state="readonly")
        combo_Nationality["value"]=("Indian","American","Japan")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)


   #=========================labels and Entry and Address===============

        lblAddress=Label(labelframeleft,text="Address",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=8,column=0,sticky=W)

        txtAddress=ttk.Entry(labelframeleft,width=25,textvariable=self.var_address,font=("times new roman",12,"bold"))
        txtAddress.grid(row=8,column=1)

 
    #=============Buttons================

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


        #=======================table frame====================

        
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"))
        Table_Frame.place(x=435,y=50,width=690,height=415)

    #=======================Searche button=================
        lblSearchBy=Label(Table_Frame,text="Search By  ",font=("times new roman",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.serch_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.serch_var,font=("arial",12,"bold"),state="readonly")
        combo_Search["value"]=("Mobile","Ref")
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
        details_table.place(x=0,y=50,width=680,height=320)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","father","gender","addhar","mobile","email","nationality","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("father",text="Father Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("addhar",text="Addhar")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"


        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("father",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("addhar",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("address",width=100)
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self. get_cuersor)
        self.fetch_data()

    def add_data(self):
         if self.var_mobile.get()=="" or self.var_mother.get()=="":
             messagebox.showerror("Error","All fileds are requaired",parent=self.root)
         else:
                
            try:   
            
                conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
                my_cursor=conn.cursor() 
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    
                                                                                self.var_ref.get(),
                                                                                self.var_cust_name.get(),  
                                                                                self.var_mother.get(),  
                                                                                self.var_gender.get(),  
                                                                                self.var_post.get(),
                                                                                self.var_mobile.get(), 
                                                                                self.var_email.get(), 
                                                                                self.var_nationality.get(),
                                                                                self.var_address.get()  

                                                                            )) 
                conn.commit()
                self.fetch_data()
                conn.close()
        
                messagebox.showinfo("Success","Customer has been added",parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)
    

    def fetch_data(self):
         conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
         my_cursor=conn.cursor() 
         my_cursor.execute("select * from customer")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
             for i in rows:
                 self.Cust_Details_Table.insert("",END,values=i)
             conn.commit()
             conn.close()

             #==========goto the cursor and display the data========

    def get_cuersor(self,event=""):
        cusrsor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cusrsor_row)
        row=content["values"]

        self.var_ref.set(row[0]), 
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_address.set(row[8])

     #==================update custemer detailes===============


    def update(self):
         if self.var_mobile.get()=="":
             messagebox.showerror("Error","Plaease enter mobile number",parent=self.root)
         else:    
            conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
            my_cursor=conn.cursor() 
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Address=%s where Ref=%s",(
                                                                                                                            
                                                                                                                                        self.var_cust_name.get(),  
                                                                                                                                        self.var_mother.get(),  
                                                                                                                                        self.var_gender.get(),  
                                                                                                                                        self.var_post.get(),
                                                                                                                                        self.var_mobile.get(), 
                                                                                                                                        self.var_email.get(), 
                                                                                                                                        self.var_nationality.get(),
                                                                                                                                        self.var_address.get(),
                                                                                                                                        self.var_ref.get()  
                                                                                                                                        ))

   



            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer Details Has Been Update Successfully",parent=self.root)

      
# ===================Delete the customer Records==================

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Managment System ","DO you want delete this customer information",parent=self.root)
        if mDelete>0:
             conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
             my_cursor=conn.cursor() 
             query="delete from customer where Ref=%s"
             value=(self.var_ref.get(),)
             my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close() 

    #============================Reset the information customer===================

    def reset(self):
        
        #self.var_ref.set(""), 
        self.var_cust_name.set(""),
        self.var_mother.set(""),
       #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
      #  self.var_nationality.set(""),
        self.var_address.set("")

       
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
                    

#==============================searchinmg the customer data botton==============================
    # def search(self):
        
    #          conn=mysql.connector.Connect(host="localhost",username="root",password="Sandip712",database="management") 
    #          my_cursor=conn.cursor() 

    #          my_cursor.execute("select * from customer where"+str(self.serch_var.get())+"LIKE'%"+str(self.txt_search.get())+"%'")
    #          rows=my_cursor.fetchall()
    #          if len(rows)!=0:
    #              self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
    #              for i in rows:
    #                  self.Cust_Details_Table.insert("",END,values=i)
    #              conn.commit()
    #          conn.close()   

    def search(self):
        try:
        # Establishing the connection
            conn = mysql.connector.Connect(host="localhost", username="root", password="Sandip712", database="management")
            my_cursor = conn.cursor()

            # Define the query with a placeholder for the search term
            search_term = "%" + str(self.txt_search.get()) + "%"

            # Modify query to safely handle dynamic column and value
            query = "SELECT * FROM customer WHERE {} LIKE %s".format(str(self.serch_var.get()))

            # Execute the query with the parameter
            my_cursor.execute(query, (search_term,))

            # Fetch the results
            rows = my_cursor.fetchall()

            # Handle the results
            if len(rows) != 0:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())  # Clear the existing data
                for i in rows:
                    self.Cust_Details_Table.insert("", END, values=i)  # Insert the fetched rows into the table
                conn.commit()

        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            # Ensure connection is closed properly
            conn.close()


    
if __name__ == " __ main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()


