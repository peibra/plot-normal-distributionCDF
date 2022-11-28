from matplotlib import pyplot as plt
import numpy as np


def get_gauss_taylor_coeff(n):
    diff = [i for i in range(1, n+1)]
    negative1 = [-1 for _ in range(1, n+1)]
    D = np.diag(diff, k=1)
    N1 = np.diag(negative1, k=-1)
    A = D + N1

    coeff = [0] * (n+1)
    for i in range(n+1):
        coeff[i] = np.linalg.matrix_power(A, i)[0, 0]

    return coeff


def normal_distributionCDF(x, n):
    coeff = get_gauss_taylor_coeff(n)
    const = 1 / np.sqrt(2*np.pi)
    y = 0.5
    for k, c in enumerate(coeff):
        y = y + const * c * x**(k+1) / np.math.factorial(k+1)
    return y
