from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import tkinter.ttk as ttk


class InventoryApp:
    def __init__(self, root,my_cursor):
        self.root = root
        self.my_cursor = my_cursor
        self.root.title("Inventory Management")
        self.root.geometry('925x500+300+200')
        self.root.config(bg="#fff")
        self.root.resizable(False, False)
        self.create_widgets()
        
        
        self.trv.bind('<ButtonRelease-1>', self.on_click)


###################-----------------------------------------------------


    def create_widgets(self):
        self.heading = tk.Label(self.root, text='INVENTORY', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
        self.heading.place(x=350, y=20)

        self.frame = tk.Frame(self.root, width=350, height=370, bg="white")
        self.frame.place(x=40, y=80)


        self.frame1 = tk.Frame(self.root, width=350, height=350, bg="black")
        self.frame1.place(x=490, y=80) 


        

        self.add_button = tk.Button(self.frame, width=6, text='ADD', border=0,bg='#57a1f8',fg='white', cursor='hand2', command=self.add_item)
        self.add_button.place(x=215, y=340)

        self.show_button = tk.Button(self.frame, width=6, text='SHOW', border=0,bg='#57a1f8',fg='white', cursor='hand2', command=self.show_items)
        self.show_button.place(x=150, y=340)

        self.add_button = tk.Button(self.frame, width=6, text='BACK', border=0,bg='#57a1f8',fg='white', cursor='hand2', command=self.mm1)
        self.add_button.place(x=80, y=340)


        
        

       
        self.trv = ttk.Treeview(self.frame1, columns=(1,2,3), height=15, show="headings")
        self.trv.column(1, anchor=CENTER, stretch=NO, width=100)
        self.trv.column(2, anchor=CENTER, stretch=NO, width=100)
        self.trv.column(3, anchor=CENTER, stretch=NO, width=100)
        

        
        self.trv.heading(1, text="Name")
        self.trv.heading(2, text="Quantity")
        self.trv.heading(3, text="Price")

        self.display_users()

        self.trv.grid(row=0, column=3, rowspan=5, padx=10, pady=10)
        self.trv.bind("<ButtonRelease-1>", self.on_click)


        


        self.crop_name = Entry(self.frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
        self.crop_name.place(x=30, y=80)
        #self.crop_name.insert(0, 'Item')
        #self.crop_name.bind('<FocusIn>', self.on_enter_crop_name)
        #self.crop_name.bind('<FocusOut>', self.on_leave_crop_name)
        
        Frame(self.frame,width=250,height=2,bg='black').place(x=25,y=107)

        self.quantity = Entry(self.frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
        self.quantity.place(x=30, y=150)
        self.quantity.insert(0, 'Quantity IN(KG)')
        self.quantity.bind('<FocusIn>', self.on_enter_quantity)
        self.quantity.bind('<FocusOut>', self.on_leave_quantity)
        
        Frame(self.frame,width=250,height=2,bg='black').place(x=25,y=177)

    '''
        self.price = Entry(self.frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
        self.price.place(x=30, y=210)
        self.price.insert(0, 'Price')
        self.price.bind('<FocusIn>', self.e_price)
        self.price.bind('<FocusOut>', self.l_price)
        
        Frame(self.frame,width=250,height=2,bg='black').place(x=25,y=240)
    '''
###############_---------------------------------------------------------

    def on_click(self, event):
    # Get the selected item
        item = self.trv.selection()[0]
    
    # Retrieve data from the selected item
        data = self.trv.item(item, "values")

    # Assuming you have entry boxes named entry_name, entry_quantity, entry_price
    # You can populate them with the selected data
        self.crop_name.delete(0, END)
        self.crop_name.insert(0, data[0])  # Name
        #self.quantity.delete(0, END)
        #self.quantity.insert(0, data[1])  # Quantity
        #self.entry_price.delete(0, END)
       # self.entry_price.insert(0, data[2])  # Price
    
   
    '''
    def on_enter_crop_name(self, event):
        self.crop_name.delete(0, 'end')

    def on_leave_crop_name(self, event):
        name = self.crop_name.get()
        if name == '':
            self.crop_name.insert(0, 'Crop Name')
    '''
    
    def on_enter_quantity(self, event):
        self.quantity.delete(0, 'end')

    def on_leave_quantity(self, event):
        name1 = self.quantity.get()
        if name1 == '':
            self.quantity.insert(0, 'Quantity(IN KG)')

    '''
    def e_price(self, event):
        self.price.delete(0, 'end')

    def l_price(self, event):
        name2 = self.price.get()
        if name2 == '':
            self.price.insert(0, 'Price')
    '''
    
    
   

##########################_-----------------------------------------------------------
      
    def display_users(self):
        self.root = root
        self.c = my_cursor
       
        for row in self.trv.get_children():
            self.trv.delete(row)

        
        self.c.execute("SELECT * FROM `crops`")
        users = self.c.fetchall()

        for user in users:
            self.trv.insert('', END, values=user)


    def mm1(self):
        root.destroy()
        import mm
        
            
   #########################_---------------------------------------------------------- 

    def add_item(self):
        try:                    
            cn = self.crop_name.get()
            qn = self.quantity.get()
            #pr = self.price.get()  

            command = "UPDATE crops SET quantity = %s WHERE cropname = %s"
            
            my_cursor.execute(command, (qn, cn))
            conn.commit()

        # Check if any rows were affected by the update
            if my_cursor.rowcount == 0:
            # If no rows were affected, show an error message
                messagebox.showerror("Inventory", "No records updated. Please check the crop name.")
            else:
            # If rows were affected, show success message
                messagebox.showinfo("Inventory", "Added")
            
        except mysql.connector.Error as e:
            print("Error:", e)
            messagebox.showerror("Inventory", "Try Again")
 

    def show_items(self):
        self.display_users()




root = tk.Tk()
conn = mysql.connector.connect(host='localhost',port='3307',username='root',password='0000',database='reg')
my_cursor=conn.cursor()
InventoryApp(root,my_cursor)
root.mainloop()




        
