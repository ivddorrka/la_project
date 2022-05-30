import numpy as np

def simplex_matrix_method(A,b, c):
    '''
    Solve simplex linear problem using matrix method

    source: https://towardsdatascience.com/developing-the-simplex-method-with-numpy-and-matrix-operations-16321fd82c85
    '''

    size = A.shape[0]
    num_vars = A.shape[1] - size

    var_coeff = [i for i in range(0, len(c))]

    base_vars = np.array(c[num_vars:])
    non_base_vars = np.array(c[:num_vars])


    while True:
        base_indx = var_coeff[num_vars:]
        non_base_indx = var_coeff[:num_vars]

        basis_matrix = A[:, base_indx]
        b_inv = np.linalg.inv(basis_matrix)

        non_basis_matrix = A[:, non_base_indx]

        basis_vars = b_inv @ b
        y_t = base_vars @ b_inv

        non_basis_hat = non_base_vars - (y_t @ non_basis_matrix)

        min_indx = np.argmin(non_basis_hat)

        if (all(i >= 0 for i in non_basis_hat)):
            return base_vars, base_indx, non_base_vars, non_base_indx, basis_vars, non_basis_hat
        

        indx = var_coeff[min_indx]

        a_hat = b_inv @ A[:, indx]


        ratios = []

        for i in range(0, len(basis_vars)):
            a_value = a_hat[i]
            b_value = basis_vars[i]

            if (a_value <= 0):
                ratios.append(10000000)
                continue
            ratios.append(b_value/a_value)
        

        rat_min_indx = np.argmin(ratios)

        non_base_vars[min_indx], base_vars[rat_min_indx] = base_vars[rat_min_indx], non_base_vars[min_indx]

        var_coeff[min_indx], var_coeff[rat_min_indx + num_vars] = var_coeff[rat_min_indx + num_vars], var_coeff[min_indx]


# another example test
A = np.array([[1, 1, 1, 1, 0, 0],
            [-1, 2, -2, 0, 1, 0],
            [2, 1, 0, 0, 0, 1]])

b = np.array([4, 6, 5])
c = np.array([-1, -2, 1, 0, 0, 0])

print(simplex_matrix_method(A, b, c))
