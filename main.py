from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from myCons import myCons
from cfd import cfd
from misc import misc
from poisson import poisson
from graph import graph
#array of dimensions -1 in every direction consisting of the next elemenent of the centered array.



    
#calculate velocity for t+dt. First imput->velocity being calculated.
def vTStep(myVar,u,v,p):
    if myVar=="x":
        u1=u.copy()
        u2=v.copy()
        
    elif myVar=="y":
        u1=v.copy()
        u2=u.copy()
        
        
    
    u1[1:-1,1:-1]=cfd.centerElementArray(u1)\
        -cfd.centerElementArray(u)*myCons.dt*cfd.BD(u1,"x")\
        -cfd.centerElementArray(v)*myCons.dt*cfd.BD(u2,"y")\
        -(myCons.dt/(2*myCons.rho))*cfd.CD(p,myVar)\
        +myCons.visc*myCons.dt*(cfd.SOD(u1,"x")+cfd.SOD(u2,"y"))
        
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
    T=misc.TInitial(T)
    u=misc.vInitial(u)
    v=misc.vInitial(v)
    
    
    
    for n in range(nt):
        un=u.copy()
        vn=v.copy()
        Tn=T.copy()
        
        p=poisson.pressure(p, un, vn,bArray)
        u=vTStep("x", un, vn, p)
        #v=vTStep("y", un, vn, p)
        v=vTStepGravity("y", un, vn, p,Tn)
        T=TTStep(Tn, un, vn)
        
        flowTest(n,u,v,T,p,bArray)
        
    return u,v,p,T

def flowTest(n,u,v,T,p,bArray):
    
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
    
    nt=myCons.nt
    u,v,p,T=flow(u,v,T,p,bArray,nt)
    
    graph.graphStuff(T,nt,u,v)
    


def testPoisson():
    print("hello there poisson test")
    u=misc.initArray(0)
    v=misc.initArray(0)
    p=misc.initArray(0)
    bArray=misc.initArray(0)
    T=misc.initArray(myCons.T0)
    
    
    nt=myCons.nt
    
    p=poisson.pressure(p, u, v, bArray)
    
    graph.plot2D(myCons.x, myCons.y, p)
    
#main()
testPoisson()



print("DONE")




