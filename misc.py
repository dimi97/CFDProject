import numpy as np
from myCons import myCons


class misc:
   
    #initialize an array of correct dimensions to zeros.
    def initArray(value):
        
        if value==0:
            return np.zeros((myCons.ny,myCons.nx))     
        else:
            return np.ones((myCons.ny,myCons.nx))*value

    
    def TInitial(T):
        T[0,:] = myCons.T_high
        T[:,0] = 2*T[:,1]-T[:,2]
        T[:,-1] = 2*T[:,-2]-T[:,-3]
        T[-1,:] = myCons.T0    
        return T

    def vInitial(vel):
        vel[0,:] = 0
        vel[-1,:] = 0
        vel[:,0] = 0
        vel[:,-1] = 0
        return vel