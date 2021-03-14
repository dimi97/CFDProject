from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from myCons import myCons
from cfd import cfd
from misc import misc
from poisson import poisson
from graph import graph
  
#calculate velocity for t+dt. First input->velocity being calculated.
def vTStep(myVar,u,v,p):
    if myVar=="x":
        u1=u.copy()
        
    elif myVar=="y":
        u1=v.copy()
        
    u1[1:-1,1:-1]=cfd.centerElementArray(u1)\
        -cfd.centerElementArray(u)*myCons.dt*cfd.BD(u1,"x")\
        -cfd.centerElementArray(v)*myCons.dt*cfd.BD(u1,"y")\
        -(myCons.dt/(2*myCons.rho))*cfd.CD(p,myVar)\
        +myCons.visc*myCons.dt*(cfd.SOD(u1,"x")+cfd.SOD(u1,"y"))
        
    return u1

#calculate velocity t+dt with gravity.
def vTStepGravity(myVar,u,v,p,T):
    oldV=vTStep(myVar,u,v,p)
    
    oldV[1:-1,1:-1]=cfd.centerElementArray(oldV)\
     -(1-myCons.beta*(cfd.centerElementArray(T)))*myCons.g*myCons.dt
    #oldV[1:-1,1:-1]=cfd.centerElementArray(oldV)
    return oldV
            
    
def TTStep(T,u,v):
    Tn=np.empty_like(T)
    Tn=T.copy()
    
    T[1:-1,1:-1] = Tn[1:-1,1:-1]\
        +myCons.dt*(\
        +myCons.D*(cfd.SOD(Tn,"x")+cfd.SOD(Tn,"y"))\
        -(cfd.centerElementArray(u)*cfd.CD(T,"x")+cfd.centerElementArray(v)*cfd.CD(T,"y"))\
        -cfd.centerElementArray(T)*(cfd.CD(u,"x")+cfd.CD(v,"y"))    
     )
            
    return T


    
def flow(u,v,T,p,bArray,nt):
    # T=misc.TInitial(T)
    # u=misc.vInitial(u)
    # v=misc.vInitial(v)
    
    
    
    for n in range(nt):
        un=u.copy()
        vn=v.copy()
        Tn=T.copy()
        
        p=poisson.pressure(p, un, vn,bArray)
        u=vTStep("x", un, vn, p)
        v=vTStepGravity("y", un, vn, p,Tn)
        T=TTStep(Tn, un, vn)
        
        flowPrint(n,u,v,T,p,bArray)
        
        T=misc.TInitial(T)
        u=misc.vInitial(u)
        v=misc.vInitial(v)
        
    return u,v,p,T

def flowPrint(n,u,v,T,p,bArray):
    
    print("Time step:",n)
    print("u Array")
    print(u)
    print("v Array")
    print(v)
    print("T Array")
    print(T)
    print("p Array")
    print(p)
    print("b Array")
    print(bArray)
    



def main():
    print("hello there main")
    u=misc.initArray(0)
    v=misc.initArray(0)
    p=misc.initArray(0)
    bArray=misc.initArray(0)
    T=misc.initArray(myCons.T0)
    
    nt=500
    u,v,p,T=flow(u,v,T,p,bArray,nt)
    
    graph.graphStuff(T,nt,u,v)
    
    
main()




print("DONE")




