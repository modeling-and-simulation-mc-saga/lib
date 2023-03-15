import matplotlib.pyplot as plt
import re
from typing import Callable
from collections import namedtuple

def pltInit():
    """
    Setting fonts 
    """
    plt.rcParams['font.size']=28
    plt.rcParams['font.family']='Times New Roman'
    plt.rcParams['mathtext.fontset']='cm'
    plt.rcParams['mathtext.default']='it'

#Defining simple named tuple for keeping 2 dimensional coordinate
Point = namedtuple('Point',('x','y'))

class DataFile:
    """
    Class for reading data text file
    All lines contain data separating by spaces
    Comment lines start by "#"
    """
    def __init__(self, filename:str):
        with open(filename, 'r') as f:
            self.__lines = f.read().splitlines()

    def readData(self, x=0, y=1) -> tuple[list[float],list[float]]:
        """
        extracting data
        
        Parameters
        ------
        x: data for horizontal axis
        y: data for vertical axis
        """
        xList=[]
        yList=[]
        for l in self.__lines:
            if len(l)>0 and l[0] != '#':
                d = l.split()
                xList.append(float(d[x]))
                yList.append(float(d[y]))
        return xList, yList

    def readDataM(self, x=0, y=1) -> tuple[list[list[float]],list[list[float]]]:
        """
        extracting data
        data are separated by null lines
        """
        xListM=[]
        yListM=[]
        xList=[]
        yList=[]
        for l in self.__lines:
            if len(l)==0:
                xListM.append(xList)
                xList=[]
                yListM.append(yList)
                yList=[]
            elif l[0] != '#':
                d = l.split()
                xList.append(float(d[x]))
                yList.append(float(d[y]))
        xListM.append(xList)
        yListM.append(yList)
        return xListM, yListM    

    def getParam(self,label:str) -> float:
        """
        getting parameters from comment lines

        Parameters
        ------
        label: name of parameter
        """
        pattern = '#\s*'+label+'\s*:\s*([0-9\.]*)'
        for l in self.__lines:
            if len(l)>0 and l[0] == '#':
                res = re.search(pattern,l)
                if res != None:
                    r = float(res.group(1))
                    return r
        return None