import numpy as np
def pointPotential(x,y,q,Xc,Yc):
    """
    return the electric potential for a point charge q at (Xc,Yc)
    Units are [Volts] if input is [meters][Coulombs]
    """
    k = 8.987551787997912e9 #(Nm^2/C^2)                                                                        
    Vxy = k*q/np.sqrt(((x-Xc)**2 + (y-Yc)**2))
    return Vxy
def dipolePotential(x,y,q,d):
    """
    Return electric potential for pair of point charges -/+ q
    separated by distance d along x axis with center (0,0)
    Units are [Volts] if inputs are [meters][Coulombs]
    """
    Vxy = pointPotential(x,y,q,-d/2.,0.) + pointPotential(x,y,-q, +d/2.,0.)
    return Vxy