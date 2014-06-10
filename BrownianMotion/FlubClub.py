import numpy as np
from StringIO import StringIO
import matplotlib.pyplot as plt
import requests
import glob, os
from PIL import Image, ImageOps

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
        return "From str method of Blob: loc is %s, \n mass is %s \n com is: %s" % (self.loc, self._mass, self.centerOfMass)
        
    def add(self, (i, j)):
        """
        Add a pixel (i, j) to the flubber as part of the drawing process.
        """
        self.loc.append((i, j));
        self._mass = (len(self.loc))
        
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
        self.dist = round(((self.centerOfMass()[0] - duece.centerOfMass()[0])**2 + \
                     (self.centerOfMass()[1] - duece.centerOfMass()[1])**2)**.5, 4)
        return self.dist
        
    def centerOfMass(self):
        """
        Return tuple of (x,y) values for this flubber's center of mass.
        Format center-of-mass coordinates with 4 sig figs.
        """
        x = 0; y = 0;
        for point in self.loc:
            x += point[0]
            y += point[1]
        return (x / len(self.loc), y / len(self.loc))

        
def flubberFinder(P, picture, tau):
    '''find all flubbers in the picture using the luminance threshold tau.'''
    BLACK = (0, 0, 0); WHITE = (255, 255, 255); RED = (255, 0, 0);  float(tau);
    FlubArray = [] 
    
    tempImage = picture.load()
    horLen, verLen = picture.size
    monochrome(picture, tau)    
    
    for x in range(horLen):
        for y in range(verLen):
            if tempImage[x, y] == BLACK:
                FlubArray.append(fill(picture, horLen, verLen, x, y))
    
    return FlubArray

def monochrome(picture, tau):
    '''Reads and loads a temporary image to convert to black or white in regards to luminance threshold tau. '''
    BLACK = (0, 0, 0); WHITE = (255, 255, 255); tempImage = picture.load(); horLen, verLen = picture.size;
        
    for x in range(horLen):
        for y in range(verLen):
            r,g,b = tempImage[x, y]
            if r+g+b >= tau:
                tempImage[x,y] = BLACK
            else:
                tempImage[x,y] = WHITE

def fill(picture, horLen, verLen, xi, yi):  #Using Fastfill algorithm.
    '''Lists all the pixels that are associated with currentFlubber that haven't been filled or looked at.'''
    BLACK = (0, 0, 0); 
    RED = (255, 0, 0); 
    img = picture.load();
    queue = [(xi, yi)];
    if img[xi, yi] == BLACK: #If pixel is black--track covered by changing to red.
        img[xi, yi] = RED
        Flubber = Blob();
        while queue:
            x, y, queue = queue[0][0], queue[0][1], queue[1:]
            # Horizontal/Vertical Postive/Negative Displacement
            Flubber.add((x, y)) # Add this pixel to the current flubber array.
            if x > 0 and (img[x - 1, y] == BLACK): # "and" is from FastFill algorithm.
                img[x - 1, y] = RED
                queue.append((x - 1, y))
            if x < (horLen - 1) and (img[x + 1, y] == BLACK):
                img[x + 1, y] = RED
                queue.append((x + 1, y))
            if y > 0 and (img[x, y - 1] == BLACK):
                img[x, y - 1] = RED
                queue.append((x, y - 1))
            if y < (verLen - 1) and (img[x, y + 1] == BLACK):
                img[x, y + 1] = RED
                queue.append((x, y + 1))
    #print str(Flubber)
    return Flubber
    
# Determines mass of all flubber by >= p pixels
def qualityFlubbers(P, listFlubbers): #getBeads(P) Function
    '''
    return all unit flubbers with >= P pixels. 
    '''
    tempListFlubbers = [] 
    #print dir(listFlubbers), str(listFlubbers.loc), str(listFlubbers._mass)
    for i in listFlubbers:
        if i._mass >= P:
            tempListFlubbers.append(i)
           #print i._mass
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