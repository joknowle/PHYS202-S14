import numpy as np

def twoPtForwardDiff(x,y):
    """
    Function performs differentiation of two floating values.
    array y is reshaped to accomodate dy/dx calculation.
    index 0 through and including the second to last element are calculated
    separately from the last index, so there are no ValueErrors.
    dy/dx is returned.
    """
    dydx = np.zeros(y.shape, float)
    dydx[0:-1] = np.diff(y)/np.diff(x)
    dydx[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])
    return dydx


def twoPtCenteredDiff(x,y):
    """
    Function performs differentiation of two floating values.
    array y is reshaped to accomodate dy/dx calculation.
    Function values are stored in new array by three cases:
    0th index, nth index, and center values.
    0th index uses forward differentiation,
    nth index uses backwards differentiation,
    Center difference is normal delta y / delta x.
    dy/dx is returned.
    """
    
    dydx = np.zeros(y.shape,float)
    dydx[1:-1] = (y[2:] - y[:-2]) / (x[2:] - x[:-2]) # Center difference.
    dydx[0] = (y[1] - y[0]) / (x[1] - x[0]) # Forward difference.
    dydx[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2]) #Backward difference.
    
    return dydx

def fourPtCenteredDiff(x,y):

    """
    Function performs differentiation of two floating values.
    array y is reshaped to accomodate dy/dx calculation.
    Function values are stored in new array by three cases:
    0th index, nth index, and center values.
    0th index uses forward differentiation,
    nth index uses backwards differentiation,
    Center difference is normal delta y / delta x.
    dy/dx is returned.
    """
    dydx = np.zeros(y.shape,float)
    # Center difference.
    dydx[2:-2] = (y[0:-4] - 8*y[1:-3] + \
                  8*y[3:-1] - y[4:]) / (12*x[1:2])

    dydx[0] = (y[1] - y[0]) / (x[1] - x[0]) # Forward difference.
    dydx[1] = (y[2] - y[1]) / (x[2] - x[1]) 
    
    dydx[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2]) #Backward difference.
    dydx[-2] = (y[-2] - y[-3]) / (x[-2] - x[-3])
    return dydx