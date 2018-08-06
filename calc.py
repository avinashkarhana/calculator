print("Calculator\n########### \n")
inp=input("Calculation is done in form of expression numbers(Example : 2(4+6)^2/10*2-15*2+(5)(2)(5) in this epression ^2 means power 2 and its Answer would be -40.0 )\n Enter your expression : ")
x=""
test=[]
testo=[]
error=0
lstap=""
#input formating in list START
for letter in inp :
    if letter == "(" or letter == ")":
        if lstap==")": testo.append('*')
        if x!="": testo.append(float(x))
        if letter=="(" and x!="": testo.append('*')
        testo.append(letter)
        lstap=letter
        x=""
    elif letter == "+" or letter == "-" or letter == "*" or letter == "/" or letter == "^":
        if x!="" and lstap==")": testo.append('*')
        if x!="": testo.append(float(x))
        testo.append(letter)
        lstap=letter
        x=""
    #non-numeric character immunity START
    elif letter=="0" or letter=="1" or letter=="2" or letter=="3" or letter=="4" or letter=="5" or letter=="6" or letter=="7" or letter=="8" or letter=="9" :
        x=x+letter
    else:blank="blank"
    #non-numeric character imunity END
if x!="" and lstap==")": testo.append('*')
if x!="":testo.append(float(x))
v=0
if len(testo)>0:
    for v in range(0,2):

            if set([testo[0]]).issubset(set(['+', '-', '/', '*'])):
                testo.insert(0,0)
            if set([testo[len(testo)-1]]).issubset(set(['+', '-', '/', '*'])):
                testo.insert(len(testo)+1,0)
    #input formating END

    #expression validation START
    current=""
    lst=""
    for letter in testo:
        current=letter
        if  set([current, lst]).issubset(set(['+', '-', '/', '*'])):
            error=1
            print("Invalid expression ! i think you added two operators consicutively "+lst+" and "+current +" in your expression." )
            break
        lst=current
    #expression validation End

    #solve function START
    def slv(test):
        #setting of value after single calculation in list with function START
        def setvalue(pos):
            if pos>0 and pos<=len(test) : del test[pos+1]
            if pos>0 and pos<=len(test) : del test[pos]
        #setting of value after single calculation in list with function END

        #calculation of ^ START
        def power():
            x=1
            for element in test:
                if(element=="^"):
                    pos=test.index(element)
                    for v in range(0,int(test[pos+1])):
                        x=x*test[pos-1]
                    setvalue(pos)
                    if pos>0 and pos<=len(test) : test[pos-1]=x
        #calculation of ^ END

        #calculation of / START
        def divide():
            x=0
            for element in test:
                if(element=="/"):
                    pos=test.index(element)
                    x=test[pos-1]/test[pos+1]
                    setvalue(pos)
                    if pos>0 and pos<=len(test) : test[pos-1]=x
        #calculation of / END

        #calculation of * START
        def mul():
            x=0
            for element in test:
                if(element=="*"):
                    pos=test.index(element)
                    x=test[pos-1]*test[pos+1]
                    setvalue(pos)
                    if pos>0 and pos<=len(test) : test[pos-1]=x
        #calculation of * END

        #calculation of + START
        def add():
            x=0
            for element in test:
                if(element=="+"):
                    pos=test.index(element)
                    x=test[pos-1]+test[pos+1]
                    setvalue(pos)
                    if pos>0 and pos<=len(test) : test[pos-1]=x
        #calculation of + END

        #calculation of - START
        def sub():
            x=0
            for element in test:
                if(element=="-"):
                    pos=test.index(element)
                    x=test[pos-1]-test[pos+1]
                    setvalue(pos)
                    if pos>0 and pos<=len(test) : test[pos-1]=x
        #calculation of - END

        for element in test:
            for elememt in test:
                if(element=="^"):
                    power()
        for element in test:
            for elememt in test:
                if(element=="/"):
                    divide()
        for element in test:
            for elememt in test:
                if(element=="*"):
                    mul()
        for element in test:
            for elememt in test:
                if(element=="+"):
                    add()
        for element in test:
            for elememt in test:
                if(element=="-"):
                    sub()
        return(test[0])
    #solve function END

    #intitial left and right bracket counter START
    ilbcount=0
    irbcount=0
    for element in testo:
        if element=="(": 
            ilbcount=ilbcount+1
        if element==")": 
            irbcount=irbcount+1
    #intitial left and right bracket counter END

    #bracket check START
    if ilbcount==irbcount:
        #loop repeat START
        for j in range(0,ilbcount):
            #bracket position collector START
            z=0
            for element in testo:
                if element=="(": 
                    lbpos=z
                if element==")":
                    rbpos=z
                    break
                z=z+1
            #bracket position collector END
            #new list temp list creater START
            temp=[]
            for i in  range(lbpos+1,rbpos):
                temp.append(testo[i])
            #new list temp list creater END
            #solve temp list START
            b=slv(temp)
            #solve temp list END
            #remove from temp list from testo list START
            for k in range(lbpos+1,rbpos+1) :
                del testo[lbpos+1]
            #remove from temp list from testo list END
            #replace temp result in tempo list on place of left bracket which is solved START
            testo[lbpos]=b
            #replace temp result in tempo list on place of left bracket which is solved END
         #loop repeat END           

    else:
        print("Invalid expression! Please check you brackets.")
        error=1
    #bracket check STOP
    if error==0:
        rslt=slv(testo)
        print("  Your result is : "+str(rslt))
else:
        print("No calculations to be made !")
