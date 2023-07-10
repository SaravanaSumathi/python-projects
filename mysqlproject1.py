import tkinter as tk

from tkinter.messagebox import showinfo
import mysql.connector as sqlct



def createdb():
    global mycn
    global mycur
    
    mycn=sqlct.connect(host="localhost",user="root",password="Saravanasumathi@4",database="sumathi")
    if mycn.is_connected():
        print("\t\tlogin and register form using tkinter .")
    mycur=mycn.cursor()
    cmd1 = "create table if not exists signin (Email varchar(100),password varchar(100))"
    mycur.execute(cmd1)
    cmd2 = "create table if not exists register (Email varchar(100),UserName varchar(100),password varchar(100),confirm_password varchar(100))"
    mycur.execute(cmd2)
createdb()
root = tk.Tk()


email = tk.StringVar()
password = tk.StringVar()
username = tk.StringVar()
confirm_password = tk.StringVar()


#inserting
def insert_login():
    email1 = email_entry.get()
    password1 = password_entry.get()
    
    try:
        for i in range(len(res1)): #range(4) -> i = 0
            if email1 == res1[i][0] and password1 == res1[i][2]:
                #email1 == res1[0][0] and 
                msg = f'Welcome to our page {res1[i][1]}'
                showinfo(
                    title='Information',
                    message=msg
                )
                cmd3 = "insert into signin values ('"+str(email1)+"','"+str(password1)+"')"
    
                mycur.execute(cmd3)
                mycn.commit()
    except:
        msg = f'sorry you are not registered.'
        showinfo(
                    title='Information',
                    message=msg
                )
        

    
def show_data():
    global res
    root3 = tk.Tk()
    root3.geometry("500x500")
    cmd5 = "select * from signin"
    mycur.execute(cmd5)
    res = mycur.fetchall()
    signin3 = tk.Frame(root3,bg="lightgreen",bd=5,highlightbackground="pink",highlightthickness=5)
    signin3.pack(padx=10, pady=10, expand=True)
    data1 = tk.Label(signin3, text= "Email",bg="lightgreen",fg="white",font="bold",width=32,bd=5,highlightbackground="pink",highlightthickness=5)
    data1.grid(row=0,column=1,padx = 5, pady = 5)
    data2 = tk.Label(signin3, text= "Password",bg="lightgreen",fg="white",font="bold",width=32,bd=5,highlightbackground="pink",highlightthickness=5)
    data2.grid(row=0,column=2,padx = 5, pady = 5)
    for i in range(len(res)):
        for j in range(len(res[i])):
            data = tk.Label(signin3, text= res[i][j],bg="lightgreen",fg="red",width=50,bd=5,highlightbackground="pink",highlightthickness=5)
            data.grid(row=i+1,column=j+1,padx = 5, pady = 5)
            
    
#show_data()
def chesvi():
    root1 = tk.Tk()
    root1.geometry("500x2000")
    global email_entry
    global password_entry
    signin1 = tk.Frame(root1,bg="lightgreen",bd=5,highlightbackground="pink",highlightthickness=5,height=600)
    
    signin1.place(x=150,y=150)
    login = tk.Label(signin1, text="LOGIN FORM",bg="lightgreen",fg="white",font=("Lucida Calligraphy",30,"bold"),width=32)
    
    login.grid(row=0,column=1, columnspan = 2, pady=20)
# email
    email_label = tk.Label(signin1, text="Email Address:",bg="lightgreen",fg="white",font="bold",width=32,bd=5,highlightbackground="pink",highlightthickness=5)
    
    email_label.grid(row=1,column=1, pady=20)
    
    email_entry = tk.Entry(signin1, textvariable=email,bg="lightgreen",fg="white",font="bold",width=32,bd=5,highlightbackground="pink",highlightthickness=5)
    
    email_entry.grid(row=1,column=2, pady=20)
    

# password
    password_label = tk.Label(signin1, text="Password:",bg="lightgreen",fg="white",font="bold",width=32,bd=5,highlightbackground="pink",highlightthickness=5)
    
    password_label.grid(row=2,column=1, pady=20)

    password_entry = tk.Entry(signin1, textvariable=password, show="*",bg="lightgreen",fg="white",font="bold",width=32,bd=5,highlightbackground="pink",highlightthickness=5)
    
    password_entry.grid(row=2,column=2, pady=20)
    

# login button
    login_button = tk.Button(signin1, text="Login",command=insert_login,bg="lightgreen",fg="white",font="bold",width=32,bd=5,highlightbackground="pink",highlightthickness=5)
    
    login_button.grid(row=3,column=1, columnspan = 2, pady=20)

def show_data1():
    global res1
    root4 = tk.Tk()
    cmd6 = "select * from register"
    mycur.execute(cmd6)
    res1 = mycur.fetchall()
    signin4 = tk.Frame(root4)
    signin4.pack(padx=20, pady=10,fill='x', expand=True)
    data1 = tk.Label(signin4, text= "Email",bg="lightgreen",fg="white",font="bold",width=25,bd=5,highlightbackground="pink",highlightthickness=5)
    data1.grid(row=0,column=1,padx = 5, pady = 5)
    data2 = tk.Label(signin4, text= "User Name",bg="lightgreen",fg="white",font="bold",width=25,bd=5,highlightbackground="pink",highlightthickness=5)
    data2.grid(row=0,column=2,padx = 5, pady = 5)
    data3 = tk.Label(signin4, text= "Password",bg="lightgreen",fg="white",font="bold",width=25,bd=5,highlightbackground="pink",highlightthickness=5)
    data3.grid(row=0,column=3,padx = 5, pady = 5)
    data4 = tk.Label(signin4, text= "Confirm_password",bg="lightgreen",fg="white",font="bold",width=25,bd=5,highlightbackground="pink",highlightthickness=5)
    data4.grid(row=0,column=4,padx = 5, pady = 5)
    for i in range(len(res1)): #4 -> range(4) -> 0,3 -> i = 1
        for j in range(len(res1[i])): #range(len(res1[0]))->range(4) ->0,3
            data = tk.Label(signin4, text= res1[i][j],bg="lightgreen",fg="red",width=39,bd=5,highlightbackground="pink",highlightthickness=5)
            #res1[1][3]
            data.grid(row=i+1,column=j+1,padx = 5, pady = 5)
            
    
#show_data1()

def insert_signup():
    email1 = email_entry.get()
    user = user_entry.get()
    password1 = password_entry.get()
    confirm = password1_entry.get()
  
    if password_entry.get() == password1_entry.get():
            
            cmd4 = "insert into register values ('"+str(email1)+"','"+str(user)+"','"+str(password1)+"','"+str(confirm)+"')"
    
            mycur.execute(cmd4)
            mycn.commit()
            msg = f'Successfully Registered.'
            showinfo(
                    title='Information',
                    message=msg

              )
    else:
            msg = f'password and confirm password does not match'
            showinfo(
                    title='Information',
                    message=msg
                )
            


def pooji():
    root2 = tk.Tk()
    global email_entry
    global password_entry
    global user_entry
    global password1_entry
    signin2 = tk.Frame(root2,bg="lightgreen",bd=5,highlightbackground="pink",highlightthickness=5,height=600)
    
    signin2.place(x=150,y=50)
    login = tk.Label(signin2, text="REGISTER FORM",bg="lightgreen",fg="white",font=("Lucida Calligraphy",30,"bold"),width=32)
    
    login.grid(row=0,column=1, columnspan = 2, pady=20)

# email
    email_label = tk.Label(signin2, text="Email Address:",bg="lightgreen",fg="white",font="bold",width=32,bd=5,highlightbackground="pink",highlightthickness=5)
    
    email_label.grid(row=1,column=1, pady=20)

    email_entry = tk.Entry(signin2, textvariable=email,bg="lightgreen",fg="white",font="bold",width=32,bd=5,highlightbackground="pink",highlightthickness=5)
    
    email_entry.grid(row=1,column=2, pady=20)
# user name
    user_label = tk.Label(signin2, text="User Name:",bg="lightgreen",fg="white",font="bold",width=32,bd=5,highlightbackground="pink",highlightthickness=5)
    
    user_label.grid(row=2,column=1, pady=20)

    user_entry = tk.Entry(signin2, textvariable=username,bg="lightgreen",fg="white",font="bold",width=32,bd=5,highlightbackground="pink",highlightthickness=5)
    
    user_entry.grid(row=2,column=2, pady=20)
# password
    password_label = tk.Label(signin2, text="Password:",bg="lightgreen",fg="white",font="bold",width=32,bd=5,highlightbackground="pink",highlightthickness=5)
    
    password_label.grid(row=3,column=1, pady=20)

    password_entry = tk.Entry(signin2, textvariable=password, show="*",bg="lightgreen",fg="white",font="bold",width=32,bd=5,highlightbackground="pink",highlightthickness=5)
    
    password_entry.grid(row=3,column=2, pady=20)

# confirm password
    password1_label = tk.Label(signin2, text="confirm Password:",bg="lightgreen",fg="white",font="bold",width=32,bd=5,highlightbackground="pink",highlightthickness=5)
    
    password1_label.grid(row=4,column=1, pady=20)

    password1_entry = tk.Entry(signin2, textvariable=confirm_password, show="*",bg="lightgreen",fg="white",font="bold",width=32,bd=5,highlightbackground="pink",highlightthickness=5)
    
    password1_entry.grid(row=4,column=2, pady=20)

# login button
    login_button = tk.Button(signin2, text="Register",command=insert_signup,bg="lightgreen",fg="white",font="bold",width=32,bd=5,highlightbackground="pink",highlightthickness=5)
    
    login_button.grid(row=5,column=1, columnspan = 2, pady=20)
    

    
signin = tk.Frame(root,bg="pink",width=1200,highlightbackground="lightgreen",highlightthickness=5,height=400).place(x=50,y=80)

login_button = tk.Button(signin, text="Login", command=chesvi,bg="lightgreen",fg="white",font="bold",width=32,bd=5,highlightbackground="pink",highlightthickness=5)
login_button.place(x=200, y=150)

login_button1 = tk.Button(signin, text="signup",command=pooji,bg="lightgreen",fg="white",font="bold",width=32,bd=5,highlightbackground="pink",highlightthickness=5)
login_button1.place(x=800, y=150)

login_button3 = tk.Button(signin, text="Show Login form data",command=show_data,bg="lightgreen",fg="white",font="bold",width=32,bd=5,highlightbackground="pink",highlightthickness=5)
login_button3.place(x=200, y=350)

login_button4 = tk.Button(signin, text="Show Register form data",command=show_data1,bg="lightgreen",fg="white",font="bold",width=32,bd=5,highlightbackground="pink",highlightthickness=5)
login_button4.place(x=800, y=350)

root.mainloop()
