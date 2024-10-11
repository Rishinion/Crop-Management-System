from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import tkinter.ttk as ttk


class bill:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management")
        self.root.geometry('925x500+300+200')
        self.root.config(bg="#fff")
        self.root.resizable(False, False)
        
        self.qty=IntVar()
        self.create_widgets()
        
#--------------------------------------------------------------------

    def create_widgets(self):
        self.heading = tk.Label(self.root, text='BILLING', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
        self.heading.place(x=350, y=20)

        self.frame = tk.Frame(self.root, width=500, height=350, bg="white")
        self.frame.place(x=40, y=80)

        self.frame1 = tk.Frame(self.root, width=250, height=350, bg="black")
        self.frame1.place(x=490, y=80)

        self.trv = ttk.Treeview(self.frame1, columns=(1, 2,3,4), height=15, show="headings")
        self.trv.column(1, anchor=CENTER, stretch=NO, width=100)
        self.trv.column(2, anchor=CENTER, stretch=NO, width=100)
        self.trv.column(3, anchor=CENTER, stretch=NO, width=100)
        self.trv.column(4, anchor=CENTER, stretch=NO, width=100)

        self.trv.heading(1, text="Id")
        self.trv.heading(2, text="Name")
        self.trv.heading(3, text="Quantity")
        self.trv.heading(4, text="Price")

        self.display_users()

        self.trv.grid(row=0, column=3, rowspan=5, padx=10, pady=10)


        self.name = Entry(self.frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
        self.name.place(x=30, y=80)
        self.name.insert(0, 'Name')
        self.name.bind('<FocusIn>', self.e_name)
        self.name.bind('<FocusOut>', self.l_name)
        
        Frame(self.frame,width=250,height=2,bg='black').place(x=25,y=107)


        self.phn = Entry(self.frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
        self.phn.place(x=30, y=120)
        self.phn.insert(0, 'Phone Number')
        self.phn.bind('<FocusIn>', self.e_phn)
        self.phn.bind('<FocusOut>', self.l_phn)
        
        Frame(self.frame,width=250,height=2,bg='black').place(x=25,y=145)


        self.crop = Entry(self.frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
        self.crop.place(x=30, y=160)
        self.crop.insert(0, 'Crop Id')
        self.crop.bind('<FocusIn>', self.e_crop)
        self.crop.bind('<FocusOut>', self.l_crop)
        
        Frame(self.frame,width=250,height=2,bg='black').place(x=25,y=185)

        self.qty=IntVar
        self.qty = Entry(self.frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
        self.qty.place(x=30, y=200)
        self.qty.insert(0, 'Quantity(KG)')
        self.qty.bind('<FocusIn>', self.e_qty)
        self.qty.bind('<FocusOut>', self.l_qty)
        
        Frame(self.frame,width=250,height=2,bg='black').place(x=25,y=221)


        self.cpn = Entry(self.frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
        self.cpn.place(x=30, y=240)
        self.cpn.insert(0, 'Crop Name')
        self.cpn.bind('<FocusIn>', self.e_cpn)
        self.cpn.bind('<FocusOut>', self.l_cpn)
        
        Frame(self.frame,width=250,height=2,bg='black').place(x=25,y=264)



        self.heading = tk.Label(self.root, text='TOTAL\n(included 18% gst):', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light', 10, 'bold'))
        self.heading.place(x=60, y=350)

        self.pay = Entry(self.frame, width=10, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11,'bold'))
        self.pay.place(x=160, y=273)


        
        

        Frame(self.frame,width=250,height=2,bg='black').place(x=25,y=264)

        

        self.show_button = tk.Button(self.frame, width=8, text='calculate', border=0,bg='#57a1f8',fg='white', cursor='hand2', command=self.df)
        self.show_button.place(x=110, y=330)

        self.show_button = tk.Button(self.frame, width=10, text='Generate Bill ', border=0,bg='#57a1f8',fg='white', cursor='hand2', command=self.gen)
        self.show_button.place(x=180, y=330)


        self.show_button = tk.Button(self.frame, width=6, text='Back ', border=0,bg='#57a1f8',fg='white', cursor='hand2', command=self.mm)
        self.show_button.place(x=60, y=330)
#---------------------------------------------------------------------------------
        
     
        

        
        
        
        

        




    

#---------------------------------------------------------------------

    def e_name(self, event):
        self.name.delete(0, 'end')

    def l_name(self, event):
        name = self.name.get()
        if name == '':
            self.name.insert(0, 'Name')


    def e_phn(self, event):
        self.phn.delete(0, 'end')

    def l_phn(self, event):
        name = self.phn.get()
        if name == '':
            self.phn.insert(0, 'Phone Number')


    def e_crop(self, event):
        self.crop.delete(0, 'end')

    def l_crop(self, event):
        name = self.crop.get()
        if name == '':
            self.crop.insert(0, 'Crop Id')


    def e_qty(self, event):
        self.qty.delete(0, 'end')

    def l_qty(self, event):
        name = self.qty.get()
        if name == '':
            self.qty.insert(0, 'Quantity(KG)')
#-------------------------------------------------------------------------------

    def e_cpn(self, event):
        self.cpn.delete(0, 'end')

    def l_cpn(self, event):
        name = self.cpn.get()
        if name == '':
            self.cpn.insert(0, 'Crop name')


    def e_tc(self, event):
        self.tc.delete(0, 'end')

    def l_tc(self, event):
        name = self.tc.get()
        if name == '':
            self.tc.insert(0, 'Total Cost')
    

    
    

#----------------------------------------------------------------------

    def display_users(self):
        self.root = root
        self.c = my_cursor
       
        for row in self.trv.get_children():
            self.trv.delete(row)

        
        self.c.execute("SELECT * FROM `crops`")
        users = self.c.fetchall()

        for user in users:
            self.trv.insert('', END, values=user)

#--------------------------------------------------------------------------------
    def mm(self):
        root.destroy()
        import mm


    def df(self):
        global myresult
        pg = self.crop.get()
    
        try:
            
            my_cursor.execute("SELECT price,cropname FROM crops WHERE id=%s",(pg,))
            myresult = my_cursor.fetchall()
             # Inserting fetched data into the entry widget
            if myresult:
                x=list(myresult[0])
                py=float(x[0])
                crpn=(x[1])
                qt=float(self.qty.get())
                topay=(py*qt+(py*qt*0.18))



                self.pay.delete(0, END)
                self.pay.insert(END, topay) 
                self.pay.configure(state='disabled')
                self.cpn.delete(0, END)
                self.cpn.insert(END, crpn) 
                self.cpn.configure(state='disabled')
            
            else:
                messagebox.showerror("Data","Enter Correct Crop Id:")
                



        
        except Exception as e:
            print("Error:", e)





#-----------------------------------------------------------------------------------


    def gen(self):
        try:
            nm=self.name.get()
            phno = self.phn.get()
            cnid = self.crop.get()
            cp=self.cpn.get()
            qy=int(self.qty.get())
            cst=self.pay.get()


            my_cursor.execute("SELECT quantity FROM crops WHERE id=%s",(cnid,))
            mr = my_cursor.fetchall()
                # Inserting fetched data into the entry widget
            if mr[0]:
                    x=mr[0]
                    print(x) 
                    print(type(x))
                    y=list(x)
                    print(type(y))
                    z=y[0]
                    print(z)
                    q=int(z)
                    print(type(q))

                    print(type(qy))
                    print(qy)
                    q-=qy  
                    print(q)   
                    print(type(q))     
                    
                                               
            else:
                    messagebox.showerror("Data","Enter Correct Crop Id:")


            if(q>=0):

                command = "INSERT INTO bill(name,phno,crop,quantity,totalcost) VALUES (%s,%s,%s,%s,%s)"
                my_cursor.execute(command, (nm,phno,cp,qy,cst))
                conn.commit()
                messagebox.showinfo("Inventory", "Name: "+nm+ "\nPhone Number:"+str(phno)+ "\nCrop name:" +cp+ "\nQuantity: " +str(qy)+ "\nTotal Price:" +str(cst))
            
                command = "UPDATE crops SET quantity = %s WHERE id = %s"
                my_cursor.execute(command, (q, cnid))
                conn.commit()
                messagebox.showinfo("Inventory", "Quantity updated successfully")

            else:
                messagebox.showinfo("Stock:","Quantity not available")
            
        except mysql.connector.Error as e:
            print("Error:", e)
            messagebox.showerror("Inventory", "Try Again")  

        


        
            
                
            
                
            
                 

        







#--------------------------------------------------------------------------------


    
    
        

        





#----------------------------------------------------------------------------------


conn = mysql.connector.connect(host='localhost',port='3307',username='root',password='0000',database='reg')
my_cursor=conn.cursor()

root=tk.Tk()
bill(root)
root.mainloop()