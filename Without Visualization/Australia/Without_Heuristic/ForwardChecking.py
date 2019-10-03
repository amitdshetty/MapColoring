# Python program for solution of M Coloring 
# problem using backtracking 
import time

stateDictionary = {}
colorDictionary = {"1": "red", "2": "green", "3": "blue"}
ResultDictionary = {}
DomainDictionary = {}


class Graph(): 

	def __init__(self, vertices): 
		self.V = vertices 
		self.graph = [[0 for column in range(vertices)]
							for row in range(vertices)] 

	# A utility function to check if the current color assignment 
	# is safe for vertex v 
	def isSafe(self, v, colour, c): 
		for i in range(self.V): 
			if self.graph[v][i] == 1 and colour[i] == c: 
				return False
		return True
	
	def getTheNeighbors(self, state):
		listofneighbors = []
		for i in range(self.V):
			if self.graph[state][i] == 1:
				listofneighbors.append(i)
		return listofneighbors


	# A recursive utility function to solve m 
	# coloring problem 
	def graphColourUtil(self, m, colour, v):
		try:
			if v == self.V:  ## just to check if we have reached 50th end state.
				return True

			if not DomainDictionary[v+1]: ## check if the domain has no colors in their domain variables. if it is empty return false
				return False

			for c in DomainDictionary[v+1]:
				if self.isSafe(v, colour, c) == True:
					colour[v] = c ## assign the color to that state
					neighbors = self.getTheNeighbors(v) ## get the neighbors of the current state.

					# code to remove colors in its neighboring states
					for neighbor in neighbors:
						if c in DomainDictionary[neighbor+1]:
							DomainDictionary[neighbor+1].remove(c) ## remove the color from the neighbor domain list

					if self.graphColourUtil(m, colour, v+1) == True:
						return True

					# revert the domain values of all current neighbors
					for neighbor in neighbors:
						a = neighbor+1
						if c not in DomainDictionary[a]:
							DomainDictionary[a].append(c) ## remove the color from the neighbor domain list
							DomainDictionary[a].sort()
					colour[v] = 0
		except Exception as e:
			print("something wrong", e)

	def graphColouring(self, m): 
		colour = [0] * self.V 
		if self.graphColourUtil(m, colour, 0) == False: 
			return False

		# Print the solution 
		print("Solution exist and Following are the assigned colours:")
		for idx, val in enumerate(colour): 
			 ResultDictionary[stateDictionary[str(idx+1)]] = colorDictionary[str(val)]
		return True


stateDictionary["1"] = "New South Wales"
stateDictionary["2"] = "Northern Territory"
stateDictionary["3"] = "Queensland"
stateDictionary["4"] = "South Australia"
stateDictionary["5"] = "Tasmania"
stateDictionary["6"] = "Victoria"
stateDictionary["7"] = "Western Australia"



def createdomainDictionary():
	for key, value in enumerate(stateDictionary):
		listofintegers = list(range(1,4))
		DomainDictionary[key+1] = listofintegers




createdomainDictionary()


# Driver Code 
g = Graph(7) #number of states 

g.graph =  [[0,0,1,1,0,1,0],
         [0,0,1,1,0,0,1],
         [1,1,0,1,0,0,0],
         [1,1,1,1,0,1,1],
         [0,0,0,0,0,0,0],
         [1,0,0,1,0,0,0],
         [0,1,0,1,0,0,0]]

m = 3  ## chromataic number

start = time.time()

g.graphColouring(m)

done = time.time()

elapsed = done - start
print("THE TOTAL TIME TAKEN FOR EXEC ----------------",elapsed)

for key, value in ResultDictionary.items():
	print("{} ==> {}".format(key,value))




