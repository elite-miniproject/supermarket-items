from tkinter import *
import backenduser
def insertt_text():
    backenduser.insertt(item_text.get(),weight_text.get(),price_text.get(),qua_text.get())
    list1.delete(0,END)
    list1.insert(END,item_text.get(),weight_text.get(),price_text.get(),qua_text.get())

def vieww_text():
    list1.delete(0,END)
    for rows_view in backenduser.vieww():
        list1.insert(END,rows_view)

def searchh_text():
    list1.delete(0,END)
    for rows_search in backenduser.searchh(item_text.get()):
        list1.insert(END,rows_search)

window=Tk()
window.configure(background="misty rose")

l1=Label(window,text="SUPERMARKET  ITEMS",fg="black",bg="white",font="Times 24 bold underline")
l1.grid(row=0,column=2)

l2=Label(window,text="Item name",fg="black",bg="misty rose",font="Times 14 bold")
l2.grid(row=2,column=0)

l3=Label(window,text="Price/Kg",fg="black",bg="misty rose",font="Times 14 bold")
l3.grid(row=4,column=0)

l4=Label(window,text="Quantity",fg="black",bg="misty rose",font="Times 14 bold")
l4.grid(row=2,column=2)

l5=Label(window,text="Weight",fg="black",bg="misty rose",font="Times 14 bold")
l5.grid(row=4,column=2)

item_text=StringVar()
price_text=StringVar()
qua_text=StringVar()
weight_text=StringVar()

e1=Entry(window,textvariable=item_text,bg="plum1",fg="blue2",font="Times 16 bold underline")
e1.grid(row=2,column=1)

e2=Entry(window,textvariable=price_text,bg="plum1",fg="black",font="Times 14 bold")
e2.grid(row=4,column=1)

e3=Entry(window,textvariable=qua_text,bg="plum1",fg="black",font="Times 14 bold")
e3.grid(row=2,column=3)

e4=Entry(window,textvariable=weight_text,bg="plum1",fg="black",font="Times 14 bold")
e4.grid(row=4,column=3)

b1=Button(window,text="Submit",command=insertt_text,bg="cyan2",fg="black",font="Times 18 bold")
b1.grid(row=5,column=0)

b2=Button(window,text="Search",command=searchh_text,bg="cyan2",fg="black",font="Times 18 bold")
b2.grid(row=5,column=2)

b3=Button(window,text="View",command=vieww_text,bg="cyan2",fg="gray1",font="Times 18 bold")
b3.grid(row=5,column=4)

list1=Listbox(window,height=8,width=65)
list1.grid(row=8,column=1,rowspan=9,columnspan=3)

sb1=Scrollbar(window)
sb1.grid(row=8,column=3,rowspan=10,columnspan=1)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

window.mainloop()

