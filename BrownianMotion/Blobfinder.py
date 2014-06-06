import numpy as np
from PIL import Image
from StringIO import StringIO
import requests

class Blob():
    def __init__():
        """
        Construct an empty flubber array for the purpose of filling 
        it with information in other functions.
        """
        self.flubber = []
        self.mass = 0
        
    def add(self, i, j):
        """
        Add a pixel (i, j) to the flubber.
        """
        self.flubber.append((i,j));
        
    def mass(self):
        """
        Return number of pixels added equal to its mass.
        """
        self.append(len(self.flubber))
        
    def distanceTo(self, comFirst, comSecond):
        """
        Return distance between the center of mass of this flubber and b
        """
        #
        pX1 = comFirst[0]; pX2 = comFirst[1]; pY1 = comSecond[0]; pY2 = comSecond[1]; 
        self.dist = round(np.sqrt((pX2 - pX1)**2. + (pY2 - pY1)**2.), 4)
        return self.dist
    
    def centerOfMass(self):
        """
        Return tuple of (x,y) values for this flubber's center of mass.
        Format center-of-mass coordinates with 4 sig figs.
        """
        xLocs = 0; yLocs = 0;
        for loc in self.flubber:
            xLocs += loc[0]; yLocs += loc[1];
            
        # Average of total stored in array:
        xAvg = round(xLocs, 4) / len(self.flubber); yAvg = round(yLocs, 4)/ len(self.flubber);
        self.centerOfMass = [xAvg, yAvg]; Avg = [xAvg, yAvg];
        return Avg
    
    
def count(picture, inc, listFlubbers):
    """scan the image top to bottom and left to right using a nested loop.
    when black pixel is found, increment the count, create a new blob, then call the fill
    function to fill in all the pixels connected to that one. Put the pixels into the blob in the fill function."""
    BLACK = (0, 0, 0); RED = (255, 0, 0); tempImage = picture.load(); horLen, verLen = picture.size;
    for x in xrange(horLen):
        for y in xrange(verLen):
            if tempImage[x,y] == BLACK:
                redFlubbers = Blob()
                fill(tempImage, horLen, verLen, x, y, redFlubbers)
                redFlubbers.mass()
                redFlubbers.centerOfMass()
                listFlubbers.append(redFlubbers)
                inc += 1
    return listFlubbers


def flubberFinder(P, picture, tau):
    '''find all flubbers in the picture using the luminance threshold tau.'''
    Flubbers = []
    # Need to handle filter color information in images:
    monochrome(picture, tau)
    listFlubbers = sortImage(picture, mask, Flubbers)
    return listFlubbers

def flubberGTEPixel(P, listFlubbers):
    '''
    return all unit flubbers with >= P pixels. 
    '''
    tempListFlubbers = []
    for i in listFlubbers: 
        if i.mass >= 25.0000:
            tempListFlubbers.append(i)
    return tempListFlubbers
    
def monochrome(picture, tau):
    """ Reads and loads a temporary image to convert to black or white in regards to luminance threshold tau. """
    BLACK = (0, 0, 0); WHITE = (255, 255, 255); horLen, verLen = picture.size; tempImage = picture.load();
    for x in xrange(horLen):
        for y in xrange(verLen):
            r, g, b = tempImage[x, y]
            if r + g + b >= tau: 
                tempImage[x, y] = BLACK
            else:
                tempImage[x,y] = WHITE
    #return tempImage

def fill(picture, horLen, verLen, xi, yi, currentFlubber):
    """keep a list of pixels that need to be looked at, but haven't 
    yet been filled in - a list of the (x,y) coordinates of pixels that 
    are neighbors of ones we have already examined.  Keep looping until 
    there's nothing left in this list"""
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    queue = [(xi, yi)]
    while queue:
        x, y, queue = queue[0][0], queue[0][1], queue[1:]
        if picture[x, y] == BLACK:
            picture[x, y] = RED
            #adds red points to the blob in question
            currentFlubber.add(x, y)
            if x > 0:
                queue.append((x - 1, y))
            if x < (horLen - 1):
                queue.append((x + 1, y))
            if y > 0:
                queue.append((x, y - 1))
            if y < (verLen - 1):
                queue.append((x, y + 1))
    
#if __name__ == "__main__":
#    p = 25
#    tau = 600
#    print tau, p
    # pictureObject = # call from drive.
    # BlobFinder(pictureObject, tau)