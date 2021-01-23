import os
comment = False
comment2 = False
for x in os.popen('cat FYP_GUI_NoRoot.py').readlines():
    out = str(x)[:-1]
    if len(out)==0:#remove empty line
        continue
    if len(out.replace(' ',''))==0:#remove line only have space
        continue
    if str(out.replace(' ',''))[0]=='#':#remove comment line
        continue
    if str(out.replace(' ',''))=="'''":#remove long comment line
        if comment == False:
            comment = True
        else:
            comment = False
        continue
    if comment == True:
        continue

    if str(out.replace(' ',''))=='"""':#remove long comment line
        if comment2 == False:
            comment2 = True
        else:
            comment2 = False
        continue
    if comment2 == True:
        continue    

    if out.find('#')>0:
        print(str(x)[:out.find('#')])
    else:
        print(str(x)[:-1])


#Count the line:python3 test.py|wc -l
#Count the character:python3 test.py|wc -m


