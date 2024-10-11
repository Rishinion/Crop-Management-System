from tkinter import *


class MainMenu(Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Menu")
        self.geometry("925x500+300+200")
        self.configure(bg="#fff")
        self.resizable(False, False)

        self.heading = Label(self, text='Main Menu', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light', 28, 'bold'))
        self.heading.place(x=360, y=50)

        self.frame = Frame(self, width=700, height=350, bg="white")
        self.frame.place(x=120, y=100)

        self.add_button = Button(self.frame, width=30, pady=10, text='Add Inventory', bg='#57a1f8', fg='white',
                                 font=('Microsoft Yahei UI Light', 18, 'bold'), border=5, command=self.ad)
        self.add_button.place(x=120, y=30)

        self.bill_button = Button(self.frame, width=30, pady=10, text='Bill', bg='#57a1f8', fg='white',
                                  font=('Microsoft Yahei UI Light', 18, 'bold'), border=5, command=self.bl)
        self.bill_button.place(x=120, y=130)

        # Button(self.frame, width=30, pady=10, text="Items", bg='#57a1f8', fg='white',
        #        font=('Microsoft Yahei UI Light', 18, 'bold'), border=5).place(x=120, y=230)

    def ad(self):
        self.destroy()
        import add1

    def bl(self):
        self.destroy()
        import test


app = MainMenu()
app.mainloop()







'''from tkinter import *



window=Tk()
window.title("Main Menu")
window.geometry("925x500+300+200")
window.configure(bg="#fff")
window.resizable(False,False)

def ad():
    window.destroy()
    import add1

    

def bl():
    window.destroy()
    import test

heading = Label(window,text='Main Menu',fg='#57a1f8',bg='white',font=('Miscrosoft Yahei UI Light',28,'bold'))
heading.place(x=360,y=50)

frame=Frame(window,width=700,height=350,bg="white")
frame.place(x=120,y=100)


Button(frame,width=30,pady=10,text='Add Inventory',bg='#57a1f8',fg='white',font=('Miscrosoft Yahei UI Light',18,'bold'),border=5,command=ad).place(x=120,y=30)

Button(frame,width=30,pady=10,text='Bill',bg='#57a1f8',fg='white',font=('Miscrosoft Yahei UI Light',18,'bold'),border=5,command=bl).place(x=120,y=130)

#Button(frame,width=30,pady=10,text="Items",bg='#57a1f8',fg='white',font=('Miscrosoft Yahei UI Light',18,'bold'),border=5).place(x=120,y=230)

window.mainloop()'''