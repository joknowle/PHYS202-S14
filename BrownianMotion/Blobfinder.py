import numpy as np
from PIL import Image
from StringIO import StringIO
class Blob():
    def __init__():
        """
        Construct an empty blob.
        """
        return None

    def add(i,j):
        """
        Add a pixel (i, j) to the blob.
        """
        return None

    def mass():
        """
        Return number of pixels added equal to its mass.
        """
        return None

    def distanceTo(blob):
        """
        Return distance between the center of mass of this blob and b
        """
        return None

    def centerOfMass():
        """
        Return tuple of (x,y) values for this blob's center of mass.
        Format center-of-mass coordinates with 4 sig figs.
        """
        return None

def BlobFinder(picture, tau):
    '''
    find all blobs in the picture using the luminance threshold tau
    '''
    black = (0, 0, 0)
    white = (255, 255, 255)
    xsize, ysize = picture.size
    temp = picture.load()
    for x in range(xsize):
        for y in range(ysize):
            r,g,b = temp[x,y]
            if r+g+b >= tau: 
                temp[x,y] = black
            else:
                temp[x,y] = white
    return None

def countBeads(P):
    '''
    return the number of beads with >= P pixels
    '''

def getBeads(P):
    '''
    return all beads with >= P pixels
    '''
if __name__ == "__main__":
    p = 25
    tau = 600
    print tau, p
    # pictureObject = # call from drive.
    # BlobFinder(pictureObject, tau)