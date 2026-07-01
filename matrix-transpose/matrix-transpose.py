import numpy as np

def matrix_transpose(a):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A=np.array(a)
    B=np.empty((A.shape[1],A.shape[0]), dtype=int)
    i=0
    while i<A.shape[0]:
        j=0
        while j<A.shape[1]:
            B[j][i]=A[i][j]
            j+=1
        i+=1
    return B
    pass
