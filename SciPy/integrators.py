import numpy as np

def trapz(func, a, b, N):
    """
    A technique for approximating the definite integral using straight line segments.
    The trapezoidal rule works by approximating the region under the graph of 
    the function f(x) as a trapezoid and calculating its area. 
    """
    h = (b - a)/float(N) # width of each slice
    k = np.arange(1,N)
    I =  h*(0.5*func(a) + 0.5*func(b) + func(a+k*h).sum())
    return I

def simps(func, a, b, N):
    """
    A numerical approximation of definite integrals using quadratic polynomials.
    Parabolic arcs are used instead of the straight line segments that 
    the trapezoidal rule uses. 
    """
    h = (b-a)/float(N)
    k1 = np.arange(1,N/2+1)
    k2 = np.arange(1,N/2)
    
    I = (1./3.)*h*(func(a) + func(b) + 4.*func(a+(2*k1-1)*h).sum() \
                   + 2.*func(a+2*k2*h).sum())
    return I