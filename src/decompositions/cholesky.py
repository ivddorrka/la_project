from matrx_generation import *
import matplotlib.pyplot as plt

def cholesky_decomposition_numpy(A):
    L = scipy.linalg.cholesky(A, lower=True)
    U = scipy.linalg.cholesky(A, lower=False)
    return L, U


def cholesky_decomposition_algo(matrix, n):

    lower = [[0 for x in range(n)]
                for y in range(n)];
    upper = [[0 for x in range(n)]
                for y in range(n)];

    for i in range(n):
        for j in range(i + 1):
            sum1 = 0;
 
            if (j == i):
                for k in range(j):
                    sum1 += pow(lower[j][k], 2);
                if(j != n):
                    lower[j][j] = (math.sqrt(matrix[j][j] - sum1));
                    upper[j][j] = lower[j][j]
            else:

                for k in range(j):
                    sum1 += (lower[i][k] *lower[j][k]);
                if(lower[j][j] > 0):
                    if(j != n):
                        lower[i][j] = ((matrix[i][j] - sum1) /
                                                lower[j][j]);
                        upper[j][i] = lower[i][j]                           

    return lower, upper



def cholesky_decomposition_algo2(A):
    
    n = len(A)

    L = [[0.0] * n for i in range(n)]

    for i in range(n):
        for k in range(i+1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))
            
            if (i == k): 
                L[i][k] = math.sqrt(A[i][i] - tmp_sum)
            else:
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
    return L


# n = 1000;
# matrix = generate_hermitian(n)


# start = time.time()
# res = cholesky_decomposition_algo(matrix, n)
# end = time.time()
# print(end-start)

# start = time.time()
# res_nmp = cholesky_decomposition_numpy(matrix)
# end = time.time()
# print(end-start)


# start = time.time()
# res_nmp = cholesky_decomposition_algo2(matrix)
# end = time.time()
# print(end-start)



lst_sizes = []

lst_times_nmp = []
lst_times_algo = []
lst_times_algo2 = []
i =2

while i <= 1025:
    n = i
    matrix = generate_hermitian(n)
    print(matrix)
    start = time.time()
    res_nmp = cholesky_decomposition_numpy(matrix)
    end = time.time()

    result_nmp = end-start
    lst_times_nmp.append(result_nmp)

    start1 = time.time()
    res_algo = cholesky_decomposition_algo(matrix, n)
    end1 = time.time()

    result_algo = end1-start1
    lst_times_algo.append(result_algo)

    start2 = time.time()
    res_algo2 = cholesky_decomposition_algo2(matrix)
    end2 = time.time()

    result_algo2 = end2-start2
    lst_times_algo2.append(result_algo2)

    lst_sizes.append(n)
    print(f"Finished iteration {i}")
    i = i * 2

plt.plot(lst_sizes, lst_times_nmp)
plt.show()
plt.plot(lst_sizes, lst_times_algo)
plt.show()
plt.plot(lst_sizes, lst_times_algo2)
plt.show()
