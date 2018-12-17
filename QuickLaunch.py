from tkinter import *
from tkinter import ttk

global TOTALPRICE

root = Tk()

def CalculateTotal():
    global TOTALPRICE
    TOTALPRICE = 0

    Drink = str(drink.get()).replace('[','-').replace(']','').replace('$','')
    DrinkPrice = Drink.split('-')

    Entree = str(allentreeLB.get(ACTIVE)).replace('[','-').replace(']','').replace('$','')
    EntreePrice = Entree.split('-')

    TOTALPRICE += float(EntreePrice[1])
    TOTALPRICE += float(DrinkPrice[1])

    TotalPriceL.config(text='Total Price = $%s'%TOTALPRICE)

def Check():

    if drink.get() == '' or allentreeLB.get(ACTIVE) == '' or POC.get() == '' or IDText.get() == '':
        TotalPriceL.config(text = 'You have not filled it all out yet')
    else:
        CalculateTotal()

def Check2():

    if drink.get() == '' or allentreeLB.get(ACTIVE) == '' or POC.get() == '' or IDText.get() == '':
        TotalPriceL.config(text = 'You have not filled it all out yet')
    else:
        CheckOut()

def CheckOut():
    allinfo = 'ID-%s --- Payment-%s --- Day-%s --- drink-%s --- Entree-%s' %(IDText.get(),POC.get(),dayS.get(),drink.get(),allentreeLB.get(ACTIVE))

    OpenF = open('WhatOrder.txt','a')
    OpenF.write(allinfo + '\n')
    OpenF.close()
    clear()

def clear():
    POC.set('')
    IDText.delete(0, 'end')


def about():
    top = Toplevel()
    top.title("About")
    top.minsize(width=200, height=150)
    top.resizable(width = FALSE, height = FALSE)
    msg = Message(top, text='V1.0.0')
    msg2 = Message(top, text='Made by - Keenan H\n12/17/18')
    msg.pack()
    msg2.pack()
    button = Button(top, text="Close", command=top.destroy)
    button.pack()

def howtouse():
   top = Toplevel()
   top.title("How To Use")
   top.minsize(width=200, height=100)
   top.resizable(width=FALSE, height=FALSE)
   msg = Message(top, text='\nHow To Use\n')
   msg2 = Message(top, text='''You have to select what you want to drink, what entree you want to have, what day it is, your method of payment, andyour employess ID.
You can then go and calculate the total price of your meal and check out.''')
   msg.pack()
   msg2.pack()


def QUIT():
    quit()


#ProgressBar
PB = ttk.Progressbar(length = 500,orient ="horizontal",mode='determinate')
PB.grid(row = 0, column = 1, columnspan = 3)


#Drink
drink = StringVar()

DrinkL = Label(root,text = 'Drinks')
DrinkL.grid(row = 1, column = 1, sticky = NSEW)

AllDrinksL = Frame(root,borderwidth=2,relief="groove")
AllDrinksL.grid(row = 2, column = 1, sticky = NSEW)

SodaR = Radiobutton(AllDrinksL,text='Soda[$1]', value="Soda[$1]", variable=drink)
SodaR.grid(row=1, column=0, sticky=NSEW)

TeaR = Radiobutton(AllDrinksL,text='Tea[$1]', value="Tea[$1]", variable=drink)
TeaR.grid(row=2, column=0, sticky=NSEW)

MilkR = Radiobutton(AllDrinksL,text='Milk[$.75]', value="Milk[$.75]", variable=drink)
MilkR.grid(row=3, column=0, sticky=NSEW)

JuiceR = Radiobutton(AllDrinksL,text='Juice[$1.25]', value="Juice[$1.25]", variable=drink)
JuiceR.grid(row=4, column=0, sticky=NSEW)

#Entree
entree = StringVar()

entreeL = Label(root,text = 'Entree')
entreeL.grid(row = 1, column = 2, sticky = NSEW, columnspan = 2)

allentreeLB = Listbox(height = 6, width = 50)
allentreeLB.insert(END,'Sandwich[$3]','Pizza[$4]','Chicken Nugget[$3.75]','Chicken[$4]','Tofu[$15]','Gluten/Soy/Shellfish Free Clam Chowder[$20]','')
allentreeLB.grid(row = 2,column = 2, sticky = NSEW, columnspan = 2)


#def OWO():
#    print(allentreeLB.get(ACTIVE))
#b=Button(text='sadfsadasd',command=OWO)
#b.grid(row=99,column=99)


#Days
dayL = Label(text = 'Day')
dayL.grid(row = 5, column = 1)

dayS = Spinbox(values = ["Monday","Tuesday","Wednesday","Thursday","Friday"],wrap = TRUE)
dayS.grid(row = 6, column = 1)

#PaymentOptions
POL = Label(text = 'Payment Options')
POL.grid(row = 3, column = 1)

POC = ttk.Combobox(values = ['Credit','Check','Cash'])
POC.grid(row = 4,column = 1)

#ID
IDl = Label(text = 'Emploee ID')
IDl.grid(row = 4, column = 2)

IDText = Entry()
IDText.grid(row = 4, column = 3)

#Buttons
CalculateB = Button(text = "CALCULATE", command = Check)
CalculateB.grid(row = 6, column = 2)

CheckOutB = Button(text = 'CHECKOUT', command = Check2)
CheckOutB.grid(row = 6, column = 3)

#TotalPrice
TotalPriceL = Label()
TotalPriceL.grid(row = 7, column = 1, columnspan = 3)

#Menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = 'Exit',command = QUIT)
menubar.add_cascade(label = 'File', menu = filemenu)
helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = 'About', command = about)  #state = DISABLED
helpmenu.add_command(label = 'How To Use', command = howtouse)
menubar.add_cascade(label = 'Help', menu = helpmenu)
root.config(menu=menubar)


#Others
ttk.Sizegrip(root).grid(column=999, row=999, sticky=(N,S,E,W))
root.minsize(height = 300, width = 550)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)

AllDrinksL.grid_columnconfigure(0, weight=1)
AllDrinksL.grid_columnconfigure(1, weight=1)
AllDrinksL.grid_columnconfigure(2, weight=1)
AllDrinksL.grid_columnconfigure(3, weight=1)
AllDrinksL.grid_columnconfigure(4, weight=1)

allentreeLB.grid_columnconfigure(0, weight=1)
allentreeLB.grid_columnconfigure(1, weight=1)
allentreeLB.grid_columnconfigure(2, weight=1)
allentreeLB.grid_columnconfigure(3, weight=1)
allentreeLB.grid_columnconfigure(4, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_rowconfigure(7, weight=1)

AllDrinksL.grid_rowconfigure(0, weight=1)
AllDrinksL.grid_rowconfigure(1, weight=1)
AllDrinksL.grid_rowconfigure(2, weight=1)
AllDrinksL.grid_rowconfigure(3, weight=1)
AllDrinksL.grid_rowconfigure(4, weight=1)

allentreeLB.grid_rowconfigure(0, weight=1)
allentreeLB.grid_rowconfigure(1, weight=1)
allentreeLB.grid_rowconfigure(2, weight=1)
allentreeLB.grid_rowconfigure(3, weight=1)
allentreeLB.grid_rowconfigure(4, weight=1)


root.title('Drink')
root.mainloop()