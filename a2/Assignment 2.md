#Homework Assignment 2
##
###Problem 1
![](https://github.com/JoshuaGhost/lsdm16/blob/master/a2p1fml.png?raw=true)
##
###Problem 2
####Question 1

{

'Even hash them ', 

'hash them four bytes each, ',

'four bytes each, space needed ', 

'space needed store ', 

'store still roughly four times ', 

'still roughly four times space taken ', 

'space taken document ', 

'document '

}

####Question 2
	
n-k+1
##
###Problem 3

Map phase: 
	
	
Map(index\_of\_band, index\_of\_doc, shingles\_of\_every\_doc) -> <index\_of\_band, index\_of\_doc, hash\_per\_band>

Inside ever Mapper hash table for every documents is caculated within

same band. Meanwhile indexes of documents are only be preserved.
  
Reduce phase:
	
Reduce(index\_of\_doc, hash\_table\_per\_band) -> <index\_of\_doc, hash\_table\_per\_doc>

For every Reducer hash tables per band are grouped and ordered according to document id

##
###Problem 4

![](https://github.com/JoshuaGhost/lsdm16/blob/master/p4f0.png?raw=true)

![](https://github.com/JoshuaGhost/lsdm16/blob/master/p4f1.png?raw=true)

![](https://github.com/JoshuaGhost/lsdm16/blob/master/p4f2.png?raw=true)

![](https://github.com/JoshuaGhost/lsdm16/blob/master/p4f3.png?raw=true)

![](https://github.com/JoshuaGhost/lsdm16/blob/master/p4f4.png?raw=true)
##
###Problem 5

1.	precise threshold	: 0.569

	estimate threshold	: 0.607

	relative difference(|pt-et|/pt)	: 0.066

2. precise threshold	: 0.406

	estimate threshold	: 0.464
	
	relative difference	: 0.143

3. precise threshold	: 0.880

	estimate threshold	: 0.890

	relative differnce	: 0.011
	
The esitimate threshold approches to precise threshold when the value of formular is exactly 1/2, especially when the value of b as well as r are sufficiently great.
##
###Problem 6

1. max(x, y) is not a distance measure. When x!=0, max(x, x)=x!=0 Identity not holds.
	
2. diff(x, y) is a distance measure. Because
	1. Non-negativity: 	diff(x, y) = |x - y| >= 0, 
							if and only if x = y the equality holds.
	2. symmetricity: 	diff(x, y) = |x - y| = |y - x| = diff(y, x)
		3. Identity: 		diff(x, y) = |x - y| = 0, iff x = y
		4. Trangle inequality:	
			diff(x, y) + diff(y, z) = |x - y| + |y - z|
			case 1: x = z
					|x - y| + |y - z| 
					=|x - y| + |y - x|>=0=|x - x| = |x - y| = diff(x, y)
			case 2: x != z,
					let x < z
					unequality={x-y+z-y=z-x+2x-2y>z-x=diff(x, z), if 0<y<x<z
							   {y-x+z-y=z-x=diff(x,z), if x<=y<z
							   {y-z+y-x=z-x-2z+2y>z-x=diff(x, z), if x<z<=y
		so, it's a metric
	
3. sum(x, y) = x + y is not a metric. if x!=0 sum(x, x)=2x!=0 Identity not holds.

4. Jaccard distance is a matric.
	Given three sets A, B and C, Jaccard distance of two sets (e.g. A
	and B) is defined as J(A, B) = 1-|AnB|/|AUB|
	1. Non-negativity:	1-|AnB|/|AUB|>=0, iff A=B the equality holds.
	2. Symmetricity:	J(A, B)=1-|AnB|/|AUB|=1-|BnA|/|AUB|=J(B, A)
	3. Identity:		J(A, A)=1-|AnA|/|AUA|=1-|A|/|A|=0
	4. Trangle inequality: see solution below:
![](https://github.com/JoshuaGhost/lsdm16/blob/master/p6f0.png?raw=true)
![](https://github.com/JoshuaGhost/lsdm16/blob/master/p6f1.png?raw=true)

5. Shotest path is a distance measure
	Given a graph G=(V,E,W), where by V is the set of vertex, E is the set of edge which is a sub set of VxV, W is the set of weight, for each edge there is a non-negtive weight.

	Define len(V')=sum(w'∈W) where V'⊆V, w's are with V' corresponded weight.

	Define sp(x, y): ∀x∈V,∀y∈V:(V(x, y)∨(∃z∈V:sp(x, z)∧V(z, y))∧(¬∃z∈V:len(sp(x, z))+len(sp(z, y))<len(sp(x, y))).

	1. Non-negativity: 	Since lenth of shotest path is defined as sum of weight of subset of edge, and weight edges is non-negative, length of shothest path is non-negative.
	2. Symmertricity:  	Since the graph G is a undirected graph, length(sp(x,y))=length(xp(y,x))
	3. Identity:		Obviously len(sp(x, x))=0 ∀x∈V
	4. Trangle inequality:	
		
		given sp(x, y) (∀x∈V,∀y∈V) is a shortest path between x and y.

		assume ∃z∈V, let len(sp(x,z))+len(sp(z,y))<len(sp(x,y)). 
		
		Then z either on sp(x,y), which meet a contradiction of the defination of length of a path, or not on sp(x,y), which leads to another contradiction that x->z->y is the shortest path, instead of x->y.

		∴len(sp(x,z))+len(sp(z,y))>=len(sp(x,y))
 