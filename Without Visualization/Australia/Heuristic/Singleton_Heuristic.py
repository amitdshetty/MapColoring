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

	## heuristic functions
	def MRV(self, domainDictionary, colours):
		LeastRemainingValuesStates = {0:[],1:[],2:[],3:[]}

		for key, value in domainDictionary.items():
			if len(value)==0 and colours[key-1] == 0:
				LeastRemainingValuesStates[0].append(key-1)

			elif(len(value)==1 and colours[key-1]==0):
				LeastRemainingValuesStates[1].append(key-1)

			elif(len(value)==2 and colours[key-1]==0):
				LeastRemainingValuesStates[2].append(key-1)

			elif(len(value)==3 and colours[key-1]==0):
				LeastRemainingValuesStates[3].append(key-1)

		if len(LeastRemainingValuesStates[0])>0:
			return LeastRemainingValuesStates[0]

		elif len(LeastRemainingValuesStates[1])>0:
			return LeastRemainingValuesStates[1]

		elif len(LeastRemainingValuesStates[2])>0:
			return LeastRemainingValuesStates[2]

		elif len(LeastRemainingValuesStates[3])>0:
			return LeastRemainingValuesStates[3]

	def DegreeConstraint(self, domainDictionary, colours):
		MaximumDegreeConstraint = 0
		MaximumDC_State = -1

		for v in range(self.V): 
			if colours[v]!=0:
				continue
			temp = 0
			for i in range(self.V):
				if self.graph[v][i] == 1:
					temp = temp + 1
			if temp > MaximumDegreeConstraint:
				MaximumDegreeConstraint = temp
				MaximumDC_State = v
		return MaximumDC_State


	def LCV(self, domainDictionary, colours):
		MinimumDegreeConstraint = 0
		MinimumDC_State = -1

		for v in range(self.V): 
			if colours[v]!=0:
				continue
			temp = 0
			for i in range(self.V):
				if self.graph[v][i] == 0:
					temp = temp + 1
			if temp > MinimumDegreeConstraint:
				MinimumDegreeConstraint = temp
				MinimumDC_State = v

		return MinimumDC_State

	def getTheNextState(self, domainDictionary, colours):
		if self.checkIfAllStatesColored(colours):
			return 0
		NextState = 0

		nextMRVStates = self.MRV(domainDictionary, colours)
		nextDCStates = self.DegreeConstraint(domainDictionary, colours)
		nextLCVStates = self.LCV(domainDictionary, colours)
		
		if (len(nextMRVStates)==1):
			NextState = nextMRVStates[0]
		elif(nextDCStates!=-1):
			NextState = nextDCStates
		else:
			NextState = nextLCVStates

		return NextState



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


	#singleton methods
	def checkIfAllStatesColored(self, colors):
		numberofvertices = 0

		for color in colors:
			if color != 0:
				numberofvertices = numberofvertices + 1

		# check if all states has been assigned.
		if numberofvertices == 7:
			return True
		else:
			return False

	def checkSingletonConstraints(self, v):
		if self.checkIfAllStatesColored(colour): ## break condition to check if all states colored or not. 
				return True
		if v == self.V:  ## just to check if we have reached 50th end state.
				v = random.choice([a for a in range(len(colour)) if colour[a] == 0])

	def SingletonRemoveDomainVariables(self, v):
		## code to remove the color from the domain dictionary from the current state
		if c in DomainDictionary[v+1]:
			DomainDictionary[v+1].remove(c)

		## revert back the original domain variable current state color
		if c not in DomainDictionary[v+1]:
			DomainDictionary[v+1].append(c)
			DomainDictionary[v+1].sort()


	def SingletonHeartLogic(self, listofsingletonstates):
		if len(listofsingletonstates)==0:
			return
		stateToColor = -1
		## code to return the singleton state.
		for key,value in DomainDictionary.items():
			if len(value) == 1 and colour[key-1] == 0:
				stateToColor = key
				break
					
		## if there is no singleton state pass the v+1.
		if stateToColor == -1:
			## select one random state from the uncolored.
			current = random.choice([a for a in range(len(colour)) if colour[a] == 0])
			if self.graphColourUtil(m, colour, current) == True:
				return True
		else: ## if there is singleton state pass that singleton state.
			if self.graphColourUtil(m, colour, stateToColor-1) == True:
				return True

	# A recursive utility function to solve m 
	# coloring problem 
	def graphColourUtil(self, m, colour, v):
		try:
			if self.checkIfAllStatesColored(colour):
				return True
			if v == self.V:  ## just to check if we have reached 50th end state.
				return True

			## singleton logic. 
			listof_singleton_states = list(range(self.V%7))
			## core logic for singleton
			self.SingletonHeartLogic(listof_singleton_states)

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

					Nextstate = self.getTheNextState(DomainDictionary, colour)
					if Nextstate != -1:
						if self.graphColourUtil(m, colour, Nextstate) == True:
							return True
					else:
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
g = Graph(7) #number of states 48

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




