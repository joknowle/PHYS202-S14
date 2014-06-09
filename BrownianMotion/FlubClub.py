import numpy as np
from StringIO import StringIO
import matplotlib.pyplot as plt
import requests
import glob, os
from PIL import Image

class Blob():
    def __init__(self):
        """
        Construct an empty flubber array for the purpose of filling 
        it with information determined by other functions.
        """
        self.loc = [] # Stores the number of pixels; AKA mass or size of flubber.
        self._mass = 0
    def __repr__(self):
        return "<loc:%s mass:%s>" % (self.loc, self._mass)
    
    def __str__(self):
        return "From str method of Blob: loc is %s, mass is %s" % (self.loc, self._mass)
        
    def add(self, i, j):
        """
        Add a pixel (i, j) to the flubber as part of the drawing process.
        """
        print "Add",i,j
        (self__init__().loc).append((i, j))
        self.mass = (len(self.loc))
        
    def mass(self):
        """
        Return number of pixels added equal to its mass.
        """
        self._mass = (len(self.loc))
        return self._mass
    def distanceTo(self, duece):
        """
        Return distance between the center of mass of this flubber and another.
        """
        dist = round(((self.centerOfMass()[0] - duece.centerOfMass()[0])**2 + \
                     (self.centerOfMass()[1] - duece.centerOfMass()[1])**2)**.5, 4)
        return dist
        
    def centerOfMass(self):
        """
        Return tuple of (x,y) values for this flubber's center of mass.
        Format center-of-mass coordinates with 4 sig figs.
        """
        xLocs = 0; yLocs = 0;
        for loc in self.loc:
            xLocs += loc[0]; yLocs += loc[1];
            
        # Average of total stored in array:
        xAvg = round(xLocs / len(self.loc), 4); yAvg = round(yLocs / len(self.loc), 4);
        self.centerOfMass = [xAvg, yAvg];
        return self.centerOfMass

        
def flubberFinder(P, picture, tau):
    '''find all flubbers in the picture using the luminance threshold tau.'''
    BLACK = (0, 0, 0); WHITE = (255, 255, 255); 
    FlubArray = [] 
    
    tempImage = picture.load()
    horLen, verLen = picture.size
    monochrome(picture, tau)    
    
    for x in range(horLen):
        for y in range(verLen):
            if tempImage[x, y] == BLACK:
                #Flubber = Blob();
                #fill(picture, horLen, verLen, x, y, Flubber)
                FlubArray.append(fill(picture, horLen, verLen, x, y))
                #print str(Flubber.loc), str(Flubber.mass)
    return FlubArray

def monochrome(picture, tau):
    '''Reads and loads a temporary image to convert to black or white in regards to luminance threshold tau. '''
    BLACK = (0, 0, 0); WHITE = (255, 255, 255); i = []; tempImage = picture.load(); horLen, verLen = picture.size;
        
    for x in range(horLen):
        for y in range(verLen):
            r, g, b = tempImage[x, y]
            if r + g + b >= tau:
                tempImage[x, y] = BLACK
            else:
                tempImage[x,y] = WHITE
    
#def count(P, picture, tau, Flubber, fM, fCOM):
#    '''Scan image from top left, to bottom right using nested loops. 
#    Black pixels are counted and fill function is called to create a circular representation of a flubber.
#    This is done by recognizing same-state pixels near it.
#    Once neighboring pixels are determined, they are assigned to the current flubber array.'''
#    BLACK = (0, 0, 0); RED = (255, 0, 0); tempImage = picture.load(); 
#    horLen, verLen = picture.size; flubberCount = 0; flubberMassInfo = [];
#    for x in range(horLen):
#        for y in range(verLen):
#            if tempImage[x,y] == BLACK:
#                
#                fill(tempImage, horLen, verLen, x, y, Flubber)
#                Flubber.mass()
#                Flubber.centerOfMass
#                #print str(Flubber.loc), str(Flubber.mass) #, Flubber.centerOfMass
#                flubberMassInfo.append(Flubber)
#    qualFlubbers = qualityFlubbers(P, flubberMassInfo)
#    flubberCount = numFlubber(P, qualFlubbers)
#
#    return flubberCount, qualFlubbers, flubberMassInfo

def fill(picture, horLen, verLen, xi, yi):  #Using Fastfill algorithm.
    '''Lists all the pixels that are associated with currentFlubber that haven't been filled or looked at.'''
    BLACK = (0, 0, 0); RED = (255, 0, 0); queue = [(xi, yi)];
    img = picture.load()
    Flubber = Blob()
    while queue:
        x, y, queue = queue[0][0], queue[0][1], queue[1:]
        # Horizontal/Vertical Postive/Negative Displacement
        HPD = x + 1; HND = x - 1; VPD = y + 1; VND = y - 1;
        if img[x, y] == BLACK: #If pixel is black--track covered by changing to red.
            img[x, y] = RED
            print "ADDING TO FLUBBER"
            Flubber.add(x, y) # Add this pixel to the current flubber array.
            print str(Flubber)
            if x > 0 and img[HND, y] == BLACK: # "and" is from FastFill algorithm.
                img[HND, y] = RED
                queue.append((HND, y))

            if x < (horLen - 1) and img[HPD, y] == BLACK:
                img[HPD, y] = RED
                queue.append((HPD, y))

            if y > 0 and img[x, VND] == BLACK:
                img[x, VND] = RED
                queue.append((x, VND))

            if y < (verLen - 1) and img[x, VPD] == BLACK:
                img[x, VPD] = RED
                queue.append((x, VPD))
    #Flubber.mass
    return Flubber



# Determines mass of all flubber by >= p pixels
def qualityFlubbers(P, listFlubbers): #getBeads(P) Function
    '''
    return all unit flubbers with >= P pixels. 
    '''
    tempListFlubbers = [] 
    print dir(listFlubbers), str(listFlubbers.loc), str(listFlubbers._mass)
    for i in listFlubbers:
        if i._mass >= P:
            tempListFlubbers.append(i)
    return tempListFlubbers

def numFlubber(P, listFlubbers): #getBeads(P) Function (number of quality beads)
    '''
    return all unit flubbers with >= P pixels. 
    '''
    count = 0;
    for i in listFlubbers:
        if i._mass >= P:
            count += 1
    return count