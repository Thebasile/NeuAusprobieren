#ENitz
from tkinter import *
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
    

root = Tk()
root.state("zoomed")

frame1=Frame(root)
frame2=Frame(root)
frame3=Frame(root)
frame4=Frame(root)

#frame1
Feld=Label(frame1,text="Punkte in Feld")
Feld.grid(row=0,column=0)

#frame2
eN=Entry(frame2)
eN.grid(row=0,column=0)
eI=Entry(frame2)
eI.grid(row=1,column=0)
et=Entry(frame2)
et.grid(row=2,column=0)
steadya=Label(frame2, text="Setiger Wert für alpha")
steadya.grid(row=3,column=0)
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
Diagramm=Label(frame3, text="Diagramm")
#Diagramm=Diagramm.SIR(N0,I0,a,b,days,R0=0,samples=200,steps=10000)
Diagramm.grid(row=0,column=0)


#frame4
Iaktuell=Label(frame4, text="xx infiziert")
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