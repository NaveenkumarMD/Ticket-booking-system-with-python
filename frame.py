from tkinter import *
from sqlite3 import *
import random
from tkinter import messagebox
                ##############bookmtickets window########
def rad():
    m=Tk()
    m.minsize(1520,800)
    m.configure(background="grey")
    seats={'a1':1,'a2':2,'a3':3}
    for (i,j) in seats.items():
        s=j/10
        r=Radiobutton(m,text="",bg="grey")
        r.place(relx=(0.2+s),rely=0.3)
def w1():
    m=Tk()
    m.minsize(1520,800)
    u1=150
    u2=250
    u3=400
    m.title("TIMINGS")
    m.configure(background="grey")
    l3=Label(m,text="SEAT TYPE",font=("Times New Roman",35),bg="grey",fg="red")
    l3.pack()
    b=Button(m,text="NORMAL [RS.150]",width=40,height=3,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,rad]])
    b.place(relx=0.5,rely=0.3,anchor="c")
    b=Button(m,text="SILVER [RS.250]",width=40,height=3,bg="DodgerBlue2",fg="white",font=(10))
    b.place(relx=0.5,rely=0.5,anchor="c")
    b=Button(m,text="EXECUTIVE [RS.400]",width=40,height=3,bg="DodgerBlue2",fg="white",font=(10))
    b.place(relx=0.5,rely=0.7,anchor="c")
    b5=Button(m,text="BACK",width=6,height=1,bg="firebrick1",fg="snow",font=(10),command=lambda: [f() for f in [m.destroy,q1]])
    b5.place(relx=0.9,rely=0.08,anchor="c")
    
def w2():
    m=Tk()
    m.minsize(1520,800)
    m.title("TIMINGS")
    v1=350
    v2=450
    v3=600
    m.configure(background="grey")
    l3=Label(m,text="SEAT TYPE",font=("Times New Roman",35),bg="grey",fg="red")
    l3.pack()
    b=Button(m,text="NORMAL [RS.350]",width=40,height=3,bg="DodgerBlue2",fg="white",font=(10))
    b.place(relx=0.5,rely=0.3,anchor="c")
    b=Button(m,text="SILVER [RS.450]",width=40,height=3,bg="DodgerBlue2",fg="white",font=(10))
    b.place(relx=0.5,rely=0.5,anchor="c")
    b=Button(m,text="EXECUTIVE [RS.600]",width=40,height=3,bg="DodgerBlue2",fg="white",font=(10))
    b.place(relx=0.5,rely=0.7,anchor="c")
    b5=Button(m,text="BACK",width=6,height=1,bg="firebrick1",fg="snow",font=(10),command=lambda: [f() for f in [m.destroy,q1]])
    b5.place(relx=0.9,rely=0.08,anchor="c")
def w3():
    m=Tk()
    m.minsize(1520,800)
    x1=200
    x2=300
    x3=450
    m.title("TIMINGS")
    m.configure(background="grey")
    l3=Label(m,text="SEAT TYPE",font=("Times New Roman",35),bg="grey",fg="red")
    l3.pack()
    b=Button(m,text="NORMAL [RS.200]",width=40,height=3,bg="DodgerBlue2",fg="white",font=(10))
    b.place(relx=0.5,rely=0.3,anchor="c")
    b=Button(m,text="SILVER [RS.300]",width=40,height=3,bg="DodgerBlue2",fg="white",font=(10))
    b.place(relx=0.5,rely=0.5,anchor="c")
    b=Button(m,text="EXECUTIVE [RS.450]",width=40,height=3,bg="DodgerBlue2",fg="white",font=(10))
    b.place(relx=0.5,rely=0.7,anchor="c")
    b5=Button(m,text="BACK",width=6,height=1,bg="firebrick1",fg="snow",font=(10),command=lambda: [f() for f in [m.destroy,q1]])
    b5.place(relx=0.9,rely=0.08,anchor="c")
def w4():
    m=Tk()
    m.minsize(1520,800)
    y1=200
    y2=300
    y3=450
    m.title("TIMINGS")
    m.configure(background="grey")
    l3=Label(m,text="SEAT TYPE",font=("Times New Roman",35),bg="grey",fg="red")
    l3.pack()
    b=Button(m,text="NORMAL [RS.200]",width=40,height=3,bg="DodgerBlue2",fg="white",font=(10))
    b.place(relx=0.5,rely=0.3,anchor="c")
    b=Button(m,text="SILVER [RS.300]",width=40,height=3,bg="DodgerBlue2",fg="white",font=(10))
    b.place(relx=0.5,rely=0.5,anchor="c")
    b=Button(m,text="EXECUTIVE [RS.450]",width=40,height=3,bg="DodgerBlue2",fg="white",font=(10))
    b.place(relx=0.5,rely=0.7,anchor="c")
    b5=Button(m,text="BACK",width=6,height=1,bg="firebrick1",fg="snow",font=(10),command=lambda: [f() for f in [m.destroy,q1]])
    b5.place(relx=0.9,rely=0.08,anchor="c")
def w5():
    m=Tk()
    m.minsize(1520,800)
    z1=300
    z2=400
    z3=550
    m.title("TIMINGS")
    m.configure(background="grey")
    l3=Label(m,text="SEAT TYPE",font=("Times New Roman",35),bg="grey",fg="red")
    l3.pack()
    b=Button(m,text="NORMAL [RS.300]",width=40,height=3,bg="DodgerBlue2",fg="white",font=(10))
    b.place(relx=0.5,rely=0.3,anchor="c")
    b=Button(m,text="SILVER [RS.400]",width=40,height=3,bg="DodgerBlue2",fg="white",font=(10))
    b.place(relx=0.5,rely=0.5,anchor="c")
    b=Button(m,text="EXECUTIVE [RS.550]",width=40,height=3,bg="DodgerBlue2",fg="white",font=(10))
    b.place(relx=0.5,rely=0.7,anchor="c")
    b5=Button(m,text="BACK",width=6,height=1,bg="firebrick1",fg="snow",font=(10),command=lambda: [f() for f in [m.destroy,q1]])
    b5.place(relx=0.9,rely=0.08,anchor="c")
    ########################################################################################################################################################
    
def q1():
    m=Tk()
    m.minsize(1520,800)
    m.title("TIMINGS")
    m.configure(background="grey")
    l3=Label(m,text="TIMINGS",font=("Times New Roman",35),bg="grey",fg="red")
    l3.pack()
    b5=Button(m,text="BACK",width=6,height=1,bg="firebrick1",fg="snow",font=(10),command=lambda: [f() for f in [m.destroy,a]])
    b5.place(relx=0.9,rely=0.08,anchor="c")
    b=Button(m,text="MORNING SHOW(9:00 to 12:30)",width=40,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,w1]])
    b.place(relx=0.5,rely=0.3,anchor="c")
    b=Button(m,text="MATINEE SHOW(1:00 to 2:30)",width=40,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,w1]])
    b.place(relx=0.5,rely=0.4,anchor="c")
    b=Button(m,text="EVENING SHOW(3:00 to 5:30)",width=40,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,w1]])
    b.place(relx=0.5,rely=0.5,anchor="c")
    b=Button(m,text="NIGHT SHOW(6:00 to 8:30)",width=40,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,w1]])
    b.place(relx=0.5,rely=0.6,anchor="c")
def q2():
    m=Tk()
    m.minsize(1520,800)
    m.title("TIMINGS")
    m.configure(background="grey")
    l3=Label(m,text="TIMINGS",font=("Times New Roman",35),bg="grey",fg="red")
    l3.pack()
    b5=Button(m,text="BACK",width=6,height=1,bg="firebrick1",fg="snow",font=(10),command=lambda: [f() for f in [m.destroy,c]])
    b5.place(relx=0.9,rely=0.08,anchor="c")
    b=Button(m,text="MORNING SHOW(9:00 to 12:30)",width=40,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,w2]])
    b.place(relx=0.5,rely=0.3,anchor="c")
    b=Button(m,text="MATINEE SHOW(1:00 to 2:30)",width=40,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,w2]])
    b.place(relx=0.5,rely=0.4,anchor="c")
    b=Button(m,text="EVENING SHOW(3:00 to 5:30)",width=40,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,w2]])
    b.place(relx=0.5,rely=0.5,anchor="c")
    b=Button(m,text="NIGHT SHOW(6:00 to 8:30)",width=40,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,w2]])
    b.place(relx=0.5,rely=0.6,anchor="c")
def q3():
    m=Tk()
    m.minsize(1520,800)
    m.title("TIMINGS")
    m.configure(background="grey")
    l3=Label(m,text="TIMINGS",font=("Times New Roman",35),bg="grey",fg="red")
    l3.pack()
    b5=Button(m,text="BACK",width=6,height=1,bg="firebrick1",fg="snow",font=(10),command=lambda: [f() for f in [m.destroy,d]])
    b5.place(relx=0.9,rely=0.08,anchor="c")
    b=Button(m,text="MORNING SHOW(9:00 to 12:30)",width=40,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,w3]])
    b.place(relx=0.5,rely=0.3,anchor="c")
    b=Button(m,text="MATINEE SHOW(1:00 to 2:30)",width=40,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,w3]])
    b.place(relx=0.5,rely=0.4,anchor="c")
    b=Button(m,text="EVENING SHOW(3:00 to 5:30)",width=40,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,w3]])
    b.place(relx=0.5,rely=0.5,anchor="c")
    b=Button(m,text="NIGHT SHOW(6:00 to 8:30)",width=40,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,w3]])
    b.place(relx=0.5,rely=0.6,anchor="c")
def q4():
    m=Tk()
    m.minsize(1520,800)
    m.title("TIMINGS")
    m.configure(background="grey")
    l3=Label(m,text="TIMINGS",font=("Times New Roman",35),bg="grey",fg="red")
    l3.pack()
    b5=Button(m,text="BACK",width=6,height=1,bg="firebrick1",fg="snow",font=(10),command=lambda: [f() for f in [m.destroy,e]])
    b5.place(relx=0.9,rely=0.08,anchor="c")
    b=Button(m,text="MORNING SHOW(9:00 to 12:30)",width=40,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,w4]])
    b.place(relx=0.5,rely=0.3,anchor="c")
    b=Button(m,text="MATINEE SHOW(1:00 to 2:30)",width=40,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,w4]])
    b.place(relx=0.5,rely=0.4,anchor="c")
    b=Button(m,text="EVENING SHOW(3:00 to 5:30)",width=40,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,w4]])
    b.place(relx=0.5,rely=0.5,anchor="c")
    b=Button(m,text="NIGHT SHOW(6:00 to 8:30)",width=40,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,w4]])
    b.place(relx=0.5,rely=0.6,anchor="c")
def q5():
    m=Tk()
    m.minsize(1520,800)
    m.title("TIMINGS")
    m.configure(background="grey")
    l3=Label(m,text="TIMINGS",font=("Times New Roman",35),bg="grey",fg="red")
    l3.pack()
    b5=Button(m,text="BACK",width=6,height=1,bg="firebrick1",fg="snow",font=(10),command=lambda: [f() for f in [m.destroy,f]])
    b5.place(relx=0.9,rely=0.08,anchor="c")
    b=Button(m,text="MORNING SHOW(9:00 to 12:30)",width=40,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,w5]])
    b.place(relx=0.5,rely=0.3,anchor="c")
    b=Button(m,text="MATINEE SHOW(1:00 to 2:30)",width=40,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,w5]])
    b.place(relx=0.5,rely=0.4,anchor="c")
    b=Button(m,text="EVENING SHOW(3:00 to 5:30)",width=40,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,w5]])
    b.place(relx=0.5,rely=0.5,anchor="c")
    b=Button(m,text="NIGHT SHOW(6:00 to 8:30)",width=40,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,w5]])
    b.place(relx=0.5,rely=0.6,anchor="c")

    
#######################movies details###################

def a():
    m=Tk()
    m.minsize(1520,800)
    m.title("ASURAN")
    m.configure(background="grey")
    l3=Label(m,text="Asuran (U/A)",font=("Times New Roman",35),bg="grey",fg="red")
    l3.place(x=30,y=30)
    l4=Label(m,text="Cast : Dhanush,Manju Warrier,Ken Karunas,Teejay,Prakash Raj,Pasupathy,Naren,Pawan",font=("Times New Roman",28),bg="grey",fg="white")
    l4.place(x=10,y=150)
    l5=Label(m,text="Director : Vetri Maaran",font=("Times New Roman",28),bg="grey",fg="white")
    l5.place(x=10,y=200)
    l6=Label(m,text="Music Composer : G V Prakash Kumar",font=("Times New Roman",28),bg="grey",fg="white")
    l6.place(x=10,y=250)
    l7=Label(m,text="Language : Tamil, Malayalam",font=("Times New Roman",28),bg="grey",fg="white")
    l7.place(x=10,y=300)
    l8=Label(m,text="The teenage son of a farmer from an underprivileged caste kills a rich, upper caste landlord.\n Will the farmer, a loving father and a pacifist by heart, be able to save his hot-blooded son is the rest.",font=("Baskervile Old Face",25),bg="grey",fg="snow")
    l8.place(x=10,y=400)
    b=Button(m,text="BOOK TICKETS",width=100,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,q1]])
    b.place(relx=0.5,rely=0.9,anchor="c")
    b5=Button(m,text="BACK",width=6,height=1,bg="firebrick1",fg="snow",font=(10),command=lambda: [f() for f in [m.destroy,o]])
    b5.place(relx=0.9,rely=0.08,anchor="c")
def c():
    m=Tk()
    m.minsize(1520,800)
    m.title("JOKER(A)")
    m.configure(background="grey")
    l3=Label(m,text="JOKER(A)",font=("Times New Roman",35),bg="grey",fg="red")
    l3.place(x=30,y=30)
    l4=Label(m,text="Cast : Joaquin, Robert, Zazie, Brian Tyree",font=("Times New Roman",28),bg="grey",fg="white")
    l4.place(x=10,y=150)
    l5=Label(m,text="Director : Todd Philips",font=("Times New Roman",28),bg="grey",fg="white")
    l5.place(x=10,y=200)
    l6=Label(m,text="Music Composer : Hildur",font=("Times New Roman",28),bg="grey",fg="white")
    l6.place(x=10,y=250)
    l7=Label(m,text="Language : English",font=("Times New Roman",28),bg="grey",fg="white")
    l7.place(x=10,y=300)
    l8=Label(m,text="Joker centers around an origin of the iconic arch nemesis and is an original,\n standalone story not seen before on the big screen. Todd Phillips' exploration of Arthur Fleck",font=("Baskervile Old Face",25),bg="grey",fg="snow")
    l8.place(x=10,y=400)
    b9=Button(m,text="BOOK TICKETS",width=100,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,q2]])
    b9.place(relx=0.5,rely=0.9,anchor="c")
    b5=Button(m,text="BACK",width=6,height=1,bg="firebrick1",fg="snow",font=(10),command=lambda: [f() for f in [m.destroy,o]])
    b5.place(relx=0.9,rely=0.08,anchor="c")
def d():
    m=Tk()
    m.minsize(1520,800)
    m.title("SyeRaa Narasimha Reddy (U)")
    m.configure(background="grey")
    l3=Label(m,text="SyeRaa Narasimha Reddy (U)",font=("Times New Roman",35),bg="grey",fg="red")
    l3.place(x=30,y=30)
    l4=Label(m,text="Cast : Chiranjeevi,Kicha Sudeep, Vijay Sethupathi,Jagapati Babu,Nayantara",font=("Times New Roman",28),bg="grey",fg="white")
    l4.place(x=10,y=150)
    l5=Label(m,text="Director : Surender Reddy",font=("Times New Roman",28),bg="grey",fg="white")
    l5.place(x=10,y=200)
    l6=Label(m,text="Music Composer : Amit Trivedi",font=("Times New Roman",28),bg="grey",fg="white")
    l6.place(x=10,y=250)
    l7=Label(m,text="Language : Telugu,Kannada,Tamil,Hindi",font=("Times New Roman",28),bg="grey",fg="white")
    l7.place(x=10,y=300)
    l8=Label(m,text="A chieftain of 66 villages in early colonial rule, Uyyalawada Narasimha Reddy, revolts against \n the atrocities of East India Company. He raids and defeats British Army camps\n and becomes a threat to the them.",font=("Baskervile Old Face",25),bg="grey",fg="snow")
    l8.place(x=10,y=400)
    b9=Button(m,text="BOOK TICKETS",width=100,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,q3]])
    b9.place(relx=0.5,rely=0.9,anchor="c")
    b5=Button(m,text="BACK",width=6,height=1,bg="firebrick1",fg="snow",font=(10),command=lambda: [f() for f in [m.destroy,o]])
    b5.place(relx=0.9,rely=0.08,anchor="c")


def e():
    m=Tk()
    m.minsize(1520,800)
    m.title("Pailwaan (U/A)")
    m.configure(background="grey")
    l3=Label(m,text="Pailwaan (U/A)",font=("Times New Roman",35),bg="grey",fg="red")
    l3.place(x=30,y=30)
    l4=Label(m,text="Cast : Kicha Sudeep,Sunil Shetty,Sushant Singh,Akansha Singh",font=("Times New Roman",28),bg="grey",fg="white")
    l4.place(x=10,y=150)
    l5=Label(m,text="Director : S Krishna",font=("Times New Roman",28),bg="grey",fg="white")
    l5.place(x=10,y=200)
    l6=Label(m,text="Music Composer : Arjun Janya",font=("Times New Roman",28),bg="grey",fg="white")
    l6.place(x=10,y=250)
    l7=Label(m,text="Language : Kannada, Telugu, Tamil, Malayalam",font=("Times New Roman",28),bg="grey",fg="white")
    l7.place(x=10,y=300)
    l8=Label(m,text=" The film follows the journey of an orphan who goes on to become a wrestler and a boxer while getting \n into brawls with those who disrupt his personal life.",font=("Baskervile Old Face",25),bg="grey",fg="snow")
    l8.place(x=10,y=400)
    b9=Button(m,text="BOOK TICKETS",width=100,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,q4]])
    b9.place(relx=0.5,rely=0.9,anchor="c")
    b5=Button(m,text="BACK",width=6,height=1,bg="firebrick1",fg="snow",font=(10),command=lambda: [f() for f in [m.destroy,o]])
    b5.place(relx=0.9,rely=0.08,anchor="c")

def f():
    m=Tk()
    m.minsize(1520,800)
    m.title("Chichhorre (U)")
    m.configure(background="grey")
    l3=Label(m,text="Chichhorre (U)",font=("Times New Roman",35),bg="grey",fg="red")
    l3.place(x=30,y=30)
    l4=Label(m,text="Cast :Sushant Singh, Shradda Kapoor, Varun Sharma, Akansha Singh",font=("Times New Roman",28),bg="grey",fg="white")
    l4.place(x=10,y=150)
    l5=Label(m,text="Director :  Nithesh Tiwari",font=("Times New Roman",28),bg="grey",fg="white")
    l5.place(x=10,y=200)
    l6=Label(m,text="Music Composer : Pritam",font=("Times New Roman",28),bg="grey",fg="white")
    l6.place(x=10,y=250)
    l7=Label(m,text="Language : Hindi",font=("Times New Roman",28),bg="grey",fg="white")
    l7.place(x=10,y=300)
    l8=Label(m,text=" The setup was within 1990's till present where Anni, a divorcee used his past experience in overcoming \n challenges of being a loser in college where he met His Wife, Maya and his Losers friends,\n Saxa, Mummy, Acid, Derek and Bevda. His shares past experience to his son,\n Raghav who struggles with being failed at getting an offer to college despite\n being an excellent student.",font=("Baskervile Old Face",25),bg="grey",fg="snow")
    l8.place(x=10,y=400)
    b9=Button(m,text="BOOK TICKETS",width=100,height=2,bg="DodgerBlue2",fg="white",font=(10),command=lambda: [f() for f in [m.destroy,q5]])
    b9.place(relx=0.5,rely=0.9,anchor="c")
    b5=Button(m,text="BACK",width=6,height=1,bg="firebrick1",fg="snow",font=(10),command=lambda: [f() for f in [m.destroy,o]])
    b5.place(relx=0.9,rely=0.08,anchor="c")
    
    
    
################################################movies list #######################################    
def o():
    m2=Tk()
    m2.minsize(1520,800)
    m2.title("MOVIES LIST")
    m2.configure(background="grey")
   
    l2=Label(m2,text="MOVIES LIST",font=("Times New Roman",33),bg="grey",fg="firebrick1")
    l2.place(x=600,y=30)
    b=Button(m2,text="Asuran (U/A)\n\nAction, Drama",width=15,height=10,bg="firebrick1",fg="snow",font=(25),command=lambda: [f() for f in [a,m2.destroy]])
    b.place(relx=0.17,rely=0.3,anchor="c")
    b1=Button(m2,text="Joker (A)\n\nCrime,Fantasy,\nThriller",width=15,height=10,bg="firebrick1",fg="snow",font=(25),command=lambda: [f() for f in [c,m2.destroy]])
    b1.place(relx=0.50,rely=0.3,anchor="c")
    b2=Button(m2,text="SyeRaa Narasimha\nReddy (U)\n\nAction,Drama",width=15,height=10,bg="firebrick1",fg="snow",font=(25),command=lambda: [f() for f in [d,m2.destroy]])
    b2.place(relx=0.80,rely=0.3,anchor="c")
    b3=Button(m2,text="Pailwaan (U/A)\n\nAction, Drama",width=15,height=10,bg="firebrick1",fg="snow",font=(25),command=lambda: [f() for f in [e,m2.destroy]])
    b3.place(relx=0.34,rely=0.7,anchor="c")
    b4=Button(m2,text="Chichhorre (U)\n\nComedy,Romantic,\nDrama",width=15,height=10,bg="firebrick1",fg="snow",font=(25),command=lambda: [f() for f in [f,m2.destroy]])
    b4.place(relx=0.65,rely=0.7,anchor="c")
    
    b5=Button(m2,text="BACK",width=6,height=1,bg="firebrick1",fg="snow",font=(10),command=lambda: [f() for f in [m2.destroy,r]])
    b5.place(relx=0.9,rely=0.08,anchor="c")
    
    ####################trailer#################
def p():
    
    m3=Tk()
    m3.minsize(1520,800)
    m3.title("TRAILERS AND REVIEW")
    m3.configure(background="grey")
    l3=Label(m3,text="B",font=("Times New Roman",30),bg="grey",fg="firebrick1").pack()
    

    ###################snacks################333
def q():
    m4=Tk()
    m4.minsize(1520,800)
    m4.title("SNACKS AND REFRESHMENTS")
    m4.configure(background="grey")
    l4=Label(m4,text="MOVIES LIST",font=("Times New Roman",30),bg="grey",fg="firebrick1").pack()
    #################second page (books= tickets ,snacks,trailers#######################
def r():
    m.destroy
    m1=Tk()
    m1.title("HOME")
    m1.minsize(1520,800)
    m1.configure(background="grey")
    l1=Label(m1,text='COVAI CINEMAS',font=("ALGERIAN",40),bg='grey',fg='red')
    l1.place(x=550,y=100)
    b=Button(m1,text="BOOK TICKETS",width=30,height=2,bg="firebrick1",fg="snow",font=(25),command=lambda: [f() for f in [o,m1.destroy]])
    b.place(relx=0.17,rely=0.5,anchor="c")
    b1=Button(m1,text="REVIEWS AND TRAILERS",width=30,height=2,bg="firebrick1",fg="snow",font=25,command=lambda: [f() for f in [p,m1.destroy]])
    b1.place(relx=0.50,rely=0.5,anchor="c")
    b2=Button(m1,text="SNACKS AND REFRESHMENTS",width=30,height=2,bg="firebrick1",fg="snow",font=25,command=lambda: [f() for f in [q,m1.destroy]])
    b2.place(relx=0.82,rely=0.5,anchor="c")
    b3=Button(m1,text="EXIT",width=20,height=2,bg="firebrick1",fg="snow",font=25,command=m1.destroy)
    b3.place(relx=0.85,rely=0.9,anchor="c")
    m1.mainloop()
    
    

    


######################(first page)welcome page###################### 

m=Tk()

m.title("TICKET BOOKING")
m.minsize(1520,800)
l=Label(m,text="WELCOME TO COVAI CINEMAS",font=("ALGERIAN",40),bg="firebrick1",fg="snow")
l.place(x=400,y=300)
l1=Label(m,text="Get into reality...........",font=("Times New Roman",29),bg="firebrick1",fg="snow")
l1.place(x=950,y=400)
m.configure(background="firebrick1")
m.after(50,lambda: [f() for f in [r]])
m.after(51,lambda:m.destroy())
m.mainloop()

