import numpy as np
import cupy as cp
A = cp.array([[-2, 1, 1, 0, 0],
             [-1, 2, 0, 1, 0],
             [1, 0, 0, 0, 1]])

b = cp.array([2, 7, 3])

c = cp.array([-1, -2, 0, 0, 0])

def Simplex(A, b, c):
    
    basicSize = A.shape[0] # number of constraints, m
    nonbasicSize = A.shape[1] - basicSize #n-m, number of variables
    cindx = [i for i in range(0, len(c))]
    
    cbT = cp.array(c[nonbasicSize:])
    cnT = cp.array(c[:nonbasicSize])
    while True:
        
        cbIndx = cindx[nonbasicSize:]
        cnIndx = cindx[:nonbasicSize]

        B = A[:, cbIndx]
        Binv = cp.linalg.inv(B)

        N = A[:, cnIndx]
        bHat = Binv @ b
        yT = cbT @ Binv

        cnHat = cnT - (yT @ N)
        
        cnMinIndx = int(cp.argmin(cnHat))

        if(all(i>=0 for i in cnHat)):
           
            return cbT, cbIndx, cnT, cnIndx, bHat, cnHat
        
        indx = cindx[cnMinIndx]

        Ahat = Binv @ A[:, indx]
        
        ratios = cp.ndarray(len(bHat), dtype=float)
        for i in range(0, len(bHat)):
            Aval = Ahat[i]
            Bval = bHat[i]

            if(Aval <= 0):
                ratios[i] = 10000000
                continue
            to_append = Bval / Aval
            ratios[i] = to_append
            
        ratioMinIndx = int(cp.argmin(cp.asanyarray(ratios)))
        cbt_inp_array = cp.ndarray(cbT.size, dtype=int)
        for i in range(0, cbT.size):
          if i != ratioMinIndx:
            cbt_inp_array[i] = cbT[i]
          else :
            cbt_inp_array[i] = cnT[cnMinIndx]



        cNt_inp_array = cp.ndarray(cnT.size, dtype=int)
        for i in range(0, cnT.size):
          if i != cnMinIndx:
            cNt_inp_array[i] = cnT[i]
          else :
            cNt_inp_array[i] = cbT[ratioMinIndx]

        cp.copyto(cbT, cbt_inp_array)
        cp.copyto(cnT, cNt_inp_array)
        cindx[cnMinIndx], cindx[ratioMinIndx + nonbasicSize] = cindx[ratioMinIndx + nonbasicSize], cindx[cnMinIndx]
        

Simplex(A, b, c) 
