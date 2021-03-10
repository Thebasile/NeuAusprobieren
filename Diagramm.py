import matplotlib.pyplot as plt

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
    plt.plot(dWert, SWert, "g", label="gesund")
    plt.plot(dWert, IWert, "r", label="infiziert")
    plt.plot(dWert, RWert, "b", label="removed")
    plt.xlabel("Tage")
    plt.ylabel("Menschen")
    plt.legend(loc="upper right")
    plt.show()
    
N0=float(input("N0= "))
I0=float(input("I0= "))
a=float(input("alpha= "))
duration=float(input("Krankheitsdauer= "))
b=1/duration
days=float(input("anzuzeigende Dauer= "))

SIR(N0,I0,a,b,days,R0=0,samples=200,steps=10000)