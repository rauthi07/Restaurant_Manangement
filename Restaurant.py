from tkinter import *
import time

root=Tk()
root.configure(background='#EEEEEE')
root.title('Restaurant Management System')

frame1=Frame(root, bg='#EEEEEE')
frame1.pack(side=TOP)
frame2=Frame(root, bg='#EEEEEE')
frame2.pack(side=BOTTOM)

CurrentTime=time.asctime(time.localtime(time.time()))

lbl1 = Label(frame1,font=('arial',30,'bold'), text='Restaurant Management System')
lbl1.pack()
lbl2 = Label(frame1,font=('arial',15,'bold'), text=CurrentTime)
lbl2.pack()

def Price():
    root = Tk()
    root.title("PRICE LIST")
    lbl1 = Label(root, font=('ariaL', 15, 'bold'), text='ITEM')
    lbl1.grid(row=0, column=0)
    lbl2 = Label(root, font=('ariaL', 15, 'bold'), text='PRICE')
    lbl2.grid(row=0, column=3)
    lbl3 = Label(root, font=('arial', 15, 'bold'), text='FRIES MEAL')
    lbl3.grid(row=1, column=0)
    lbl4 = Label(root, font=('arial', 15, 'bold'), text='30')
    lbl4.grid(row=1, column=3)
    lbl5 = Label(root, font=('arial', 15, 'bold'), text='LUNCH MEAL')
    lbl5.grid(row=2, column=0)
    lbl6 = Label(root, font=('arial', 15, 'bold'), text='40')
    lbl6.grid(row=2, column=3)
    lbl7 = Label(root, font=('arial', 15, 'bold'), text='CHICKEN MEAL')
    lbl7.grid(row=3, column=0)
    lbl8 = Label(root, font=('arial', 15, 'bold'), text='100')
    lbl8.grid(row=3, column=3)
    lbl9 = Label(root, font=('arial', 15, 'bold'), text='PIZZA MEAL')
    lbl9.grid(row=4, column=0)
    lbl10 = Label(root, font=('arial', 15, 'bold'), text='75')
    lbl10.grid(row=4, column=3)
    lbl11 = Label(root, font=('arial', 15, 'bold'), text='CHEESE BURGER')
    lbl11.grid(row=5, column=0)
    lbl12 = Label(root, font=('arial', 15, 'bold'), text='45')
    lbl12.grid(row=5, column=3)
    lbl13 = Label(root, font=('arial', 15, 'bold'), text='DRINKS')
    lbl13.grid(row=6, column=0)
    lbl14 = Label(root, font=('arial', 15, 'bold'), text='40')
    lbl14.grid(row=6, column=3)

    root.mainloop()

def Reset():
    order.set('')
    drinks.set('')
    fries.set('')
    cost.set('')
    lunch.set('')
    service_charge.set('')
    chicken.set('')
    tax.set('')
    pizza.set('')
    subtotal.set('')
    cheese_burger.set('')
    total.set('')

def Total():
    a=float(fries.get())
    b=float(drinks.get())
    c=float(lunch.get())
    d=float(chicken.get())
    e=float(pizza.get())
    f=float(cheese_burger.get())

    cost_of_fries=a*30
    cost_of_drinks =b*40
    cost_of_lunch =c*40
    cost_of_chicken =d*100
    cost_of_pizza =e*75
    cost_of_cheese_burger =f*45

    costofmeal = 'Rs.',('%.2f' % (cost_of_fries + cost_of_drinks + cost_of_lunch + cost_of_chicken + cost_of_pizza + cost_of_cheese_burger))
    Tax = ((cost_of_fries + cost_of_drinks + cost_of_lunch + cost_of_chicken + cost_of_pizza + cost_of_cheese_burger) * 0.25)
    Totalcost = (cost_of_fries + cost_of_drinks + cost_of_lunch + cost_of_chicken + cost_of_pizza + cost_of_cheese_burger)
    Service_Charge = ((cost_of_fries + cost_of_drinks + cost_of_lunch + cost_of_chicken + cost_of_pizza + cost_of_cheese_burger) / 80)
    service = 'Rs.',('%.2f' % Service_Charge)
    OverAllCost = 'Rs.',(Tax + Totalcost + Service_Charge)
    PayTax = 'Rs.',('%.2f' % Tax)

    service_charge.set(service)
    cost.set(costofmeal)
    tax.set(PayTax)
    subtotal.set(costofmeal)
    total.set(OverAllCost)

def Exit():
    root.destroy()

lbl3 = Label(frame2,font=('arial',15,'bold'),text='ORDER No')
lbl3.grid(row=0, column=0)
order=StringVar()
e1 = Entry(frame2,font=('arial',15,'bold'),textvariable=order)
e1.grid(row=0, column=1)

lbl4 = Label(frame2,font=('arial',15,'bold'),text='DRINKS')
lbl4.grid(row=0, column=2)
drinks=StringVar()
e2 = Entry(frame2,font=('arial',15,'bold'),textvariable=drinks)
e2.grid(row=0, column=3)

lbl5 = Label(frame2,font=('arial',15,'bold'),text='FRIES MEAL')
lbl5.grid(row=1, column=0)
fries=StringVar()
e3 = Entry(frame2,font=('arial',15,'bold'),textvariable=fries)
e3.grid(row=1, column=1)

lbl6= Label(frame2,font=('arial',15,'bold'),text='COST')
lbl6.grid(row=1, column=2)
cost=StringVar()
e4 = Entry(frame2,font=('arial',15,'bold'),textvariable=cost)
e4.grid(row=1, column=3)

lbl7 = Label(frame2,font=('arial',15,'bold'),text='LUNCH MEAL')
lbl7.grid(row=2, column=0)
lunch=StringVar()
e5 = Entry(frame2,font=('arial',15,'bold'),textvariable=lunch)
e5.grid(row=2, column=1)

lbl8 = Label(frame2,font=('arial',15,'bold'),text='SERVICE CHARGE')
lbl8.grid(row=2, column=2)
service_charge=StringVar()
e6 = Entry(frame2,font=('arial',15,'bold'),textvariable=service_charge)
e6.grid(row=2, column=3)

lbl9 = Label(frame2,font=('arial',15,'bold'),text='CHICKEN MEAL')
lbl9.grid(row=3, column=0)
chicken=StringVar()
e7 = Entry(frame2,font=('arial',15,'bold'),textvariable=chicken)
e7.grid(row=3, column=1)

lbl10 = Label(frame2,font=('arial',15,'bold'),text='GST')
lbl10.grid(row=3, column=2)
tax=StringVar()
e8 = Entry(frame2,font=('arial',15,'bold'),textvariable=tax)
e8.grid(row=3, column=3)

lbl11 = Label(frame2,font=('arial',15,'bold'),text='PIZZA MEAL')
lbl11.grid(row=4, column=0)
pizza=StringVar()
e9 = Entry(frame2,font=('arial',15,'bold'),textvariable=pizza)
e9.grid(row=4, column=1)

lbl12 = Label(frame2,font=('arial',15,'bold'),text='SUBTOTAL')
lbl12.grid(row=4, column=2)
subtotal=StringVar()
e10 = Entry(frame2,font=('arial',15,'bold'),textvariable=subtotal)
e10.grid(row=4, column=3)

lbl13 = Label(frame2,font=('arial',15,'bold'),text='CHEESE BURGUR')
lbl13.grid(row=5, column=0)
cheese_burger=StringVar()
e11 = Entry(frame2,font=('arial',15,'bold'),textvariable=cheese_burger)
e11.grid(row=5, column=1)

lbl14 = Label(frame2,font=('arial',15,'bold'),text='TOTAL')
lbl14.grid(row=5, column=2)
total=StringVar()
e12 = Entry(frame2,font=('arial',15,'bold'),textvariable=total)
e12.grid(row=5, column=3)

btn1=Button(frame2,font=('arial',15,'bold'),text='PRICE',command=Price)
btn1.grid(row=6,column=0)

btn2=Button(frame2,font=('arial',15,'bold'),text='TOTAL',command=Total)
btn2.grid(row=6,column=1)

btn3=Button(frame2,font=('arial',15,'bold'),text='RESET',command=Reset)
btn3.grid(row=6,column=2)

btn4=Button(frame2,font=('arial',15,'bold'),text='EXIT',command=Exit)
btn4.grid(row=6,column=3)

root.resizable(False, False)

root.mainloop()