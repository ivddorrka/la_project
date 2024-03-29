from matrx_generation import *
# https://gist.github.com/Hsankesara/cd35edb30825df19f182a6ecf96e126e implementation


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


# A = scipy.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]])  # From the Wikipedia Article on QR Decomposition
A = generate_random_matrix(3, 3)
res = obtain_QR(A, 3, 3)
print(res[0])
print(res[1])

