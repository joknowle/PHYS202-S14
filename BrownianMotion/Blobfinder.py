import numpy as np
from PIL import Image
import requests
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
    return None


def countBeads(P):
    '''
    return the number of beads with >= P pixels
    '''

def getBeads(P):
    '''
    return all beads with >= P pixels
    '''