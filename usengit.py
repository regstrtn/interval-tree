from __future__ import print_function
import itree
import os 
import sys
import pprint
import pgraph
import csv


fbcsv = open("b.csv", "r")

composers = csv.reader(fbcsv, delimiter = ",", quotechar = '"')
data = []

for row in composers:
	life = []
	#print(row[2].split("-")[1])
	life.append(int(row[2].split("-")[0]))
	life.append(int(row[2].split("-")[1]))
	life.append(row[1])
	data.append(life)

print(data)

a = data
#print(a)
mytree = itree.itree(a, 1679, 1998)
mytree.traverse()
mytree.findrange(1790, 1800)

pgraph.printtree(mytree)

'''
myTree = ngit.intervalTree(a, 0, 1, 1679, 1998)
myTree.pprint(6)
r = [1800, 1900]
print(myTree.findRange(r))
'''
