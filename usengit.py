from __future__ import print_function
import ngit
import os 
import sys
import pprint

f = open("a.txt", "r")
a = []
for line in f:
	b = []
	b.append(int(line.split()[0]))
	b.append(int(line.split()[1]))
	b.append(line.split()[2])
	a.append(b)
	
#print(a)

myTree = ngit.intervalTree(a, 0, 1, 1679, 1998)
myTree.pprint(6)
r = [1800, 1900]
print(myTree.findRange(r))
