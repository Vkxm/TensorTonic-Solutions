import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    X=np.array(x)
    Y=np.array(y)
    Z=(X-Y)**2
    return (Z.sum())**0.5
    pass