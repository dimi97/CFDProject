import numpy as np


class myCons:
    #myConstants
    nx = 41
    ny = 41
    nit= 500
    c = 1
    dx = 1./(nx-1)
    dy = 1./(ny-1)
    x = np.linspace(0,1,nx)
    y = np.linspace(0,1,ny)
    X,Y = np.meshgrid(x,y)
    
    rho = 1
    visc = 0.1
    dt = 0.001
    T0 = 0
    T_high = 1
    D = 0.1
    g = 1
    beta = 0.01
    v0= np.zeros(nx)
    nt=50
    
    
    
class myConsTest:
    #myConstants
    nx = 50
    ny = 50
    nit  = 100
    xmin = 0
    xmax = 2
    ymin = 0
    ymax = 1
    
    dx = (xmax - xmin) / (nx - 1)
    dy = (ymax - ymin) / (ny - 1)
    
    x  = np.linspace(xmin, xmax, nx)
    y  = np.linspace(xmin, xmax, ny)
    
    #further testing variables
    rho=1