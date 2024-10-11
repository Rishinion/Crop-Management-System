from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
from tkinter import messagebox
import tempfile
import os
from time import strftime

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("AV")
        
        #-----------------------------------------------
        self.c_name=StringVar()
        self.c_phno=StringVar()
        self.bill_no=StringVar()
        self.c_email=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        


        
        #Product Categories List

        self.Category=["Select Option","Vegetables","Grains"]
        
        #Sub category vegetable

        self.SubCatVegetables=["LeafGreen","RootVegetables","CruciferousVegetables"]
        self.LeafGreen=["Spinach", "Lettuce", "Kale", "Swiss Chard"]
        self.price_Spinach=12
        self.price_Lettuce=18
        self.price_Kale=14 
        self.price_SwissChard=18

        self.RootVegetables=["Carrots", "Potatoes", "Beets", "Turnips"]
        self.price_Carrots=20
        self.price_Potatoes=16
        self.price_Beets=14
        self.price_Turnips=18

        self.CruciferousVegetables=["Broccoli", "Cauliflower", "BrusselsSprouts", "Cabbage"]
        self.price_Broccoli=30
        self.price_Cauliflower=28
        self.price_BrusselsSprouts=32
        self.price_Cabbage=19


        #sub category Grains


        self.SubCatGrains=["Wheat","Rice","Corn","Barley"]

        self.Wheat=["Durum", "HardRedSpring", "HardRedWinter", "BrownRice"]
        self.price_Durum=34
        self.price_HardRedSpring=24
        self.price_HardRedWinter=28
        self.price_SoftWhite=36

        self.Rice=["Basmati", "Jasmine", "Arborio", "BrownRice"]  
        self.price_Basmati=22
        self.price_Jasmine=18
        self.price_Arborio=40
        self.price_BrownRice=58


        self.Corn=["SweetCorn", "FieldCorn", "Popcorn", "FlintCorn"]
        self.price_SweetCorn=12
        self.price_FieldCorn=14
        self.price_Popcorn=20
        self.price_FlintCorn=10

        self.Barley=["Hulled", "Pearled", "BarleyFlour", "BarleyGrits"]
        self.price_Hulled=34
        self.price_Pearled=24
        self.price_BarleyFlour=18
        self.price_BarleyGrits=36

        self.LeafGreen=["Spinach", "Lettuce", "Kale", "SwissChard"]
        self.price_Spinach=12
        self.price_Lettuce=24
        self.price_Kale=22
        self.price_SwissChard=36

        
        
    
       

        lbl_title=Label(self.root,text="CROP MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=130,width=1530,height=45)

        def time():
            String=strftime('%H:%M:%S %p')
            lbl.config(text=String)
            lbl.after(1000,time)

        lbl=Label(lbl_title,font=("times new roman",16,"bold"),background='white',foreground='blue')
        lbl.place(x=0,y=(-15),width=120,height=50)
        time()


        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)

        #custm label

        cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lbl_mob=Label(cust_Frame,text="Mobile no",font=("times new roman",12,"bold"),bg="white",fg="black")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(cust_Frame,textvariable=self.c_phno,font=("times new roman",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        self.lblCustName=Label(cust_Frame,font=("arial",12,"bold"),bg="white",text="Customer Name",fg="black")
        self.lblCustName.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(cust_Frame,textvariable=self.c_name,font=("arial",10,"bold"),width=24)
        self.txtCustName.grid(row=1,column=1,stick=W,padx=5,pady=2)

        self.lblEmail=Label(cust_Frame,font=("arial",12,"bold"),bg="white",text="Email",fg="black")
        self.lblEmail.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(cust_Frame,textvariable=self.c_email,font=("arial",10,"bold"),width=24)
        self.txtEmail.grid(row=2,column=1,stick=W,padx=5,pady=2)

#######_-------------------------
        #product label

        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=630,height=140)

        #category 

        self.lblCategory=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Select Categories",bd=4)
        self.lblCategory.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,stick=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        #subcategory

        self.lblSubCategory=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text=" Subcategories",bd=4)
        self.lblSubCategory.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[""],font=("arial",10,"bold"),width=24,state="readonly")
        self.ComboSubCategory.grid(row=1,column=1,stick=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        #Product Name

        self.lblProduct=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text=" Product Name",bd=4)
        self.lblProduct.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,font=("arial",10,"bold"),width=24,state="readonly")
        self.ComboProduct.grid(row=2,column=1,stick=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)
        
        #Price
        self.lblPrice=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text=" Price",bd=4)
        self.lblPrice.grid(row=0,column=2,stick=W,padx=5,pady=2)

        self.ComboPrice=ttk.Combobox(Product_Frame,textvariable=self.prices,font=("arial",10,"bold"),width=24,state="readonly")
        self.ComboPrice.grid(row=0,column=3,stick=W,padx=5,pady=2)

        #Qty

        self.lblQty=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text=" Qty",bd=4)
        self.lblQty.grid(row=1,column=2,stick=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=("arial",10,"bold"),width=24,state="readonly")
        self.ComboQty.grid(row=1,column=3,stick=W,padx=5,pady=2)
         

        #Middle 
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=980,height=340)

        #search
        Serach_Frame=Frame(Main_Frame,bd=2,bg="white")
        Serach_Frame.place(x=1020,y=15,width=500,height=40)

        self.lblBill=Label(Serach_Frame,font=("arial",12,"bold"),fg="white",bg="red",text="Bill Number")
        self.lblBill.grid(row=0,column=0,stick=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(Serach_Frame,textvariable=self.search_bill,font=("arial",10,"bold"),width=24)
        self.txt_Entry_Search.grid(row=0,column=1,stick=W,padx=2)

        self.BtnSearch=Button(Serach_Frame,command=self.find_bill,text=" Search",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)


        #Bill Area

        RightLabelFrame=LabelFrame(Main_Frame,text="Bill",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1020,y=45,width=480,height=440)


        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg='white',fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #Bill Label

        Button_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        Button_Frame.place(x=0,y=485,width=1520,height=125)

        
        self.lblSubTotal=Label(Button_Frame,font=("arial",12,"bold"),bg="white",text=" Sub Total",bd=4)
        self.lblSubTotal.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.EntrySubTotal=ttk.Entry(Button_Frame,font=("arial",10,"bold"),width=26)
        self.EntrySubTotal.grid(row=0,column=1,stick=W,padx=5,pady=2)

        self.lbl_tax=Label(Button_Frame,font=("arial",12,"bold"),bg="white",text=" Tax(gst)",bd=4)
        self.lbl_tax.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Button_Frame,font=("arial",10,"bold"),width=26)
        self.txt_tax.grid(row=1,column=1,stick=W,padx=5,pady=2)

        self.lblAmountTotal=Label(Button_Frame,font=("arial",12,"bold"),bg="white",text=" Amount Total",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.txtAmountTotal=ttk.Entry(Button_Frame,font=("arial",10,"bold"),width=26)
        self.txtAmountTotal.grid(row=2,column=1,stick=W,padx=5,pady=2)


        #Button

        Btn_Frame=Frame(Button_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add to cart",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngenerate=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Btngenerate.grid(row=0,column=1)

        self.BtnSave=Button(Btn_Frame,height=2,command=self.save_bill,text="Save Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint=Button(Btn_Frame,height=2,command=self.iprint,text="Print",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,height=2,command=self.clear,text="Clear",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,height=2,command=self.root.destroy,text=" Exit",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()

        self.l=[]

    #=====================================Funtion==========================

    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n 
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("ERROR","Select product name")

        else:
            self.textarea.insert(END,f"\n{self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f' % (sum(self.l))))
            self.tax_input.set(str('Rs.%.2f' % ((((sum(self.l))-float(self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f' % (((sum(self.l))+((((sum(self.l))-float(self.prices.get()))*Tax)/100)))))



    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Item")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n===============================================")
            self.textarea.insert(END,f"\nSub Amount\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\nTax Amount\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\nTotal Amount\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n===============================================")


    def save_bill(self):
        op=messagebox.askyesno("SAVE BILL","Do you want to save the bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("SAVE",f"Bill No:{self.bill_no.get()} Saved Successfully")
            f1.close

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mkdtemp(',txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")


    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                    f1=open(f'bills/{i}','r')
                    self.textarea.delete(1.0,END)
                    for d in f1:
                            self.textarea.insert(END,d)
                    f1.close()
                    found="yes"
            if found=="no":
                    messagebox.showerror("ERROR","INVALID")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phno.set("")
        self.c_email.set("")
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.bill_no.set("")
        self.search_bill.set("")
        self.product.set("")
        self.prices.set("")
        self.qty.set("")
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()



    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t Welcome")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phno.get()}")
        self.textarea.insert(END,f"\n E-mail:{self.c_email.get()}")

        self.textarea.insert(END,"\n===============================================")
        self.textarea.insert(END,f"\n Products\t\t\tQTY\t\tPrice")
        self.textarea.insert(END,"\n===============================================")

        
        

    def Categories(self,event=""):
        if self.Combo_Category.get()=="Vegetables":
            self.ComboSubCategory.config(value=self.SubCatVegetables)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Grains":
            self.ComboSubCategory.config(value=self.SubCatGrains)
            self.ComboSubCategory.current(0)

    def Product_add(self,event=""):
        if self.ComboSubCategory.get()=="LeafGreen":
            self.ComboProduct.config(value=self.LeafGreen)
            self.ComboProduct.current(0)


        if self.ComboSubCategory.get()=="RootVegetables":
            self.ComboProduct.config(value=self.RootVegetables)
            self.ComboProduct.current(0)


        if self.ComboSubCategory.get()=="CruciferousVegetables":
            self.ComboProduct.config(value=self.CruciferousVegetables)
            self.ComboProduct.current(0)

        #=["Wheat","Rice","Corn","Barley"]

        if self.ComboSubCategory.get()=="Wheat":
            self.ComboProduct.config(value=self.Wheat)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Rice":
            self.ComboProduct.config(value=self.Rice)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Corn":
            self.ComboProduct.config(value=self.Corn)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Barley":
            self.ComboProduct.config(value=self.Barley)
            self.ComboProduct.current(0)



        
    def price(self,event=""):

        # self.LeafGreen=["Spinach", "Lettuce", "Kale", "SwissChard"]
       
        if self.ComboProduct.get()=="Spinach":
            self.ComboPrice.config(value=self.price_Spinach)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Lettuce":
            self.ComboPrice.config(value=self.price_Lettuce)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Kale":
            self.ComboPrice.config(value=self.price_Kale)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="SwissChard":
            self.ComboPrice.config(value=self.price_SwissChard)
            self.ComboPrice.current(0)
            self.qty.set(1)
        


        #self.RootVegetables=["Carrots", "Potatoes", "Beets", "Turnips"]


        if self.ComboProduct.get()=="Carrots":
            self.ComboPrice.config(value=self.price_Carrots)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Potatoes":
            self.ComboPrice.config(value=self.price_Potatoes)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Beets":
            self.ComboPrice.config(value=self.price_Beets)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Turnips":
            self.ComboPrice.config(value=self.price_Turnips)
            self.ComboPrice.current(0)
            self.qty.set(1)



        #self.CruciferousVegetables=["Broccoli", "Cauliflower", "BrusselsSprouts", "Cabbage"]
       

        if self.ComboProduct.get()=="Broccoli":
            self.ComboPrice.config(value=self.price_Broccoli)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Cauliflower":
            self.ComboPrice.config(value=self.price_Cauliflower)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="BrusselsSprouts":
            self.ComboPrice.config(value=self.price_BrusselsSprouts)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Cabbage":
            self.ComboPrice.config(value=self.price_Cabbage)
            self.ComboPrice.current(0)
            self.qty.set(1)


        # self.Wheat=["Durum", "HardRedSpring", "HardRedWinter", "BrownRice"]
       

        if self.ComboProduct.get()=="Durum":
            self.ComboPrice.config(value=self.price_Durum)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="HardRedSpring":
            self.ComboPrice.config(value=self.price_HardRedSpring)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="HardRedWinter":
            self.ComboPrice.config(value=self.price_HardRedWinter)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="BrownRice":
            self.ComboPrice.config(value=self.price_BrownRice)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #self.Rice=["Basmati", "Jasmine", "Arborio", "BrownRice"]  

        if self.ComboProduct.get()=="Basmati":
            self.ComboPrice.config(value=self.price_Basmati)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Jasmine":
            self.ComboPrice.config(value=self.price_Jasmine)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Arborio":
            self.ComboPrice.config(value=self.price_Arborio)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="BrownRice":
            self.ComboPrice.config(value=self.price_BrownRice)
            self.ComboPrice.current(0)
            self.qty.set(1)


        #self.Corn=["SweetCorn", "FieldCorn", "Popcorn", "FlintCorn"] 

        if self.ComboProduct.get()=="SweetCorn":
            self.ComboPrice.config(value=self.price_SweetCorn)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="FieldCorn":
            self.ComboPrice.config(value=self.price_FieldCorn)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Popcorn":
            self.ComboPrice.config(value=self.price_Popcorn)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="FlintCorn":
            self.ComboPrice.config(value=self.price_FlintCorn)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #self.Barley=["Hulled", "Pearled", "BarleyFlour", "BarleyGrits"] 

        if self.ComboProduct.get()=="Hulled":
            self.ComboPrice.config(value=self.price_Hulled)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Pearled":
            self.ComboPrice.config(value=self.price_Pearled)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="BarleyFlour":
            self.ComboPrice.config(value=self.price_BarleyFlour)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="BarleyGrits":
            self.ComboPrice.config(value=self.price_BarleyGrits)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #self.LeafGreen=["Spinach", "Lettuce", "Kale", "SwissChard"]

        if self.ComboProduct.get()=="Spinach":
            self.ComboPrice.config(value=self.price_Spinach)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Lettuce":
            self.ComboPrice.config(value=self.price_Lettuce)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Kale":
            self.ComboPrice.config(value=self.price_Kale)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="SwissChard":
            self.ComboPrice.config(value=self.price_SwissChard)
            self.ComboPrice.current(0)
            self.qty.set(1)



if __name__ == '__main__':
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()
