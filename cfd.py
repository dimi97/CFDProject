import numpy as np
from myCons import myCons

class cfd:
        
    def fwdElementArray (myArray,myVar):
        if myVar=="x":
            
            a=1
            b=-1
            
            c=2
            d=len(myArray[0])
            
        elif myVar=="y":
             a=2
             b=len(myArray)
            
             c=1
             d=-1
            
        return myArray[a:b,c:d]
    
    #array of dimensions -1 in every direction consisting of the next elemenent of the centered array.
    def bwElementArray (myArray,myVar):
        if myVar=="x":
            
            e=1
            f=-1
            
            g=0
            h=-2
            
        elif myVar=="y":
             e=0
             f=-2
            
             g=1
             h=-1
            
        return myArray[e:f,g:h]
    
    #array without the border values.
    def centerElementArray(myArray):
        return myArray[1:-1,1:-1]
   
    #find dx or dy
    def findDif(myVar):
         if myVar=="x":
            dif=myCons.dx
         elif myVar=="y":
            dif=myCons.dy
         return dif   
    
    #calculate Central Difference
    def CD(myArray,myVar):
             
        newArray=cfd.fwdElementArray(myArray,myVar)-cfd.bwElementArray(myArray,myVar)
        
        dif=cfd.findDif(myVar)
        
        
        res=newArray/(2*dif)
        return res
        
    #calculate Backward Difference
    def BD(myArray,myVar):
        
        newArray=cfd.centerElementArray(myArray)-cfd.bwElementArray(myArray,myVar)
        
        dif=cfd.findDif(myVar)
            
        res=newArray/dif
        
        return res


    #calculate Second Order Difference
    def SOD(myArray,myVar):
        dif=cfd.findDif(myVar)
        
        newArray=cfd.fwdElementArray(myArray,myVar)-2*cfd.centerElementArray(myArray)+cfd.bwElementArray(myArray,myVar)
        
        res=newArray/dif**2
        return res
    
    
    

