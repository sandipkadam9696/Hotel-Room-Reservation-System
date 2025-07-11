from tkinter import *
from PIL import Image,ImageTk
from customer import Cust_Win
from room import RoomBooking
from details import DetailsRoom
from repot import Repot


class HotelManagmentSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Reservation System ")
        self.root.geometry("1550x800+0+0")


        img1=Image.open(r"F:\Room Reasrvation  System\img\hotel6.jpg")
        img1=img1.resize((1550,140))
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)  


        #======================Logo==========================
        
        img2=Image.open(r"F:\Room Reasrvation  System\img\1st.jpg")
        img2=img2.resize((230,140))
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)  

        #========================titele======================

        lbl_title=Label(self.root,text="Hotel Reservation System",font=("times new roman",30,"bold"),bg="black",fg="gold",bd=3,relief=RIDGE)
        lbl_title.place(x=0,y=130,width=1550,height=50)

        #===========================main fraim======================

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=180,width=1550,height=620)

        #=======================menu===========================
        
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=3,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

          #===========================button fraim======================

        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=200)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)


        room_btn=Button(btn_frame,text="ROOM",command=self.room,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)


        details_btn=Button(btn_frame,text="DETAILS",command=self.details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",cursor="hand2")
        details_btn.grid(row=2,column=0,pady=1)


        report_btn=Button(btn_frame,text="REPORT",command=self.Repot1,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",cursor="hand2")
        report_btn.grid(row=3,column=0,pady=1)


        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",cursor="hand2")
        logout_btn.grid(row=4,column=0,pady=1)

        #====================right side img===================

        img3=Image.open(r"F:\Room Reasrvation  System\img\hotel8.jpg")
        img3=img3.resize((1310,590))
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1150,height=510)  

        #================================DOWN IMG============================

        img4=Image.open(r"F:\Room Reasrvation  System\img\hotel2.jpg")
        img4=img4.resize((230,210))
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg4=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg4.place(x=0,y=235,width=230,height=150)  


        img5=Image.open(r"F:\Room Reasrvation  System\img\hotel.jpg")
        img5=img5.resize((230,190))
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg5=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg5.place(x=0,y=380,width=230,height=130)  
#=============open new windo=======================

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)


   
    def room(self):
        self.new_window=Toplevel(self.root)
        self.app=RoomBooking(self.new_window)     





        
    def details(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)     


             
    def Repot1(self):
        self.new_window=Toplevel(self.root)
        self.app=Repot(self.new_window)  



    def logout(self):
        self.root.destroy()

        



        
       




       



if __name__ == "__main__":
    root=Tk()
    obj=HotelManagmentSystem(root)
    root.mainloop()