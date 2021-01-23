import os
from tkinter import *
from tkinter import Tk, ttk, messagebox, Label, Text

root=Tk()
root.title('Password Manager')
root.configure(background='black')
root.geometry("520x280")

class RootLabel:
    def __init__(self,text,foreground,x,y):
        self = Label(root,text = text, background="black",foreground=foreground,font=("Helvetica", 16, "bold"))
        self.place(x=x,y=y)

RootLabel("Password Manager","yellow",48,10)
RootLabel("Root password:"       ,"Green",48,50)
RootLabel("SSH IP:"       ,"Green",48,90)
RootLabel("SSH User:"       ,"Green",48,130)
RootLabel("SSH Password:"      ,"Green",48,170)

RootPasswd = Entry(root,font=("Helvetica", 16, "bold"),foreground="yellow", background="#1E1E1E", borderwidth = 0, highlightthickness = 0,readonlybackground="black")
RootPasswd.place(x=240,y=50 , width=230,height=30)
SSHIP = Entry(root,font=("Helvetica", 16, "bold"),foreground="yellow", background="#1E1E1E", borderwidth = 0, highlightthickness = 0,readonlybackground="black")
SSHIP.place(x=240,y=90 , width=230,height=30)
SSHUser = Entry(root,font=("Helvetica", 16, "bold"),foreground="yellow", background="#1E1E1E", borderwidth = 0, highlightthickness = 0,readonlybackground="black")
SSHUser.place(x=240,y=130 , width=230,height=30)
SSHPassword = Entry(root,font=("Helvetica", 16, "bold"),foreground="yellow", background="#1E1E1E", borderwidth = 0, highlightthickness = 0,readonlybackground="black")
SSHPassword.place(x=240,y=170 , width=230,height=30)

def Refresh():
    rootPasswords = str(os.popen("grep rootPassword SystemInformation.txt |awk '{print $2}'").readlines())[2:-4]
    SSHIps = str(os.popen("grep SSHIp SystemInformation.txt |awk '{print $2}'").readlines())[2:-4]
    SSHUsers = str(os.popen("grep SSHUser SystemInformation.txt |awk '{print $2}'").readlines())[2:-4]
    SSHPasswords = str(os.popen("grep SSHPassword SystemInformation.txt |awk '{print $2}'").readlines())[2:-4]
    
    RootPasswd.delete(0, END)
    SSHIP.delete(0, END)
    SSHUser.delete(0, END)
    SSHPassword.delete(0, END)

    RootPasswd.insert(0,rootPasswords)
    SSHIP.insert(0,SSHIps)
    SSHUser.insert(0,SSHUsers)
    SSHPassword.insert(0,SSHPasswords)


bt1 = Button(root, text = "Refresh",command=Refresh,
                 background = "black",foreground="#ffd381",
                 font = ("Helvetica", 16, "bold"),relief="raised",compound="left")
bt1.config(highlightbackground='black')
bt1.place(x=240,y=210)

def Update():
    os.system('>SystemInformation.txt')
    os.system('echo "rootPassword '+ str(RootPasswd.get()) +'" >> SystemInformation.txt')
    os.system('echo "SSHIp '+        str(SSHIP.get())      +'" >> SystemInformation.txt')
    os.system('echo "SSHUser '+      str(SSHUser.get())    +'" >> SystemInformation.txt')
    os.system('echo "SSHPassword '+  str(SSHPassword.get())+'" >> SystemInformation.txt')

    Refresh()

bt2 = Button(root, text = "Update",command=Update,
                 background = "black",foreground="#ffd381",
                 font = ("Helvetica", 16, "bold"),relief="raised",compound="left")
bt2.config(highlightbackground='black')
bt2.place(x=360,y=210)

Refresh()
root.mainloop()
'''
rootPassword q
SSHIp 172.18.33.54
SSHUser alex_wong
SSHPassword Alex180472392
'''
