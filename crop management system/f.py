
from tkinter import *
from tkinter import messagebox
import mysql.connector

class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("LOGIN")
        self.master.geometry('925x500+300+200')
        self.master.config(bg="#fff")
        self.master.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        self.img = PhotoImage(file='login.png')
        Label(self.master, image=self.img, bg='white').place(x=50, y=50)

        self.frame = Frame(self.master, width=350, height=350, bg="white")
        self.frame.place(x=480, y=70)

        heading = Label(self.frame, text='Sign IN', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
        heading.place(x=100, y=5)

        self.user = Entry(self.frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Username')
        self.user.bind('<FocusIn>', self.on_enter_user)
        self.user.bind('<FocusOut>', self.on_leave_user)

        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=107)

        self.code = Entry(self.frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
        self.code.place(x=30, y=150)
        self.code.insert(0, 'Password')
        self.code.bind('<FocusIn>', self.on_enter_code)
        self.code.bind('<FocusOut>', self.on_leave_code)
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=177)

        Button(self.frame, width=39, pady=7, text='Sign IN', bg='#57a1f8', fg='white', border=0, command=self.lgn).place(x=35, y=204)

        label = Label(self.frame, text="Don't have an account?", fg='black', bg='white',
                      font=('Microsoft Yahei UI Light', 9))
        label.place(x=75, y=270)

        sign_up = Button(self.frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=self.register)
        sign_up.place(x=215, y=270)

    def lgn(self):
        try:
            conn = mysql.connector.connect(host='localhost', port='3307', user='root', password='0000', database='reg')
            us = self.user.get()
            pswd = self.code.get()

            my_cursor = conn.cursor()
            command = "SELECT * FROM rdtl WHERE username=%s AND password=%s"

            my_cursor.execute(command, (us, pswd))
            myresult = my_cursor.fetchone()

            if myresult is None:
                messagebox.showinfo("Invalid", "Invalid username and password")
            else:
                messagebox.showinfo("Login", "Successful")
                self.master.destroy()
                import mm
            my_cursor.close()
            conn.close()
            

        except mysql.connector.Error as e:
            messagebox.showerror("Connection Error", str(e))

    def register(self):
        self.master.destroy()
        import reg

    def on_enter_user(self, e):
        self.user.delete(0, 'end')

    def on_leave_user(self, e):
        name = self.user.get()
        if name == '':
            self.user.insert(0, 'Username')

    def on_enter_code(self, e):
        self.code.delete(0, 'end')

    def on_leave_code(self, e):
        name = self.code.get()
        if name == '':
            self.code.insert(0, 'Password')


root = Tk()
app = LoginApp(root)
root.mainloop()
