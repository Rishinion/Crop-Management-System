from tkinter import *
from tkinter import messagebox
import mysql.connector

#from dbcon import cn

def insert():   
    try:
        conn = mysql.connector.connect(host='localhost', port='3307', username='root', password='0000', database='reg')
        un = uname.get()
        us = user.get()
        phn = phno.get()
        pswd = code.get()
        cpswd = confirm_code.get()

        # Validate username length
        if len(us) < 6:
            messagebox.showerror("Invalid", "Username must be at least 6 characters long")
            return
        
        # Validate password length
        if len(pswd) < 8:
            messagebox.showerror("Invalid", "Password must be at least 8 characters long")
            return
        
        # Validate name to contain only alphabets
        if not un.isalpha():
            messagebox.showerror("Invalid", "Name must contain only alphabets")
            return
        
        # Validate phone number length and content
        if not (len(phn) == 10 and phn.isdigit()):
            messagebox.showerror("Invalid", "Phone number must be numeric and of 10  digits")
            return
        
        if pswd == cpswd:
            my_cursor = conn.cursor()
            command = "insert into rdtl(name, username, phonenumber, password) value(%s, %s, %s, %s)"

            my_cursor.execute(command, (un, us, phn, pswd))
            conn.commit()
            messagebox.showinfo("Sign up", "Registered")
            print("Connected!")
            
        else:
            messagebox.showinfo("Signup", "Password doesn't match")
    except mysql.connector.Error as e:
        messagebox.showerror("Connection", str(e))
    finally:
        my_cursor.close()
        conn.close()

    
    
def login():
    window.destroy()
    import project
    
    
    


window=Tk()
window.title("Sign up")
window.geometry("1530x800+0+0")
window.configure(bg='#fff')
window.resizable(False,False)




    


img=PhotoImage(file='reg.png')
Label(window,image=img,border=0,bg='white').place(x=100,y=200)

frame=Frame(window,width=800,height=700,bg='#fff')
frame.place(x=700,y=30)

heading=Label(frame,text='SIGN UP',fg='#57a1f8',bg='white',font=('Miscrosoft Yahei UI Light',30))
heading.place(x=100,y=5)



########-----------------------------------------------------

def on_enter(e):
    uname.delete(0,'end')

def on_leave(e):
    name=uname.get()
    if name=='':
        uname.insert(0,'Name')

uname = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Miscrosoft Yahie UI Light',30))
uname.place(x=30,y=80)
uname.insert(0,'Name')
uname.bind("<FocusIn>",on_enter)
uname.bind("<FocusOut>",on_leave)

Frame(frame,width=350,height='2',bg='black').place(x=25,y=130)

#####--------------------------------------------------



def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')


user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Miscrosoft Yahie UI Light',30))
user.place(x=30,y=150)
user.insert(0,'Username')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame,width=350,height='2',bg='black').place(x=25,y=200)

########-----------------------------------------------------


def on_enter(e):
    phno.delete(0,'end')

def on_leave(e):
    name=phno.get()
    if name=='':
        phno.insert(0,'Phone Number')


phno = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Miscrosoft Yahie UI Light',30))
phno.place(x=30,y=220)
phno.insert(0,'Phone Number')
phno.bind("<FocusIn>",on_enter)
phno.bind("<FocusOut>",on_leave)

Frame(frame,width=350,height='2',bg='black').place(x=25,y=270)

######------------------------------------


def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')


code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Miscrosoft Yahie UI Light',30))
code.place(x=30,y=290)
code.insert(0,'Password')
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)

Frame(frame,width=350,height='2',bg='black').place(x=25,y=340)

######------------------------------------

def on_enter(e):
    confirm_code.delete(0,'end')

def on_leave(e):
    name=confirm_code.get()
    if name=='':
        confirm_code.insert(0,'confirm code')


confirm_code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Miscrosoft Yahie UI Light',30))
confirm_code.place(x=30,y=360)
confirm_code.insert(0,'confirm Password')
confirm_code.bind("<FocusIn>",on_enter)
confirm_code.bind("<FocusOut>",on_leave)

Frame(frame,width=350,height='2',bg='black').place(x=25,y=410)

#-------------------------------------------------------------------


Button(frame,width=39,pady=7,text='SIGNUP',bg='#57a1f8',fg='white',border=8,command=insert).place(x=60,y=430)
Label=Label(frame,text='I have an account...',fg='black',bg='white',font=('Miscrosoft Yahei UI Light',12))
Label.place(x=150,y=500)

signin=Button(frame,width=6,text='sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=login,font=('Miscrosoft Yahei UI Light',12))
signin.place(x=280,y=500)





window.mainloop()