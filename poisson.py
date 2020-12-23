import numpy as np

from myCons import myCons as myCons
from cfd import cfd
from misc import misc

class poisson:
    
        #calculate pressure operating in pseudo time.
    def pressure(p,u,v,bArray):
        pn = np.empty_like(p)
        
        b=poisson.poissonB(u,v,bArray)
        #b=poisson.testB()
        
        for q in range(myCons.nit):
            pn=p.copy()
            p[1:-1,1:-1]=(\
                (cfd.fwdElementArray(pn, "x")+cfd.bwElementArray(pn,"x"))*myCons.dy**2\
                +(cfd.fwdElementArray(pn,"y")+cfd.bwElementArray(pn,"y"))*myCons.dx**2\
                    )\
                /(2*(myCons.dx**2+myCons.dy**2))\
                    -((myCons.dx**2*myCons.dy**2)/(2*(myCons.dx**2+myCons.dy**2)))*cfd.centerElementArray(b)
                    
                    #rho is contained in the b term.
                    
                    
            p=poisson.pressureBoundary(p)
           #p=poisson.pressureBoundaryTest(p)
            
        return p
        
    #calculate B side of poisson differential equation.
    def poissonB(u,v,bArray):   
        bArray[1:-1,1:-1]=myCons.rho*( \
                          (1/myCons.dt)*(cfd.CD(u,"x")+cfd.CD(v,"y"))\
                          -cfd.CD(u,"x")**2-cfd.CD(v,"y")**2-2*cfd.CD(u,"y")*cfd.CD(v,"x")\
                              )
                            
        return bArray 

    def pressureBoundary(p):
            p[-1,:] = p[-2,:] #dp/dy = 0 at y = 2
            p[0,:] = p[1,:]  #dp/dy = 0 at y = 0
            p[:,0] = p[:,1]  #dp/dx = 0 at x = 0
            p[:,-1] = p[:,-2] #dp/dx=0 at x=2
            p[0,0] = 0   #initalize the pressure
            
            return p
        
    def pressureBoundaryTest(p):
            p[0, :] = 0
            p[myCons.ny-1, :] = 0
            p[:, 0] = 0
            p[:, myCons.nx-1] = 0
            
            return p
        
    def testB():
        b=np.zeros((myCons.ny, myCons.nx))
        b[int(myCons.ny / 4), int(myCons.nx / 4)]  = 100
        b[int(3 * myCons.ny / 4), int(3 * myCons.nx / 4)] = -100
        return b 
        
        
    def testPoisson():
        
        p=np.zeros((myCons.ny, myCons.nx))
        
        
        p=poisson.pressure(p,0,0,0)
            
        return p   
            
            
        
            
           
            #TEST the poisson function
           
# p=poisson.testPoisson()   



# # Parameters
# nx = 50
# ny = 50
# nt  = 100
# xmin = 0
# xmax = 2
# ymin = 0
# ymax = 1

# dx = (xmax - xmin) / (nx - 1)
# dy = (ymax - ymin) / (ny - 1)

# x  = np.linspace(xmin, xmax, nx)
# y  = np.linspace(xmin, xmax, ny)
              
# poisson.plot2D(x,y,p)
# print(p)       
        
        
        
        
        
        
        
        
        
        
        
        
        