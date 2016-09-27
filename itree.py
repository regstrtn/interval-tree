from __future__ import print_function
import os
import sys
import pprint

class node:
    def __init__(self, val, left, right):
        self.data = []
        self.val = val
        self.l = left
        self.r = right
    def appenddata(self, data):
        self.data.extend(data)

class itree:
    def __init__(self, data, start, end):
        self.start = start
        self.end = end
        self.root = None
       
        self.intervals = self.getintervals(data)
        self.buildtree(self.intervals, self.root)
        
    def getintervals(self, data):
        intervallist = []
        for x in data:
            intervallist.extend([x[0], x[1]])
        intervallist = list(set(intervallist))
        intervallist.sort()
        return intervallist
        
    def buildtree(self, intervals, tnode):
        '''
        Gets a sorted list of intervals and builds a BST out of that
        '''
        mid = len(intervals)//2
        left = intervals[:mid]
        right = intervals[mid+1:]
        midval = intervals[mid]
        
        tnode = node(midval, None, None)
        
        if(len(left)>1):
            self.buildtree(left, tnode.l)
        elif len(left)==1:
            tnode.l = node(left[0], None, None)
        
        if(len(right)>1):
            self.buildtree(right, tnode.r)
        elif(len(right)==1):
            tnode.r = node(right[0], None, None)
        
        if(self.root is None):
            self.root = tnode
            self.root.l = tnode.l
            self.root.r = tnode.r
    
    def inorder(self, node):
        if(node is None):
            return
        self.inorder(node.l)
        print(node.val)
        self.inorder(node.r)
        
    def traverse(self):
        self.inorder(self.root)
