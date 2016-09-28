from __future__ import print_function
import os
import sys
import pprint

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
    def __init__(self, data, start, end):
        self.start = start
        self.end = end
        
        self.intervals = self.getintervals(data)
        self.root = self.buildtree(self.intervals)
        self.insertdata(self.root, data, start, end)
        
    def getintervals(self, data):
        #collect all endpoints and sort them to get list of elementary intervals
        intervallist = []
        for x in data:
            intervallist.extend([x[0], x[1]])
        intervallist = list(set(intervallist))
        intervallist.sort()
        return intervallist
    
    def ptininterval(self, pt, interval):
        if(pt>=interval[0] and pt<=interval[1]):
            return 1
        return 0

    def spanininterval(self, nodespan, labelinterval):
        if self.ptininterval(nodespan[0], labelinterval) and self.ptininterval(nodespan[1], labelinterval):
            return 1
        return 0

    def isoverlap(self, nodespan, labelinterval):
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
                    node.appenddata(label)
            
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

    def inorder(self, rootnode):
        '''
        inorder traversal of the 
        '''
        if(rootnode is None):
            return
        self.inorder(rootnode.l)
        print(rootnode.val, rootnode.data)
        self.inorder(rootnode.r)
        
    def traverse(self):
        self.inorder(self.root)
