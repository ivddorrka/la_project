import numpy as np
import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library
# import numpy as np
from numpy.linalg import eig
import math
import time

def generate_hermitian(row_col_number):
    A = np.random.randint(1000, size=(row_col_number, row_col_number))
    w,v=eig(A)
    maxim = (max(list(w)))
    identity_matrix = np.identity(row_col_number)
    A = A+maxim*identity_matrix
    A_T = A.transpose();
    A = 0.5*(A+A_T)
    return A