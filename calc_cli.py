inp=""
def calculator(inp):   
    x=""
    test=[]
    testo=[]
    error=0
    lstap=""
    sym=['+', '-', '/', '*','^']
    num=['1','2','3','4','5','6','7','8','9','0']
    decimal=['.']
    #input formating in list START
    for letter in inp :
        if letter == "(" or letter == ")":
            if lstap==")": testo.append('*')
            if x!="" and x!=".": testo.append(float(x))
            if letter=="(" and x!="": testo.append('*')
            testo.append(letter)
            x=""
        elif letter in sym:
            if x!="" and lstap==")": testo.append('*')
            if x!=""  and x!=".": testo.append(float(x))
            testo.append(letter)
            lstap=letter
            x=""
        #non-numeric character immunity START
        elif letter in num or letter in decimal:
            if letter ==".":
                if "." not in x:
                    x=x+letter
            else:
                x=x+letter
        else:blank="blank"
        #non-numeric character imunity END
        lstlap=letter
    if x!="" and lstap==")": testo.append('*')
    if x!=""  and x!=".":testo.append(float(x))
    v=0
    if len(testo)>0:
        for v in range(0,2):

                if set([testo[0]]).issubset(sym):
                    testo.insert(0,0)
                if set([testo[len(testo)-1]]).issubset(sym):
                    testo.insert(len(testo)+1,0)
        #input formating END

        #expression validation START
        current=""
        lst=""
        for letter in testo:
            current=letter
            if  set([current, lst]).issubset(sym):
                error=1
                return("Invalid expression ! i think you added two operators consicutively "+lst+" and "+current +" in your expression." )
                break
            lst=current
        # . after Rbracket validation START
        ll=""
        ic=0
        for letter in testo:
            if ll==")" and letter not in sym and letter !=")":
                testo.insert(ic,"*")
            ll=letter
            ic=ic+1
        # . after Rbracket validation END
        #expression validation End
        #solve function START
        print(testo)
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
                        if test[pos+1]>0:
                            x=test[pos-1]/test[pos+1]
                        else:
                            error=1
                            return("Can Not Divide by Zero !\nCheck your expression.",True)
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
            er=False
            rr=""
            for element in test:
                for elememt in test:
                    if(element=="^"):
                        power()
            for element in test:
                for elememt in test:
                    if(element=="/"):
                        rr,er=divide()
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
            if len(test)>0 and er==False :return(test[0])
            else:return(rr)
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
            return("Invalid expression! Please check you brackets.")
            error=1
        #bracket check STOP
        prevc=""
        for xx in testo:
                prevc=prevc+str(xx)
        if error==0:
            rslt=slv(testo)
        if error==0:
            return(str(rslt),prevc)
    else:
            return("No calculations to be made !")
if __name__ == "__main__":
    print("Calculator\n########### \n")
    inp=input("Calculation is done in form of expression numbers(Example : 2(4+6)^2/10*2-15*2+(5)(2)(5) in this expression ^2 means power 2 and its Answer would be -40.0 )\n Enter your expression : ")
    rs=calculator(inp)
    if rs!="None": print(rs)
    else:print("Invalid Expression !")
