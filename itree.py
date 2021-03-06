from __future__ import print_function
import os
import sys
import pprint
from collections import defaultdict

'''
With ideas taken from Wikipedia, StackOverflow and NextGenetics blog
'''

class node:
    leaves = 0
    def __init__(self, val, left, right):
        self.data = []
        self.val = val
        if(self.val == -1 or self.val == -2):
            node.leaves += 1
            self.val = val - node.leaves
        self.l = left
        self.r = right

    def appenddata(self, data):
        self.data.append(data)

class itree:
    '''
    Input parameter data will be a list of lists, of the form 
    [[start, end, label], [start, end,label],......]
    '''
    def __init__(self, data):
        self.intervals = self.getintervals(data)
        self.start = 0
        self.end = self.intervals[-1]
        self.root = self.buildtree(self.intervals)
        self.insertdata(self.root, data, self.start, self.end)
        
    def getintervals(self, data):
        #collect all endpoints and sort them to get list of elementary intervals
        intervallist = []
        for x in data:
            intervallist.extend([x[0], x[1]])
        intervallist = list(set(intervallist))
        intervallist.sort()
        return intervallist
    
    def ptininterval(self, pt, interval):
        #Check if a point is within a given interval
        if(pt>=interval[0] and pt<=interval[1]):
            return 1
        return 0

    def spanininterval(self, nodespan, labelinterval):
        #Check whether the span of a tree node is fully contained within an interval
        if self.ptininterval(nodespan[0], labelinterval) and self.ptininterval(nodespan[1], labelinterval):
            return 1
        return 0

    def isoverlap(self, nodespan, labelinterval):
        #Check if two intervals overlap
        if self.ptininterval(nodespan[0], labelinterval) or self.ptininterval(nodespan[1], labelinterval) or self.ptininterval(labelinterval[0], nodespan) or self.ptininterval(labelinterval[1], nodespan):            
            return 1
        return 0
    
    def _insertdata(self, node, labelinterval,label, start, end):
        if (node is not None):
            leftspan = (start, node.val)
            rightspan = (node.val, end)
            
            #if leftspan is completely contained in the interval spanned by the label
            #store label in left child of node
            if(self.spanininterval(leftspan, labelinterval)):
                    node.l.appenddata(label)
            
            #if the two intervals overlap, then recurse lower down the tree
            elif (self.isoverlap(leftspan, labelinterval)):
                 self._insertdata(node.l, labelinterval, label, start, node.val)

            if(self.spanininterval(rightspan, labelinterval)):
                    node.r.appenddata(label)
            elif (self.isoverlap(rightspan, labelinterval)):
                self._insertdata(node.r, labelinterval, label, node.val, end)


    def insertdata(self, node, data, start, end):
        """
        loop through data and store in the tree 
        Algo: Move down both the left and right subtree till you find a node whose span is contained within the interval
        """
        for item in data:
            iteminterval = [item[0], item[1]]
            itemlabel = str(item[-1])
            self._insertdata(node, iteminterval, itemlabel, start, end)

    def buildtree(self, intervals):
        '''
        Gets a sorted list of intervals and builds a BST out of that
        '''
        mid = len(intervals)//2
        left = intervals[:mid]
        right = intervals[mid+1:]
        midval = intervals[mid]

        n = node(midval, node(-1, None, None), node(-1, None, None))
        if(len(left)>1):
            n.l = self.buildtree(left)
        elif len(left)==1:
            n.l = node(left[0], node(-1, None, None), node(-1, None, None))
    
        if(len(right)>1):
            n.r = self.buildtree(right)
        elif(len(right)==1):
            n.r = node(right[0], node(-1, None, None), node(-1, None, None))
        return n
    
    def _findrange(self, node, start, end, queryrange):
        #Return all nodes overlapping with a query interval
        if(queryrange[0]<self.start or queryrange[1]>self.end):
            print("Interval out of range")
            return

        overlaps = []
        if(node is None):
            return overlaps

        leftspan = (start, node.val)
        rightspan = (node.val, end)

        if(self.isoverlap(leftspan, queryrange)):
            overlaps.extend(node.data)
            if(node.l is not None):
                overlaps.extend(self._findrange(node.l, start, node.val, queryrange))

        if(self.isoverlap(rightspan, queryrange)):
            overlaps.extend(node.data)
            if(node.r is not None):
                overlaps.extend(self._findrange(node.r, node.val, end, queryrange))

        return list(set(overlaps))


    def findrange(self, querystart, queryend):
        #Return all nodes overlapping with a query interval. Calls _findrange function.
        overlaps = self._findrange(self.root, self.start, self.end, [querystart, queryend])
        return overlaps

    def composeroverlap(self, composer, data):
        #Can delete this function, never gets used
        overlaps = self._findrange(self.root, self.start, self.end, [data[0], data[1]])
        return overlaps

    def overlapsize(self, area1, area2):
        return(min(area1[1], area2[1]) - max(area1[0], area2[0]))


    def maximaloverlap(self, querystart, queryend, data):
        overlaps = self._findrange(self.root, self.start, self.end, [querystart, queryend])
        datadict = {}
        overlapdict = {}
        for row in data:
            datadict[row[2]] = [row[0], row[1]]
        for composer in overlaps:
            clife = [datadict[composer][0], datadict[composer][1]]
            querysize = [querystart, queryend]
            overlapdict[composer] = self.overlapsize(clife, querysize)
        sortedoverlaps = sorted(overlapdict, key = overlapdict.get, reverse = True)
        print("Composer with maximal overlap with the interval: ",sortedoverlaps[0], overlapdict[sortedoverlaps[0]])
        
    def inorder(self, rootnode):
        '''
        Inorder traversal of the interval tree
        '''
        if(rootnode is None):
            return
        self.inorder(rootnode.l)
        print(rootnode.val, rootnode.data)
        self.inorder(rootnode.r)
    

    def findsongs(self,querystart, queryend, composers):
        overlaps = self._findrange(self.root, self.start, self.end, [querystart, queryend])
        datadict = {}
        for row in composers:
            row = [i.replace('N.A.', '') for i in row]
            datadict[row[1]] = [row[3], row[4], row[5], row[6]]
        
        songs = [datadict[x] for x in overlaps]
        print("Genre: Songs")
        for i in range(0, 4):
            print(i+1, ": ",[s[i] for s in songs])


    def traverse(self):
        #Print intervals in sorted order
        self.inorder(self.root)
