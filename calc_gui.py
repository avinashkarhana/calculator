from tkinter import *
from calc_cli import calculator as strcalc
root=Tk()
root.title("Expression Calculator")
heading=Frame(root)
heading.pack(fill=BOTH)
lblhead = Label(heading,text="Calculator", font=("Times-New-Roman", 28))
lblhead.pack()
content=Frame(root)
content.pack(fill=BOTH)
lblcontent = Label(heading,text="Type in your expression from Keybord or or provided virtual keys.", font=("Arial", 18))
lblcontent.pack()
expression = Entry(content,font=("Helvetica", 28))
expression.pack(fill=BOTH)
expression.focus()
btnframe=Frame(root)
btnframe.pack(fill=BOTH, expand=True, padx=50, pady=20)
def reset():
    expression.delete(0,'end')
def delete():
    str1=expression.get()
    l=len(str1)
    if l!=0:expression.delete(l-1,'end')
def insert(num):
    str1=expression.get()
    str2=str1+num
    expression.delete(0,'end')
    expression.insert(0,str2)
def equal():
    str1=expression.get()
    rs,prevc=strcalc(str1)
    expression.delete(0,'end')
    expression.insert(0,rs)
    prevcalc['text']=prevc
#creating Buttons START
plus=Button(btnframe,height = 2, width = 10,text="+",command=lambda:insert("+"))
minus=Button(btnframe,height = 2, width = 10,text="-",command=lambda:insert("-"))
divide=Button(btnframe,height = 2, width = 10,text="/",command=lambda:insert("/"))
multiply=Button(btnframe,height = 2, width = 10,text="x",command=lambda:insert("*"))
power=Button(btnframe,height = 2, width = 10,text="^",command=lambda:insert("^"))
lbracket=Button(btnframe,height = 2, width = 10,text="(",command=lambda:insert("("))
rbracket=Button(btnframe,height = 2, width = 10,text=")",command=lambda:insert(")"))
one=Button(btnframe,height = 2, width = 10,text="1",command=lambda:insert("1"))
two=Button(btnframe,height = 2, width = 10,text="2",command=lambda:insert("2"))
three=Button(btnframe,height = 2, width = 10,text="3",command=lambda:insert("3"))
four=Button(btnframe,height = 2, width = 10,text="4",command=lambda:insert("4"))
five=Button(btnframe,height = 2, width = 10,text="5",command=lambda:insert("5"))
six=Button(btnframe,height = 2, width = 10,text="6",command=lambda:insert("6"))
seven=Button(btnframe,height = 2, width = 10,text="7",command=lambda:insert("7"))
eight=Button(btnframe,height = 2, width = 10,text="8",command=lambda:insert("8"))
nine=Button(btnframe,height = 2, width = 10,text="9",command=lambda:insert("9"))
zero=Button(btnframe,height = 2, width = 10,text="0",command=lambda:insert("0"))
dot=Button(btnframe,height = 2, width = 10,text=".",command=lambda:insert("."))
reset=Button(btnframe,height = 2, width = 10,text="Reset",command=reset)
delete=Button(btnframe,height = 2, width = 10,text="Del",command=delete)
bequal=Button(root,text="=",height = 2, width = 48,command=equal)
#creating Buttons End

#packing buttons with Grid START
lbracket.grid(row=0,padx=5,pady=5,ipadx=5,ipady=5,sticky="EW",column=0)
rbracket.grid(row=0,padx=5,pady=5,ipadx=5,ipady=5,sticky="EW",column=1)
power.grid(row=0,padx=5,pady=5,ipadx=5,ipady=5,sticky="EW",column=2)
delete.grid(row=0,padx=5,pady=5,ipadx=5,ipady=5,sticky="EW",column=3)
one.grid(row=1,padx=5,pady=5,ipadx=5,ipady=5,sticky="EW",column=0)
two.grid(row=1,padx=5,pady=5,ipadx=5,ipady=5,sticky="EW",column=1)
three.grid(row=1,padx=5,pady=5,ipadx=5,ipady=5,sticky="EW",column=2)
four.grid(row=2,padx=5,pady=5,ipadx=5,ipady=5,sticky="EW",column=0)
five.grid(row=2,padx=5,pady=5,ipadx=5,ipady=5,sticky="EW",column=1)
six.grid(row=2,padx=5,pady=5,ipadx=5,ipady=5,sticky="EW",column=2)
seven.grid(row=3,padx=5,pady=5,ipadx=5,ipady=5,sticky="EW",column=0)
eight.grid(row=3,padx=5,pady=5,ipadx=5,ipady=5,sticky="EW",column=1)
nine.grid(row=3,padx=5,pady=5,ipadx=5,ipady=5,sticky="EW",column=2)
zero.grid(row=4,padx=5,pady=5,ipadx=5,ipady=5,sticky="EW",column=1)
reset.grid(row=4,padx=5,pady=5,ipadx=5,ipady=5,sticky="EW",column=0)
plus.grid(row=1,padx=5,pady=5,ipadx=5,ipady=5,sticky="EW",column=3)
minus.grid(row=2,padx=5,pady=5,ipadx=5,ipady=5,sticky="EW",column=3)
multiply.grid(row=3,padx=5,pady=5,ipadx=5,ipady=5,sticky="EW",column=3)
divide.grid(row=4,padx=5,pady=5,ipadx=5,ipady=5,sticky="EW",column=3)
dot.grid(row=4,padx=5,pady=5,ipadx=5,ipady=5,sticky="EW",column=2)
bequal.pack(side=BOTTOM,padx=5,pady=5)
prevcalc = Label(heading,text='', font=("Arial", 12))
prevcalc.pack(side=LEFT)
expression.bind('<Return>', lambda _: equal())
#packing buttons with Grid END

root.mainloop()
