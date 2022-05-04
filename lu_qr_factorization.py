
from time import time
import numpy as np
from pprint import pprint
from timeit import timeit

def lu_factorization(A):
    '''
    Simple algorithm for lu factorization

    https://johnfoster.pge.utexas.edu/numerical-methods-book/LinearAlgebra_LU.html

    https://www.geeksforgeeks.org/doolittle-algorithm-lu-decomposition/ 
    '''
    n = A.shape[0]

    U = A.copy()
    L = np.eye(n, dtype=np.double)

    for i in range(n):
        temp = U[i+1:, i] / U[i, i]
        L[i+1:, i] = temp
        U[i+1:] -= temp[:, np.newaxis] * U[i]
    
    return L, U

def cool_gpu_cpu_lu_factorization(A):
    '''
    Algorithm from this article: https://www.hindawi.com/journals/mpe/2019/3720450/
    '''

def qr_factorization(A):
    '''
    just numpy
    '''
    return np.linalg.qr(A)

if __name__ == "__main__":
    # A = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]], dtype=np.double)

    
    setup = """import numpy as np
A = np.random.random((10, 10))
    """
    my_code_first = "lu_factorization(A)"
    my_code_second = "qr_factorization(A)"
    print(timeit(setup = setup, stmt=my_code_first, number = 100, globals=globals()))
    print(timeit(setup = setup, stmt=my_code_second, number = 100, globals=globals()))


    """
    10.744100361999699 lu - 500 - 100 
    17.12865626200073  qr - 500 - 100
    """

    """
    1.5031215569997585 lu - 250 - 100
    2.2523477710001316 qr - 250 - 100
    """

    """
    0.1512211319995913  lu - 100 - 100
    0.12111618499966426 qr - 100 - 100
    """

    """
    0.04376586499984114 lu - 50 - 100
    0.02339573900007963 qr - 50 - 100
    """

    """
    0.006281166000007943  lu - 10 - 100
    0.0027356849996067467 qr - 10 - 100
    """