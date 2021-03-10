#ENitz
from tkinter import *
import matplotlib.pyplot as plt
#import Diagramm

def get_entry_fields():
    tN=open('txtN.txt', 'w')
    tI=open('txtI.txt', 'w')
    tt=open('txtt.txt', 'w')
    
    N=eN.get()
    I=eI.get()
    t=et.get()
    
    tN.write(N)
    tI.write(I)
    tt.write(t)
    
    tN.close()
    tI.close()
    tt.close()

def SIR (N0, I0, a, b, days, R0=0, samples=200, steps=10000):
    L, S, I, R= [], N0-R0-I0, I0, R0
    step, sampleStep = days/steps , steps//samples
    for i in range(steps+1):
        if i%sampleStep ==0:
            d=i*step
            L.append((d,S,I,R))
        S, I = S*(1-(float(a*I*step))), I*(1+(a*S-b)*step)
        R= N0-S-I
    SWert=list(map(lambda p: (p[1]),L))
    IWert=list(map(lambda p: (p[2]),L))
    RWert=list(map(lambda p: (p[3]),L))
    dWert=list(map(lambda p: (p[0]),L))
    plt.plot(dWert, SWert, "g")
    plt.plot(dWert, IWert, "r")
    plt.plot(dWert, RWert, "b")
    plt.xlabel("Tage")
    plt.ylabel("Menschen")
    plt.show()
    

root = Tk()
root.state("zoomed")

frame1=Frame(root)
frame2=Frame(root)
frame3=Frame(root)
frame4=Frame(root)

#frame1
Feld=Label(frame1,text="Das Feld")
Feld.grid(row=0,column=0)

#frame2
eN=Entry(frame2)
eN.grid(row=0,column=0)
eI=Entry(frame2)
eI.grid(row=1,column=0)
et=Entry(frame2)
et.grid(row=2,column=0)
ea=Entry(frame2)
ea.grid(row=3,column=0)
eD=Entry(frame2)
eD.grid(row=4,column=0)

TN=Label(frame2,text="Personen insgesamt")
TN.grid(row=0,column=1)
TI=Label(frame2, text="Anfangsinfizierte")
TI.grid(row=1,column=1)
Tt=Label(frame2, text="Krankheitsdauer")
Tt.grid(row=2,column=1)
Ta=Label(frame2, text="alpha")
Ta.grid(row=3, column=1)
TD=Label(frame2, text="anzuzeigende Dauer")
TD.grid(row=4, column=1)

Button(frame2,text="starten", command=get_entry_fields).grid(row=5,column=0,columnspan=2)

frame2.columnconfigure(0, weight=1)
frame2.columnconfigure(1, weight=3)

#frame3
    
N0=float(input("N0= "))
I0=float(input("I0= "))
a=float(input("alpha= "))
duration=float(input("Krankheitsdauer= "))
b=1/duration
days=float(input("anzuzeigende Dauer= "))

chart=SIR(N0,I0,a,b,days,R0=0,samples=200,steps=10000)

chart.grid(row=0,column=0)

#frame4
Iaktuell=Label(frame4, text="?")
Iaktuell.grid(row=0, column=0)
Saktuell=Label(frame4,text="yy gesund")
Saktuell.grid(row=1, column=0)


frame1.grid(row=0,column=0)
frame2.grid(row=0,column=1)
frame3.grid(row=1,column=0)
frame4.grid(row=1,column=1)

root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=3)
root.rowconfigure(1, weight=1)

mainloop()