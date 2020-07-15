import pandas as pd
import numpy as np
from datetime import datetime as dt
from math import sqrt
import scipy.fftpack as fft



def class1(f):
    
    ff=0
    if f<=1.8:
        ff=0
        print("Good Condition")
    elif f>1.8 and f<4.5:
        ff=15
        print("Acceptable Condition")
    elif f>4.5 and f<7.1:
        ff=40
        print("Problem Raising Condition")
    elif f>7.1 and f<71:
        ff=75
        print("Immediate Stop Condition")
    return ff    
    

def class2(f):
     
    ff=0
    if f<=2.8:
        ff=0
        print("Good Condition")
    elif f>2.8 and f<7.1:
        ff=15
        print("Acceptable Condition")
    elif f>7.1 and f<11.1:
        ff=40
        print("Problem Raising Condition")
    elif f>11.1 and f<71:
        ff=75
        print("Immediate Stop Condition")
  
    
    return ff

def class3(f):
    
     
    ff=0
    if f<=4.5:
        ff=0
        print("Good Condition")
    elif f>4.5 and f<11.1:
        ff=15
        print("Acceptable Condition")
    elif f>11.1 and f<18:
        ff=40
        print("Problem Raising Condition")
    elif f>18 and f<71:
        ff=75
        print("Immediate Stop Condition")
    return ff
    
def class4(f):
    
    ff=0
    if f<=2.8:
        ff=0
        print("Good Condition")
    elif f>2.8 and f<11.1:
        ff=15
        print("Acceptable Condition")
    elif f>11.1 and f<18.0:
        ff=40
        print("Problem Raising Condition")
    elif f>18.0 and f<71:
        ff=75
        print("Immediate Stop Condition")
        
    
    
    return ff

def calfft(xf):
    V=[]
    ffft=xf.values 
    y=(2/len(ffft))*(fft.fft(ffft))  
    pi=3.14
    nbins=len(xx)                     
    chfre=fs/sam             
    for i in range(0,nbins):
        k=y[i]
        V.append(k*1000*0.707/(2*pi*i*chfre)) 
    
    ln=len(V)
                        
    V=np.abs(V)
    V[0]=0
    VV=[]                      
            
    for i in range(ln):              
        if (V[i]<=0.01 and V[i]>0.001) :
            VV.append(0.01)
        else:
            VV.append(V[i])
    return VV





df2=pd.read_csv("NEWSENSOR6_3.CSV")

xx=df2.X_axis*3.9*9.805*0.001  
yy=df2.Y_axis*3.9*9.805*0.001  
zz=df2.Z_axis*3.9*9.805*0.001  
overall_vib=(xx**2+yy**2+zz**2)**0.5       
p=2;f=50;fs=1600;sam=32*p//2;n=int(len(xx)/sam);T=1/f;Ts=1/fs
t=np.arange(0,p*T/2,Ts)
freq=fft.fftfreq(sam,Ts)        
x=xx[0:sam]                      
X_FFT=calfft(xx)
Y_FFT=calfft(yy)
Z_FFT=calfft(zz)
OV_Vib=calfft(overall_vib)

pw=30
h=max(OV_Vib)        #>>>>>>> taking maximum vibration value from the data
print("\n\n Health: ",h,"mm/sec of Vibration Detected\n\n")
if pw<=15:
    f_stat=class1(h)    
elif pw>15 and pw<=75:
    f_stat=class2(h)
elif pw>75 and pw<10000:
    f_stat=class3(h)
elif pw>=10000:
    f_stat=class4(h)

syshealth=(100-f_stat)
print("Fault State is \n",f_stat)
print("lenght of sample is \n",len(OV_Vib),len(Z_FFT))
print("Vibration Data is \n",OV_Vib)

df1=pd.DataFrame()

df1['date']=df2.date
df1['X_axis']=X_FFT
df1['Y_axis']=Y_FFT
df1['Z_axis']=Z_FFT
df1['Overall_vibration']=OV_Vib

print("new dataframe is \n",df1.tail())
