from tkinter import *
import backend_admin

def insert_text():
    backend_admin.insert(lic_text.get(),item_text.get(),weight_text.get(),price_text.get(),qua_text.get(),op_text.get(),mfr_text.get())
    list1.delete(0,END)
    list1.insert(END,lic_text.get(),item_text.get(),weight_text.get(),price_text.get(),qua_text.get(),op_text.get(),mfr_text.get())

def update_text():
    backend_admin.update(lic_text.get(),item_text.get(),weight_text.get(),price_text.get(),qua_text.get(),op_text.get(),mfr_text.get())

def view_text():
    list1.delete(0,END)
    for rows_view in backend_admin.view():
        list1.insert(END,rows_view)

def search_text():
    list1.delete(0,END)
    for rows_search in backend_admin.search(lic_text.get(),item_text.get()):
        list1.insert(END,rows_search)

def delete_text():
    backend_admin.delete(lic_text.get())

window=Tk()

l8=Label(window,text="SUPERMARKET  ITEMS",fg="black",bg="white",font="Times 24 bold underline")
l8.grid(row=0,column=2)

l1=Label(window,text="Lic No.",fg="black",bg="mistyrose",font="Times 16 bold")
l1.grid(row=2,column=0)

l2=Label(window,text="Item name",fg="black",bg="mistyrose",font="Times 14 bold")
l2.grid(row=4,column=0)

l3=Label(window,text="Price/Kg",fg="black",bg="mistyrose",font="Times 14 bold")
l3.grid(row=6,column=0)

l4=Label(window,text="Quantity",fg="black",bg="mistyrose",font="Times 14 bold")
l4.grid(row=2,column=2)

l5=Label(window,text="Offer price",fg="black",bg="mistyrose",font="Times 14 bold")
l5.grid(row=4,column=2)

l6=Label(window,text="Weight",fg="black",bg="mistyrose",font="Times 14 bold")
l6.grid(row=6,column=2)

l7=Label(window,text="Manufacturer",fg="black",bg="mistyrose",font="Times 14 bold")
l7.grid(row=8,column=1)

lic_text=StringVar()
item_text=StringVar()
weight_text=StringVar()
price_text=StringVar()
qua_text=StringVar()
op_text=StringVar()
mfr_text=StringVar()

el=Entry(window,textvariable=lic_text,bg="lavender",fg="blue4",font="Times 15 bold underline")
el.grid(row=2,column=1)

e2=Entry(window,textvariable=item_text,bg="lavender",fg="black",font="Times 12 bold")
e2.grid(row=4,column=1)

e3=Entry(window,textvariable=price_text,bg="lavender",fg="black",font="Times 12 bold")
e3.grid(row=6,column=1)

e4=Entry(window,textvariable=qua_text,bg="lavender",fg="black",font="Times 12 bold")
e4.grid(row=2,column=3)

e5=Entry(window,textvariable=op_text,bg="lavender",fg="black",font="Times 12 bold")
e5.grid(row=4,column=3)

e6=Entry(window,textvariable=weight_text,bg="lavender",fg="black",font="Times 12 bold")
e6.grid(row=6,column=3)

e7=Entry(window,textvariable=mfr_text,bg="lavender",fg="black",font="Times 12 bold")
e7.grid(row=8,column=2)

list1=Listbox(window,height=10,width=60)
list1.grid(row=11,column=1,rowspan=12,columnspan=3)

b1=Button(window,text="Insert",command=insert_text,bg="blue4",fg="white",font="Times 14 bold")
b1.grid(row=9,column=0)

b2=Button(window,text="Update",command=update_text,bg="blue4",fg="white",font="Times 14 bold")
b2.grid(row=9,column=1)

b3=Button(window,text="View",command=view_text,bg="navy",fg="white",font="Times 14 bold")
b3.grid(row=9,column=2)

b4=Button(window,text="Search",command=search_text,bg="blue4",fg="white",font="Times 14 bold")
b4.grid(row=9,column=3)

b5=Button(window,text="Delete",command=delete_text,bg="blue4",fg="white",font="Times 14 bold")
b5.grid(row=9,column=4)

sb1=Scrollbar(window)
sb1.grid(row=10,column=3,rowspan=15,columnspan=1)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

window.configure(background="mistyrose")
window.mainloop()