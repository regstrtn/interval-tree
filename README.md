# Interval Tree
Interval Tree
This is an implementation of an interval tree in python. There's an excellent tutorial on Interval trees in the links mentioned at the end of this page. An excerpt from Wikipedia is included below.

*[interface.py](https://github.com/regstrtn/interval-tree/blob/master/interface.py): The interface file, it reads a data file as input, constructs the interval tree, constructs the interval graph and runs other operations. 

**Usage**: python interface.py sample_data.csv

*[itree.py](https://github.com/regstrtn/interval-tree/blob/master/itree.py): The interval tree implementation

*[igraph.py](https://github.com/regstrtn/interval-tree/blob/master/igraph.py): Interval graph implementation

*[pgraph.py](https://github.com/regstrtn/interval-tree/blob/master/pgraph.py): Generates dot file for interval tree (to be displayed by graphviz). An excellent tutorial on graphviz is attached in dotguide.pdf.

*sample_data.csv: Sample data file

*timecomplexity.txt: Describes time complexity of each operation.

An interval tree is a tree data structure to hold intervals. It allows one to efficiently find all intervals that overlap with any given interval or point. The trivial solution is to visit each interval and test whether it intersects the given point or interval, which requires O(n) time, where n is the number of intervals in the collection. Since a query may return all intervals, for example if the query is a large interval intersecting all intervals in the collection, this is asymptotically optimal; however, we can do better by considering output-sensitive algorithms, where the runtime is expressed in terms of m, the number of intervals produced by the query. Interval trees have a query time of O(log n + m) and an initial creation time of O(n log n), while limiting memory consumption to O(n).

#####With inputs from the following blog:

***Implementation**: http://blog.nextgenetics.net/?e=45
***Tutorial**: http://www.dgp.utoronto.ca/people/JamesStewart/378notes/22intervals/
