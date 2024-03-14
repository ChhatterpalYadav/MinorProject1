from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import os
from subprocess import call
 
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry('350x500')
    register_screen.iconbitmap('favicon.ico')
    register_screen.configure(background='#0096DC')
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg='#0096DC',fg='white',font=('verdana',17)).pack()
    Label(register_screen, text="",bg='#0096DC').pack(pady=(20,5))
    username_lable = Label(register_screen, text="Username * ",bg='#0096DC',fg='white',font=('verdana',10))
    username_lable.pack(ipady=6,pady=(20,5)) 
    username_entry = Entry(register_screen, textvariable=username,width=50)
    username_entry.pack(ipady=6,pady=(20,5))
    password_lable = Label(register_screen, text="Password * ",bg='#0096DC',fg='white',font=('verdana',10))
    password_lable.pack(ipady=6,pady=(20,5))
    password_entry = Entry(register_screen, textvariable=password, show='*',width=50)
    password_entry.pack(ipady=6,pady=(20,5))
    Label(register_screen, text="",bg='#0096DC',fg='white',font=('verdana',10)).pack(pady=(20,5))
    Button(register_screen, text="Register", width=10, height=1, bg='white', command = register_user).pack(pady=(20,5))
 
 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry('350x500')
    login_screen.configure(background='#0096DC')
    Label(login_screen, text="Please enter details below to login",bg='#0096DC',fg='white',font=('verdana',10)).pack()
    Label(login_screen, text="",bg='#0096DC').pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ",bg='#0096DC',fg='white',font=('verdana',20)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify,width=50)
    username_login_entry.pack(ipady=6,pady=(20,5))
    Label(login_screen, text="",bg='#0096DC',fg='white',font=('verdana',20)).pack()
    Label(login_screen, text="Password * ",bg='#0096DC',fg='white',font=('verdana',20)).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*',width=50)
    password_login_entry.pack(ipady=6,pady=(20,5))
    Label(login_screen, text="",bg='#0096DC',fg='white',font=('verdana',10)).pack()
    Button(login_screen, text="Login", width=40, height=2, command = login_verify).pack()
 

 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 

 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 

 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry('350x500')
    login_success_screen.iconbitmap('favicon.ico')
    login_success_screen.configure(background='#0096DC')
    Label(login_success_screen, text="Login Success",bg='#0096DC',fg="green",font=('verdana',15)).pack()
    Label(login_success_screen, text="Welcome JIITIAN",bg='#0096DC',fg="white",font=('verdana',10)).pack()
    Label(login_success_screen, text="Choose One From Below Options: ",bg='#0096DC',fg="white",font=('verdana',10)).pack()
    Button(login_success_screen, text="Sign Language",width=40, height=2,command=signLanguage).place(x=30,y=80)
    Button(login_success_screen, text="Air Brush",width=40, height=2, command=airBrush).place(x=30,y=160)
    Button(login_success_screen, text="Eye Lid Control", width=40, height=2,command=eyeLidControl).place(x=30,y=240)
    Button(login_success_screen, text="Eye Blink Game", width=40, height=2,command=eyeblinkControl).place(x=30,y=320)
    Button(login_success_screen, text="Project Idea Generator", width=40, height=2,command=projectIdea).place(x=30,y=400)
    
    
    

def signLanguage():
    os.system('python inference_classifier.py')

def airBrush():
    os.system('python virtual.py')

def eyeLidControl():
    os.system('python eyelidcontrol.py')

def eyeblinkControl():
    os.system('python SpaceButton.py')

def projectIdea():
    os.system('python m.py')


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry('350x500')
    password_not_recog_screen.iconbitmap('favicon.ico')
    password_not_recog_screen.configure(background='#0096DC')
    Label(password_not_recog_screen, text="Invalid Password ",bg='#0096DC',fg='white',font=('verdana',20)).pack()
    Label(password_not_recog_screen, text="",bg='#0096DC').pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

 

 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry('350x500')
    user_not_found_screen.iconbitmap('favicon.ico')
    user_not_found_screen.configure(background='#0096DC')
    Label(user_not_found_screen, text="User Not Found",bg='#0096DC',fg='white',font=('verdana',20)).pack()
    Label(user_not_found_screen, text="",bg='#0096DC').pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 

 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 

 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry('350x500')
    main_screen.title("Account Login")
    main_screen.iconbitmap('favicon.ico')
    main_screen.configure(background='#0096DC')
    img = Image.open('./img1.png')
    resized_img = img.resize((90,90))
    img = ImageTk.PhotoImage(resized_img)
    img_label = Label(main_screen,image=img)
    img_label.pack(pady=(10,10))
    text_label = Label(main_screen,text='EmpowerPy',fg='white',bg='#0096DC')
    text_label.pack()
    text_label.config(font=('verdana',24))
    Label(text="Select Your Choice",width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="",bg='#0096DC').pack(pady=(20,5))
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="",bg='#0096DC').pack(pady=(20,5))
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()