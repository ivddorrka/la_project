from matrx_generation import *
import matplotlib.pyplot as plt



def column_convertor(x):
    """
    Converts 1d array to column vector
    """
    x.shape = (1, x.shape[0])
    return x

def get_norm(x):
    """
    Returns Norm of vector x
    """
    return np.sqrt(np.sum(np.square(x)))

def householder_transformation(v):
    """
    Returns Householder matrix for vector v
    """
    size_of_v = v.shape[1]
    e1 = np.zeros_like(v)
    e1[0, 0] = 1
    vector = get_norm(v) * e1
    if v[0, 0] < 0:
        vector = - vector
    u = (v + vector).astype(np.float32)
    H = np.identity(size_of_v) - ((2 * np.matmul(np.transpose(u), u)) / np.matmul(u, np.transpose(u)))
    return H

def qr_step_factorization(q, r, iter, n):
    """
    Return Q and R matrices for iter number of iterations.
    """
    v = column_convertor(r[iter:, iter])
    Hbar = householder_transformation(v)
    H = np.identity(n)
    H[iter:, iter:] = Hbar
    r = np.matmul(H, r)
    q = np.matmul(q, H)
    return q, r



def obtain_QR(A, n, m):
    Q = generate_identity_m(n)
    R = A.astype(np.float32)
    for i in range(min(n, m)):
        Q, R = qr_step_factorization(Q, R, i, n)
    min_dim = min(m, n)
    R = np.around(R, decimals=2)
    R = R[:min_dim, :min_dim]
    Q = np.around(Q, decimals=6)
    return Q, R



# A = generate_random_matrix(3, 3)
# res = obtain_QR(A, 3, 3)
# print(res[0])
# print(res[1])

# lst_sizes = []

# lst_times_algo = []
# i =2

# while i <= 1025:
#     n = i
#     matrix = generate_random_matrix(n, n)
#     # print(matrix)
#     start = time.time()
#     res_nmp = obtain_QR(matrix, n, n)
#     end = time.time()
#     res_time = end-start
#     lst_times_algo.append(res_time)
#     lst_sizes.append(n)
#     i = i*2


lst_sizes = [10, 100, 250, 500, 1000]
time_lu = [0.00028228759765625,  0.003760099411010742, 0.02787303924560547, 0.18905925750732422, 1.424250602722168]
time_qr = [0.0005943775177001953, 0.04143881797790527, 0.2863280773162842, 1.0971922874450684, 6.1295459270477295]


plt.plot(lst_sizes, time_lu)
plt.show()


plt.plot(lst_sizes, time_qr)
plt.show()