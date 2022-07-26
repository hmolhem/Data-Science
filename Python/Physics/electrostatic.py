import numpy as np
import constant as cte

def vector_norm_direction(x):
    n = np.linalg.norm(x)
    u = x/n
    return n, u


def vx2y(x1, x2):
    d = x1 - x2
    n, u = vector_norm_direction(d)
    return d, n, u

def coulombLaw(q1, q2, s, u):
    F = cte.K*q1*q2*u/(s**2)
    return vector_norm_direction(F)
