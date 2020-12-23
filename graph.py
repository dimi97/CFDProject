from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from myCons import myCons
from matplotlib import pyplot, cm




class graph:
    
    
    def makegraph(T,nt,u,v):
        plt.contourf(myCons.X,myCons.Y,T,20)    
        plt.colorbar()
        plt.quiver(myCons.X[::1,::1],myCons.Y[::1,::1],u[::1,::1],v[::1,::1],0) 
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Time Step %s' %(nt))

    def graphStuff(T,nt,u,v):
        fig = plt.figure(figsize=(15,6), dpi=100)
        ax = fig.add_subplot(121)
        graph.makegraph(T, nt, u, v)
        plt.tight_layout()
        
        
        
    def plot2D(x, y, p):
        fig = pyplot.figure(figsize=(11, 7), dpi=100)
        ax = fig.gca(projection='3d')
        X, Y = np.meshgrid(x, y)
        surf = ax.plot_surface(X, Y, p[:], rstride=1, cstride=1, cmap=cm.viridis,
                linewidth=0, antialiased=False)
        ax.view_init(30, 225)
        ax.set_xlabel('$x$')
        ax.set_ylabel('$y$')     