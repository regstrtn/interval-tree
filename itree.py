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
                
        if(self.root is None):
            self.root = node(midval, None, None)
            self.buildtree(left, self.root.l)
            self.buildtree(right, self.root.r)
        else:
            tnode = node(midval, None, None)

            if(len(left)>1):
                self.buildtree(left, tnode.l)
            elif len(left)==1:
                tnode.l = node(left[0], None, None)
        
            if(len(right)>1):
                self.buildtree(right, tnode.r)
            elif(len(right)==1):
                tnode.r = node(right[0], None, None)
    
    def add(self, intervals):
        mid = len(intervals)//2
        
        if(self.root == None):
            self.root = node(midval, None, None)
        else:
            self._add(intervals, self.root)

    def _add(self, intervals, node):
        mid = len(intervals)//2
        left = intervals[:mid]
        right = intervals[mid+1:]
        midval = intervals[mid]
        

        if(len(left)>1):
            if(node.l != None):
                self._add(left, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def inorder(self, rootnode):
        '''
        inorder traversal of the 
        '''
        if(rootnode is None):
            return
        self.inorder(rootnode.l)
        print(rootnode.val)
        self.inorder(rootnode.r)
        
    def traverse(self):
        self.inorder(self.root)
