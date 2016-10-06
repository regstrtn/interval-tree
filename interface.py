from __future__ import print_function
import itree
import os 
import sys
import pprint
import pgraph
import csv
from igraph import igraph


fbcsv = open(sys.argv[1], "r")
fbcsv.readline()

#Read csv file after ignoring the first line
composers = csv.reader(fbcsv, delimiter = ",", quotechar = '"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
data = []

for row in composers:
	life = []
	#print(row[2].split("-")[1])
	life.append(int(row[2].split("-")[0]))
	life.append(int(row[2].split("-")[1]))
	life.append(row[1])
	data.append(life)

#Construct tree
a = data
mytree = itree.itree(a)

#Output tree dot file
pgraph.printtree(mytree)
os.system("dot -Tps mytree.dot -o tree.ps")

#Make interval graph. 
g = igraph(mytree, a)
g.printdotfile()
os.system("dot -Tps myg.dot -o graph.ps")

def insertintotree():
	s = int(raw_input("Interval start: "))
	e = int(raw_input("Interval end: "))
	c = raw_input("Composer name: ")
	mytree._insertdata(mytree.root, [s,e],c,mytree.start, mytree.end)

def largestclique():
	g.getmaxclique()

def largestcc():
	g.getlcc()

def getsongs():
	#Print Songs
	fbcsv.seek(0); fbcsv.readline()
	s = int(raw_input("Interval start: "))
	e = int(raw_input("Interval end: "))
	mytree.findsongs(s,e,composers)


def maxoverlap():
	s = int(raw_input("Interval start: "))
	e = int(raw_input("Interval end: "))
	#Find max overlap
	mytree.maximaloverlap(s,e, data)

def allcomposers():
	#Print composer Overlap
	s = int(raw_input("Interval start: "))
	e = int(raw_input("Interval end: "))
	overlaps = mytree.findrange(s,e)
	print(overlaps)


while(1):
	choice = raw_input("\nChoose a function :\n1.Get songs \n2.Find overlapping composers \n3.Find max overlap \n4.LargestTeam\n5.LargestGroup\n6.Insert Composer\n7.Exit\n: ")
	if(choice == "1"):
		getsongs()
	elif(choice == "2"):
		allcomposers()
	elif(choice == "3"):
		maxoverlap()
	elif(choice == "4"):
		largestclique()
	elif(choice == "5"):
		largestcc()
	elif(choice == "6"):
		insertintotree()
	elif(choice == "7"):
		sys.exit(0)


'''
myTree = ngit.intervalTree(a, 0, 1, 1679, 1998)
myTree.pprint(6)
r = [1800, 1900]
print(myTree.findRange(r))
'''
