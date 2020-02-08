from tkinter import *
from tkinter import ttk
from gif import ImageLabel 
import time
import threading
from PIL import ImageTk,Image
from tkinter import messagebox
root=Tk()
root.geometry('1350x700')
root.configure(bg="#0086af")
root.title('PIZZA ONLINE DELIVERY FORM')
def firstpage():
    label9=Label(root,text='',bg='white',width=200,height=100)
    label9.place(x=0,y=0)
    label=Label(root,text='SUB_MENU',bg='white',fg='#0086af',font=("Courier New",25),padx=20)
    label.place(x=570,y=0)
    p=PhotoImage(file=r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\LogoMakerCa-1577683894895.png')
    p=p.subsample(10,10)
    label23=Label(root,image=p,bg='white')
    label23.image=p
    label23.place(x=-5,y=-50)

    ph=PhotoImage(file=r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\LogoMakerCa-1577687020425.png')
    ph=ph.subsample(9,9)
    label23=Label(root,image=ph,bg='white')
    label23.image=ph
    label23.place(x=1130,y=-10)
    label24=Label(root,text='8433624344',font=("Courier New",15),bg='white',fg='#0086af')
    label24.place(x=1220,y=27)

    lable37=Label(root,text='',bg='#0086af',width=200,height=32)
    lable37.place(x=0,y=80)
    label38=Label(root,text='VEG PIZZA',font=("Courier New",15),fg='#0086af',bg='white',padx=30)
    label38.place(x=590,y=40)

    photo1=ImageTk.PhotoImage(Image.open(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\Margherit.gif'))
    label25=Label(root,image=photo1,bg='white')
    label25.image=photo1    
    label25.place(x=10,y=110)
    label26=Label(root,text='Margherita',font=("Courier New",20),bg='#0086af',fg='white',padx=40)
    label26.place(x=10,y=390)
    text='A hugely popular margherita, with a\n deliciously tangy single cheese topping'
    label27=Label(root,text=text,bg='#0086af',justify=CENTER,padx=20,fg='white')
    label27.place(x=10,y=430)
    fbtn1=Button(root,text='ORDER NOW',font=("Courier New",15),bg='white',fg='#0086af',command=lambda:final('Margherita'))
    fbtn1.place(x=90,y=510)

    photo2=ImageTk.PhotoImage(Image.open(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\Peppy_Paneer.gif'))
    label28=Label(root,image=photo2,bg='white')
    label28.image=photo2
    label28.place(x=360,y=110)
    label29=Label(root,text='Peppy Paneer',font=("Courier New",20),bg='#0086af',fg='white',padx=40)
    label29.place(x=360,y=390)
    text='Chunky paneer with crisp capsicum and \nspicy red pepper - quite a mouthful!'
    label30=Label(root,text=text,bg='#0086af',justify=CENTER,fg='white',padx=35)
    label30.place(x=360,y=430)
    fbtn2=Button(root,text='ORDER NOW',font=("Courier New",15),bg='white',fg='#0086af',command=lambda:final('Peppy Paneer'))
    fbtn2.place(x=440,y=510)

    photo3=ImageTk.PhotoImage(Image.open(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\Farmhouse.gif'))
    label31=Label(root,image=photo3,bg='white')
    label31.image=photo3
    label31.place(x=720,y=110)
    label32=Label(root,text='Farm House',font=("Courier New",20),bg='#0086af',fg='white',padx=40)
    label32.place(x=720,y=390)
    text='A pizza that goes ballistic on \nveggies! Check out this mouth \nwatering overload of crunchy, crisp capsicum, \nsucculent mushrooms and fresh tomatoes'
    label33=Label(root,text=text,bg='#0086af',justify=CENTER,fg='white',padx=20)
    label33.place(x=720,y=430)
    fbtn3=Button(root,text='ORDER NOW',font=("Courier New",15),bg='white',fg='#0086af',command=lambda:final('Farm House'))
    fbtn3.place(x=800,y=510)

    photo4=ImageTk.PhotoImage(Image.open(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\Deluxe_Veggie.gif'))
    label34=Label(root,image=photo4,bg='white')
    label34.image=photo4
    label34.place(x=1070,y=110)
    label35=Label(root,text='Deluxe Veggie',font=("Courier New",20),bg='#0086af',fg='white',padx=40)
    label35.place(x=1070,y=390)
    text='For a vegetarian looking for a BIG treat that\ngoes easy on the spices, this one\'s \ngot it all.. The onions, the capsicum, \nthose delectable mushrooms \n- with paneer and golden corn to top it all.'
    label36=Label(root,text=text,bg='#0086af',justify=CENTER,fg='white',padx=20)
    label36.place(x=1070,y=430)
    fbtn4=Button(root,text='ORDER NOW',font=("Courier New",15),bg='white',fg='#0086af',command=lambda:final('Deluxe Veggie'))
    fbtn4.place(x=1150,y=510)

    btn10=Button(root,text='<-Back',fg='white',bg='#0086af',padx=30,command=startpage)
    btn10.place(x=625,y=570)

def scondpage():
    label9=Label(root,text='',bg='white',width=200,height=100)
    label9.place(x=0,y=0)
    label=Label(root,text='SUB_MENU',bg='white',fg='#0086af',font=("Courier New",25),padx=20)
    label.place(x=570,y=0)
    p=PhotoImage(file=r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\LogoMakerCa-1577683894895.png')
    p=p.subsample(10,10)
    label23=Label(root,image=p,bg='white')
    label23.image=p
    label23.place(x=-5,y=-50)

    ph=PhotoImage(file=r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\LogoMakerCa-1577687020425.png')
    ph=ph.subsample(9,9)
    label23=Label(root,image=ph,bg='white')
    label23.image=ph
    label23.place(x=1130,y=-10)
    label24=Label(root,text='8433624344',font=("Courier New",15),bg='white',fg='#0086af')
    label24.place(x=1220,y=27)

    lable37=Label(root,text='',bg='#0086af',width=200,height=32)
    lable37.place(x=0,y=80)
    label38=Label(root,text='NON-VEG PIZZA',font=("Courier New",15),fg='#0086af',bg='white')
    label38.place(x=590,y=40)

    photo1=ImageTk.PhotoImage(Image.open(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\Pepper_Barbeque.gif'))
    label25=Label(root,image=photo1,bg='white')
    label25.image=photo1    
    label25.place(x=10,y=110)
    label26=Label(root,text='BARBECUE CHICKEN',font=("Courier New",20),bg='#0086af',fg='white',padx=10)
    label26.place(x=10,y=390)
    text='Pepper Barbecue Chicken I Cheese'
    label27=Label(root,text=text,bg='#0086af',justify=CENTER,padx=30,fg='white')
    label27.place(x=10,y=430)
    sbtn1=Button(root,text='ORDER NOW',font=("Courier New",15),bg='white',fg='#0086af',command=lambda:final('BARBECUE CHICKEN'))
    sbtn1.place(x=90,y=510)

    photo2=ImageTk.PhotoImage(Image.open(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\Chicken_Sausage.gif'))
    label28=Label(root,image=photo2,bg='white')
    label28.image=photo2
    label28.place(x=360,y=110)
    label29=Label(root,text='CHICKEN SAUSAGE',font=("Courier New",20),bg='#0086af',fg='white',padx=10)
    label29.place(x=360,y=390)
    text='Chicken Sausage I Cheese'
    label30=Label(root,text=text,bg='#0086af',justify=CENTER,fg='white',padx=60)
    label30.place(x=360,y=430)
    sbtn2=Button(root,text='ORDER NOW',font=("Courier New",15),bg='white',fg='#0086af',command=lambda:final('CHICKEN SAUSAGE'))
    sbtn2.place(x=440,y=510)

    photo3=ImageTk.PhotoImage(Image.open(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\Chicken_Golden_Delight.gif'))
    label31=Label(root,image=photo3,bg='white')
    label31.image=photo3
    label31.place(x=720,y=110)
    label32=Label(root,text='GOLDEN DELIGHT',font=("Courier New",20),bg='#0086af',fg='white',padx=20)
    label32.place(x=720,y=390)
    text='Mmm! Barbeque chicken with a \ntopping of golden corn loaded with extra \ncheese. Worth its weight in gold!'
    label33=Label(root,text=text,bg='#0086af',justify=CENTER,fg='white',padx=30)
    label33.place(x=720,y=430)
    sbtn3=Button(root,text='ORDER NOW',font=("Courier New",15),bg='white',fg='#0086af',command=lambda:final('GOLDEN DELIGHT'))
    sbtn3.place(x=800,y=510)

    photo4=ImageTk.PhotoImage(Image.open(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\Non-Veg_Supreme.gif'))
    label34=Label(root,image=photo4,bg='white')
    label34.image=photo4
    label34.place(x=1070,y=110)
    label35=Label(root,text='Non-Veg Supreme',font=("Courier New",20),bg='#0086af',fg='white',padx=20)
    label35.place(x=1070,y=390)
    text='Bite into supreme delight of \nBlack Olives, Onions, Grilled Mushrooms,\nPepper BBQ Chicken, Peri-Peri \nChicken, Grilled Chicken Rashers'
    label36=Label(root,text=text,bg='#0086af',justify=CENTER,fg='white',padx=30)
    label36.place(x=1070,y=430)
    sbtn4=Button(root,text='ORDER NOW',font=("Courier New",15),bg='white',fg='#0086af',command=lambda:final('Non-Veg Supreme'))
    sbtn4.place(x=1150,y=510)

    btn10=Button(root,text='<-Back',fg='white',bg='#0086af',padx=30,command=startpage)
    btn10.place(x=625,y=570)


def thirdpage():
    label9=Label(root,text='',bg='white',width=200,height=100)
    label9.place(x=0,y=0)
    label=Label(root,text='SUB_MENU',bg='white',fg='#0086af',font=("Courier New",25),padx=20)
    label.place(x=570,y=0)
    p=PhotoImage(file=r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\LogoMakerCa-1577683894895.png')
    p=p.subsample(10,10)
    label23=Label(root,image=p,bg='white')
    label23.image=p
    label23.place(x=-5,y=-50)

    ph=PhotoImage(file=r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\LogoMakerCa-1577687020425.png')
    ph=ph.subsample(9,9)
    label23=Label(root,image=ph,bg='white')
    label23.image=ph
    label23.place(x=1130,y=-10)
    label24=Label(root,text='8433624344',font=("Courier New",15),bg='white',fg='#0086af')
    label24.place(x=1220,y=27)

    lable37=Label(root,text='',bg='#0086af',width=200,height=32)
    lable37.place(x=0,y=80)
    label38=Label(root,text='PIZZA MANIA',font=("Courier New",15),fg='#0086af',bg='white')
    label38.place(x=600,y=40)

    photo1=ImageTk.PhotoImage(Image.open(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\CapsicumVeg.gif'))
    label25=Label(root,image=photo1,bg='white')
    label25.image=photo1    
    label25.place(x=10,y=110)
    label26=Label(root,text='CAPSICUM',font=("Courier New",20),bg='#0086af',fg='white',padx=60)
    label26.place(x=10,y=390)
    text='Capsicum'
    label27=Label(root,text=text,bg='#0086af',justify=CENTER,padx=90,fg='white')
    label27.place(x=10,y=430)
    tbtn1=Button(root,text='ORDER NOW',font=("Courier New",15),bg='white',fg='#0086af',command=lambda:final('CAPSICUM'))
    tbtn1.place(x=90,y=510)

    photo2=ImageTk.PhotoImage(Image.open(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\onion_veg.gif'))
    label28=Label(root,image=photo2,bg='white')
    label28.image=photo2
    label28.place(x=360,y=110)
    label29=Label(root,text='ONION',font=("Courier New",20),bg='#0086af',fg='white',padx= 90)
    label29.place(x=360,y=390)
    text='Onion'
    label30=Label(root,text=text,bg='#0086af',justify=CENTER,fg='white',padx=110)
    label30.place(x=360,y=430)
    tbtn2=Button(root,text='ORDER NOW',font=("Courier New",15),bg='white',fg='#0086af',command=lambda:final('ONION'))
    tbtn2.place(x=440,y=510)

    photo3=ImageTk.PhotoImage(Image.open(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\golden_corn_veg.gif'))
    label31=Label(root,image=photo3,bg='white')
    label31.image=photo3
    label31.place(x=720,y=110)
    label32=Label(root,text='GOLDEN CORN',font=("Courier New",20),bg='#0086af',fg='white',padx=50)
    label32.place(x=720,y=390)
    text='Golden Corn'
    label33=Label(root,text=text,bg='#0086af',justify=CENTER,fg='white',padx=100)
    label33.place(x=720,y=430)
    tbtn3=Button(root,text='ORDER NOW',font=("Courier New",15),bg='white',fg='#0086af',command=lambda:final('GOLDEN CORN'))
    tbtn3.place(x=800,y=510)

    photo4=ImageTk.PhotoImage(Image.open(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\Paneer_Special.gif'))
    label34=Label(root,image=photo4,bg='white')
    label34.image=photo4
    label34.place(x=1070,y=110)
    label35=Label(root,text='PANEER & ONION',font=("Courier New",20),bg='#0086af',fg='white',padx=20)
    label35.place(x=1070,y=390)
    text='Creamy Paneer I Onion'
    label36=Label(root,text=text,bg='#0086af',justify=CENTER,fg='white',padx=80)
    label36.place(x=1070,y=430)
    tbtn4=Button(root,text='ORDER NOW',font=("Courier New",15),bg='white',fg='#0086af',command=lambda:final('PANEER & ONION'))
    tbtn4.place(x=1150,y=510)

    btn10=Button(root,text='<-Back',fg='white',bg='#0086af',padx=30,command=startpage)
    btn10.place(x=625,y=570)

def fourthpage():
    label9=Label(root,text='',bg='white',width=200,height=100)
    label9.place(x=0,y=0)
    label=Label(root,text='SUB_MENU',bg='white',fg='#0086af',font=("Courier New",25),padx=20)
    label.place(x=570,y=0)
    p=PhotoImage(file=r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\LogoMakerCa-1577683894895.png')
    p=p.subsample(10,10)
    label23=Label(root,image=p,bg='white')
    label23.image=p
    label23.place(x=-5,y=-50)

    ph=PhotoImage(file=r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\LogoMakerCa-1577687020425.png')
    ph=ph.subsample(9,9)
    label23=Label(root,image=ph,bg='white')
    label23.image=ph
    label23.place(x=1130,y=-10)
    label24=Label(root,text='8433624344',font=("Courier New",15),bg='white',fg='#0086af')
    label24.place(x=1220,y=27)

    lable37=Label(root,text='',bg='#0086af',width=200,height=32)
    lable37.place(x=0,y=80)
    label38=Label(root,text='BURGER PIZZA',font=("Courier New",15),fg='#0086af',bg='white')
    label38.place(x=590,y=40)

    photo1=ImageTk.PhotoImage(Image.open(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\160790_Burger_Pizza_427X298_Pixel.gif'))
    label25=Label(root,image=photo1,bg='white')
    label25.image=photo1    
    label25.place(x=120,y=110)
    label26=Label(root,text='BURGER PIZZA - CLASSIC VEG',font=("Courier New",20),bg='#0086af',fg='white',padx=10)
    label26.place(x=120,y=420)
    text='Bite into delight! Witness the epic combination of pizza and burger\n with our classic Burger Pizza, that looks good and tastes great!'
    label27=Label(root,text=text,bg='#0086af',justify=CENTER,padx=30,fg='white')
    label27.place(x=120,y=450)
    fobtn1=Button(root,text='ORDER NOW',font=("Courier New",15),bg='white',fg='#0086af',command=lambda:final('BURGER PIZZA - CLASSIC VEG'))
    fobtn1.place(x=270,y=510)

    photo2=ImageTk.PhotoImage(Image.open(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\Burger_Pizza_Non.gif'))
    label28=Label(root,image=photo2,bg='white')
    label28.image=photo2
    label28.place(x=800,y=110)
    label29=Label(root,text='BURGER PIZZA- CLASSIC NON VEG',font=("Courier New",20),bg='#0086af',fg='white',padx=10)
    label29.place(x=770,y=420)
    ext='For all the meat cravers, try the classic non-veg Burger Pizza loaded \nwith the goodness of burger and the greatness of pizza.'
    label30=Label(root,text=text,bg='#0086af',justify=CENTER,fg='white',padx=60)
    label30.place(x=780,y=450)
    fobtn2=Button(root,text='ORDER NOW',font=("Courier New",15),bg='white',fg='#0086af',command=lambda:final('BURGER PIZZA- CLASSIC NON VEG'))
    fobtn2.place(x=970,y=510)
    btn10=Button(root,text='<-Back',fg='white',bg='#0086af',padx=30,command=startpage)
    btn10.place(x=625,y=570)

#form
def startpage():
    result_number=None
    
    def clear():
        entry1.delete(0,END)
        

    def search():
        global search_label,label_reult
        global result_number
        pizza_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        search_val=entry1.get()
        print("SEARCH-> ",search_val)
        search_val=str(search_val).strip().lower()
        if search_val=='margherita':
            result_number=1
        elif search_val=='peppy paneer':
            result_number=2
        elif search_val=='farm house':
            result_number=3
        elif search_val=='deluxe veggie':
            result_number=4
        elif search_val=='barbecue chicken':
            result_number=5
        elif search_val=='chicken sausage':
            result_number=6
        elif search_val=='golden delight':
            result_number=7
        elif search_val=='non-veg supreme': 
            result_number=8
        elif search_val=='capsicum':
            result_number=9
        elif search_val=='onion':
            result_number=10
        elif search_val=='golden corn':
            result_number=11
        elif search_val=='paneer and onion':
            result_number=12
        elif search_val=='classic non veg':
            result_number=13
        elif search_val=='classic veg':
            result_number=14
        else:
            result_number=None
        
        #binary searching
        # search_label=Label(root,text='',width=107,height=5,bg='#0086af')
        # search_label.place(x=300,y=610)
        pizza_list.sort()
        a=False
        low=0
        high=len(pizza_list)-1
        if result_number is not None:
            result_number=int(result_number)
            for i in range (len(pizza_list)):
                mid=int(low+(high-low)/2)
                if result_number>pizza_list[mid]:
                    low=mid+1
                elif result_number<pizza_list[mid]:
                    high=mid-1
                elif result_number==pizza_list[mid]:
                    messagebox.showinfo("FOUND", "ONE MATCH FOUND.\n(wait for 2 sec)")
                    a=True
                    break
        elif len(search_val)==0:
            messagebox.showerror("ERROR","ENTER A NAME FOR SEARCH")
        else:
            messagebox.showerror("NOT FOUND","NO MATCH FOUND.")
        if search_val=='margherita' or search_val=='peppy paneer' or search_val=='farm house' or search_val=='deluxe veggie':
            t2= threading.Timer(1.0,firstpage)
            t2.start()
        elif search_val=='barbecue chicken' or search_val=='chicken sausage' or search_val=='golden delight' or search_val=='non-veg supreme':
            t3= threading.Timer(1.0,scondpage)
            t3.start()
        elif search_val=='capsicum' or search_val=='onion' or search_val=='golden corn' or search_val=='paneer and onion':
            t4= threading.Timer(1.0,thirdpage)
            t4.start()
        elif search_val=='classic veg' or search_val=='classic non veg':
            t5=threading.Timer(1.0,fourthpage)
            t5.start()

    label9=Label(root,text='',bg='white',width=200,height=100)
    label9.place(x=0,y=0)
    label=Label(root,text='MENU',bg='white',fg='#0086af',font=("Courier New",25))
    label.place(x=630,y=0)
    p=PhotoImage(file=r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\LogoMakerCa-1577683894895.png')
    p=p.subsample(10,10)
    label23=Label(root,image=p , bg='white')
    label23.image=p
    label23.place(x=-5,y=-50)

    ph=PhotoImage(file=r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\LogoMakerCa-1577687020425.png')
    ph=ph.subsample(9,9)
    label23=Label(root,image=ph,bg='white')
    label23.image=ph
    label23.place(x=1130,y=-10)
    label24=Label(root,text='8433624344',font=("Courier New",15),bg='white',fg='#0086af')
    label24.place(x=1220,y=27)

    lable14=Label(root,text='',bg='#0086af',width=200,height=32)
    lable14.place(x=0,y=80)

    photo1=ImageTk.PhotoImage(Image.open(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\my-vegpizza.gif'))
    label10=Label(root,image=photo1,bg='white')
    label10.image=photo1    
    label10.place(x=10,y=160)
    label15=Label(root,text='VEG PIZZA',font=("Courier New",20),bg='#0086af',fg='white',padx=40)
    label15.place(x=10,y=110)
    text='A delight for veggie lovers! Choose from \nour wide range of delicious vegetarian \npizzas, it\'s softer and tastier'
    label19=Label(root,text=text,bg='#0086af',justify=CENTER,padx=20,fg='white')
    label19.place(x=10,y=430)
    btn2=Button(root,text='VIEW ALL',font=("Courier New",15),bg='white',fg='#0086af',command=firstpage)
    btn2.place(x=90,y=510)

    photo2=ImageTk.PhotoImage(Image.open(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\my-nonveg.gif'))
    label11=Label(root,image=photo2,bg='white')
    label11.image=photo2
    label11.place(x=360,y=160)
    label16=Label(root,text='NON-VEG PIZZA',font=("Courier New",20),bg='#0086af',fg='white',padx=40)
    label16.place(x=360,y=110)
    text='Choose your favourite non-veg \npizzas from the Domino\'s Pizza menu.\n Get fresh non-veg pizza with \nyour choice of crusts & toppings'
    label20=Label(root,text=text,bg='#0086af',justify=CENTER,fg='white',padx=35)
    label20.place(x=360,y=430)
    btn3=Button(root,text='VIEW ALL',font=("Courier New",15),bg='white',fg='#0086af',command=scondpage)
    btn3.place(x=440,y=510)

    photo3=ImageTk.PhotoImage(Image.open(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\my-pizzamania.gif'))
    label12=Label(root,image=photo3,bg='white')
    label12.image=photo3
    label12.place(x=720,y=160)
    label17=Label(root,text='PIZZA MANIA',font=("Courier New",20),bg='#0086af',fg='white',padx=40)
    label17.place(x=720,y=110)
    text='Indulge into mouth-watering \ntaste of Pizza mania range, perfect\n answer to all your food cravings'
    label21=Label(root,text=text,bg='#0086af',justify=CENTER,fg='white',padx=40)
    label21.place(x=720,y=430)
    btn4=Button(root,text='VIEW ALL',font=("Courier New",15),bg='white',fg='#0086af',command=thirdpage)
    btn4.place(x=800,y=510)

    photo4=ImageTk.PhotoImage(Image.open(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\my-burgerpizza.gif'))
    label13=Label(root,image=photo4,bg='white')
    label13.image=photo4
    label13.place(x=1070,y=160)
    label18=Label(root,text='BURGER PIZZA',font=("Courier New",20),bg='#0086af',fg='white',padx=40)
    label18.place(x=1070,y=110)
    text='Looks like a burger tastes like a\n pizza. Fresh veggies with the \ngoodness of wheat, baked to perfection'
    label22=Label(root,text=text,bg='#0086af',justify=CENTER,fg='white',padx=30)
    label22.place(x=1070,y=430)
    btn5=Button(root,text='VIEW ALL',font=("Courier New",15),bg='white',fg='#0086af',command=fourthpage)
    btn5.place(x=1150,y=510)

    entry1=Entry(root,font=("Courier New",20),width=25,bg='#0086af',relief=RAISED)
    entry1.place(x=475,y=570)
    
    photo5=PhotoImage(file=r"C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\img_47710.png")
    photo5=photo5.subsample(35,35)

    photo6=PhotoImage(file=r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\download (1).png')
    photo6=photo6.subsample(8,8)
    myimage1=Button(root,image=photo5,relief=RAISED,command=search)
    myimage1.image_names=photo5
    
    myimage1.place(x=845,y=570)
    myimage2=Button(root,image=photo6,relief=RAISED,command=clear)
    myimage2.image_names=photo6
    myimage2.place(x=890,y=570)

#final
def final(order):
    price=''
    def reset():
        combo1.delete(0,END)
        spin1.delete(0,END)
        entry3.delete(0,END)
        entry4.delete(0,END)
        text1.delete('1.0',END)
        entry5.delete(0,END)
        checkbutton_1.deselect()
        checkbutton_2.deselect()
        checkbutton_3.deselect()
        checkbutton_4.deselect()

    def submit():
        list='THANK YOU FOR SHOPPING WITH US.\nYOUR ORDER SUCCESSFULLY REGISTERD'
        messagebox.showinfo('ORDER_SUCCESSFULLY_REGISTERED',list)

         
    def update():
 
        global price
        price=''
        mail=''
        no=''
        pizzaname=''
        name=''
        qty=''
        x1=''
        x2=''
        x3=''
        x4=''
        topfinal=''
        sub=''
        topprice=''
        add=''
        pizzaname=combo1.get()
        label22=Label(root,text=pizzaname,width=15,justify=CENTER)
        label22.place(x=810,y=160)
        qty=spin1.get()
        label23=Label(root,text=qty,width=15,justify=CENTER)
        label23.place(x=990,y=160)
        
        name=entry3.get()
        label26=Label(root,text=name,width=15,justify=CENTER)
        label26.place(x=810,y=300)
        x1=var1.get()
        x2=var2.get()
        x3=var3.get()
        x4=var4.get()
        topfinal='Pepperoni,Onions,Mushrooms,Cheese'
        if x1==0 and x2==0 and x3==0 and x4==0:
            topfinal='NONE' 
            topprice=0
        elif x1==0 and x2==0 and x3==0 and x4==1:
            topfinal='Cheese'
            topprice=40
        elif x1==0 and x2==0 and x3==1 and x4==0:
            topfinal='Mushrooms'
            topprice=40
        elif x1==0 and x2==0 and x3==1 and x4==1:
            topfinal='Mushrooms,Cheese'
            topprice=80
        elif x1==0 and x2==1 and x3==0 and x4==0:
            topfinal='Onions'
            topprice=40
        elif x1==0 and x2==1 and x3==0 and x4==1:
            topfinal='Onions,Cheese'
            topprice=80
        elif x1==0 and x2==1 and x3==1 and x4==0:
            topfinal='Onions,Mushrooms'
            topprice=80
        elif x1==0 and x2==1 and x3==1 and x4==1:
            topfinal='Onions,Mushrooms,Cheese'
            topprice=120
        elif x1==1 and x2==0 and x3==0 and x4==0:
            topfinal='Pepperoni'
            topprice=40
        elif x1==1 and x2==0 and x3==0 and x4==1:
            topfinal='Pepperoni,Cheese'
            topprice=80
        elif x1==1 and x2==0 and x3==1 and x4==0:
            topfinal='Pepperoni,Mushrooms'
            topprice=80
        elif x1==1 and x2==0 and x3==1 and x4==1:
            topfinal='Pepperoni,Mushrooms,Cheese'
            topprice=120
        elif x1==1 and x2==1 and x3==0 and x4==0:
            topfinal='Pepperoni,Onions'
            topprice=80
        elif x1==1 and x2==1 and x3==0 and x4==1:
            topfinal='Pepperoni,Onions,Cheese'
            topprice=120
        elif x1==1 and x2==1 and x3==1 and x4==0:
            topfinal='Pepperoni,Onions,Mushrooms'
            topprice=120
        elif x1==1 and x2==1 and x3==1 and x4==1:
            topfinal='Pepperoni,Onions,Mushrooms,Cheese'
            topprice=160
        finalprice()
        label24=Label(root,text=price,width=15,justify=CENTER)
        label24.place(x=1170,y=160)
        
        label29=Label(root,text=topfinal,width=66)
        label29.place(x=810,y=230)

        price=int(price[:-2])
        sub=int(qty)*int(price)+int(topprice)  
        label25=Label(root,text=str(sub)+' RS',width=15,justify=CENTER)
        label25.place(x=1170,y=510)
        mail=entry5.get()
        label31=Label(root,text=mail,width=41)
        label31.place(x=990,y=300)
        no=entry4.get()
        label33=Label(root,text=no,width=66)
        label33.place(x=810,y=370)
        add=text1.get('1.0','end-1c')
        label35=Label(root,text=add,width=66,height=2)
        label35.place(x=810,y=440)


    def finalprice():
        global price
        response=combo1.get()
        if response=='Margherita':
            price='299 RS'
        elif response=='Peppy Paneer':
            price='349 RS'
        elif response=='Farm House':
            price='329 RS'
        elif response=='Deluxe Veggie':
            price='249 RS'
        elif response=='BARBECUE CHICKEN':
            price='500 RS'
        elif response=='CHICKEN SAUSAGE':
            price='399 RS'
        elif response=='GOLDEN DELIGHT':
            price='449 RS'
        elif response=='Non-Veg Supreme':
            price='550 RS'
        elif response=='CAPSICUM':
            price='200 RS'
        elif response=='ONION':
            price='199 RS'
        elif response=='GOLDEN CORN':
            price='250 RS'
        elif response=='PANEER & ONION':
            price='349 RS'
        elif response=='BURGER PIZZA - CLASSIC VEG':
            price='159 RS'
        elif response=='BURGER PIZZA- CLASSIC NON VEG':
            price='259 RS'
        

    label1=Label(root,text='',bg='white',width=200,height=100)
    label1.place(x=0,y=0)    
    label2=Label(root,text='YOUR ORDER',bg='white',fg='#0086af',font=("Courier New",25))
    label2.place(x=580,y=0)
    p=PhotoImage(file=r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\LogoMakerCa-1577683894895.png')
    p=p.subsample(10,10)
    label3=Label(root,image=p,bg='white')
    label3.image=p
    label3.place(x=-5,y=-50)

    ph=PhotoImage(file=r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\LogoMakerCa-1577687020425.png')
    ph=ph.subsample(9,9)
    label4=Label(root,image=ph,bg='white')
    label4.image=ph
    label4.place(x=1130,y=-10)
    label6=Label(root,text='8433624344',font=("Courier New",15),bg='white',fg='#0086af')
    label6.place(x=1220,y=27)

    lable7=Label(root,text='',bg='#0086af',width=200,height=32)
    lable7.place(x=0,y=80)    
    response=order
    value=['Margherita','Peppy Paneer','Farm House','Deluxe Veggie','BARBECUE CHICKEN','CHICKEN SAUSAGE','GOLDEN DELIGHT','Non-Veg Supreme','CAPSICUM','ONION','GOLDEN CORN','PANEER & ONION','BURGER PIZZA - CLASSIC VEG','BURGER PIZZA- CLASSIC NON VEG']
    label8=Label(root,text=' YOUR ORDER      -> ',font=("Courier New",15),fg='white',bg='#0086af')
    label8.place(x=0,y=100)
    combo1=ttk.Combobox(root,width=21,font=("Courier New",15),values=value)
    combo1.place(x=300,y=100)
    combo1.delete(0,END)
    combo1.insert(END,response)
    spin1=Spinbox(root,width=3,font=("Courier New",15),from_=0,to=100)
    spin1.place(x=620,y=100)
    label11=Label(root,text='X',font=("Courier New",15),fg='white',bg='#0086af')
    label11.place(x=590,y=100)
    label9=Label(root,text=' NAME            -> ',font=("Courier New",15),fg='white',bg='#0086af')
    label9.place(x=0,y=150)
    entry3=Entry(root,bg='white',width=22,font=("Courier New",15))
    entry3.place(x=300,y=150)
    label10=Label(root,text=' CONTACT NUMBER  -> ',font=("Courier New",15),fg='white',bg='#0086af')
    label10.place(x=0,y=200)
    entry4=Entry(root,bg='white',width=22,font=("Courier New",15))
    entry4.place(x=300,y=200)
    label12=Label(root,text=' ADDRESS         -> ',font=("Courier New",15),fg='white',bg='#0086af')
    label12.place(x=0,y=250)
    text1=Text(root,font=("Courier New",15),width=22,height=5)
    text1.place(x=300,y=250)
    label13=Label(root,text='DELIVERY DETAILS',font=("Courier New",15),bg='white',fg='#0086af')
    label13.place(x=150,y=50)
    label20=Label(root,text='SUMMARY',font=("Courier New",15),bg='white',fg='#0086af')
    label20.place(x=990,y=50)
    label21=Label(root,text='*(click  update  button)',fg='white',bg='#0086af')
    label21.place(x=970,y=80)
    label14=Label(root,text=' E-MAIL          ->',font=("Courier New",15),fg='white',bg='#0086af')
    label14.place(x=0,y=390)
    entry5=Entry(root,bg='white',width=22,font=("Courier New",15))
    entry5.place(x=300,y=390)
    label15=Label(root,text=' TOPPINGS        ->',font=("Courier New",15),fg='white',bg='#0086af')
    label15.place(x=0,y=440) 
    var1=IntVar()
    checkbutton_1=Checkbutton(root,text='Pepperoni',variable=var1,bg='#0086af',activebackground='#0086af',font=("Courier New",10))
    checkbutton_1.place(x=300,y=440)
    var2=IntVar()
    checkbutton_2=Checkbutton(root,text='Onions',variable=var2,bg='#0086af',activebackground='#0086af',font=("Courier New",10))
    checkbutton_2.place(x=410,y=440)
    var3=IntVar()
    checkbutton_3=Checkbutton(root,text='Mushrooms',variable=var3,bg='#0086af',activebackground='#0086af',font=("Courier New",10))
    checkbutton_3.place(x=520,y=440)
    var4=IntVar()
    checkbutton_4=Checkbutton(root,text='Cheese',variable=var4,bg='#0086af',activebackground='#0086af',font=("Courier New",10))
    checkbutton_4.place(x=630,y=440)
    label16=Label(root,text=' *(you can select multiple toppings,\n40 RS for each topping)',font=("Courier New",10,'italic'),fg='white',bg='#0086af')
    label16.place(x=0,y=460)

    finalbtn1=Button(root,text='Submit Order Now',font=("Courier New",10),padx=50,command=submit)
    finalbtn1.place(x=20,y=520)
    finalbtn2=Button(root,text='Reset',font=("Courier New",10),command=reset)
    finalbtn2.place(x=270,y=520)
    finalbtn3=Button(root,text='Close',font=("Courier New",10),command=root.destroy)
    finalbtn3.place(x=335,y=520)
    finalbtn4=Button(root,text='Update',font=("Courier New",10),command=update)
    finalbtn4.place(x=400,y=520)    
    homebutton=Button(root,text='Home',font=("Courier New",10),command=startpage)
    homebutton.place(x=475,y=520)
    label17=Label(root,text='',bg='white',width=70,height=29)
    label17.place(x=800,y=110)
    label18=Label(root,text='-ORDER-',width=15)
    label18.place(x=810,y=130)
    label19=Label(root,text='-QTY-',width=15)
    label19.place(x=990,y=130)
    label20=Label(root,text='-UNIT-PRICE-',width=15)
    label20.place(x=1170,y=130)
    label21=Label(root,text='-SUB-TOTAL-',width=15)
    label21.place(x=1170,y=480)

    label27=Label(root,text='-NAME-',width=15)
    label27.place(x=810,y=270)
    label28=Label(root,text='-TOPPINGS-',width=66)
    label28.place(x=810,y=200)
    label30=Label(root,text='-E-MAIL-',width=41)
    label30.place(x=990,y=270)    
    label32=Label(root,text='-CONTACT NUMBER-',width=66)
    label32.place(x=810,y=340)
    label34=Label(root,text='-ADDRESS-',width=66)
    label34.place(x=810,y=410)

def loading():
    # username=etr1.get()
    # password=etr2.get()
    # print("UID-> ",username)
    # print("PASSWORD-> ",password)
    label7=Label(root,text='',bg='white',width=200,height=100)

    ilabel=ImageLabel(root,bg='white')
    ilabel.place(x=430,y=50) 
    ilabel.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\giphy (1).gif')
    label7.place(x=0,y=0)
    label8=Label(root,text='LOADING.....',font=("Courier New",25),bg='white')
    label8.place(x=550,y=550)
    t1= threading.Timer(2.0,startpage)
    t1.start()

#LOGINFORM
photo=PhotoImage(file=r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\Datastructure_pro\newimage\LogoMakerCa-1577619130553.png')
photoimage=photo.subsample(5,5)

label1=Label(root,text='',image=photoimage,bg="#0086af")
label2=Label(root,text='',width=50,height=30,relief=GROOVE,bg="#fff8e3")
label3=Label(root,text='Login',fg="#002947",font=("Courier New",25),padx=30,bg="#fff8e3")
label4=Label(root,text='User ID:',fg="#002947",font=("Courier New",10),bg="#fff8e3")
etr1=Entry(root,bg='white',width=21,font=("Courier New",15),relief=SUNKEN)
label5=Label(root,text='Password:',fg="#002947",font=("Courier New",10),bg="#fff8e3")
etr2=Entry(root,bg='white',width=21,font=("Courier New",15),show='*',relief=SUNKEN)
btn1=Button(root,bg="#fff1c1",text='Login',font=("Courier New",15),activebackground="white",command=loading)
chk1=Checkbutton(root,text="keep me logged in",bg="#fff8e3",activebackground='#fff8e3')
label6=Label(root,text='Lost your Password?',bg="#fff8e3",font=("Courier New",10))


label1.place(x=0,y=20)
label2.place(x=800,y=75)
label3.place(x=900,y=100)
label4.place(x=850,y=200)
etr1.place(x=850,y=230)
label5.place(x=850,y=280)
etr2.place(x=850,y=310)
btn1.place(x=850,y=400)
chk1.place(x=850,y=350)
label6.place(x=900,y=480)
root.mainloop()