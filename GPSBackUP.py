import os
print('x')
cmd = "grep rootPassword SystemInformation.txt |awk '{print $2}'"
SysPasswd = str(os.popen(cmd).readlines())[2:-4]

#22.304217 113.912238
def FindBackUpGPSBin(GPSX,GPSY):
    try:
        SearchFileName = str(GPSX)+'a'+str(GPSY).replace('.','d')
        record = os.popen('ls -1 GpsBinSave/ |grep ' + SearchFileName + '|tail -1').readlines()[0][:-1]
        return record
    except:
        pass

#print(FindBackUpGPSBin(22.304217,113.912238))

def HackRFOneReset():
    
    for res in os.popen("lsusb |grep Linux"):
        reset = res.split(' ')
        #os.system('cd usbResetTools/;echo '+SuPasswd+' |sudo -S ./usbreset /dev/bus/usb/' + str(reset[1]) +'/' + str(reset[3][:-1]) + '')
        SuPasswd = 'q'
        print('cd usbResetTools/;echo '+SuPasswd+' |sudo -S ./usbreset /dev/bus/usb/' + str(reset[1]) +'/' + str(reset[3][:-1]) + '')


HackRFOneReset()

