#Backtracking Australia (Without heuristic)

# Python program for solution of M Coloring
# problem using backtracking
import time

stateDictionary = {}
colorDictionary = {"1": "red", "2": "green", "3": "blue"}
ResultDictionary = {}


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

    # A recursive utility function to solve m
    # coloring problem
    def graphColourUtil(self, m, colour, v):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.isSafe(v, colour, c) == True:
                colour[v] = c
                if self.graphColourUtil(m, colour, v + 1) == True:
                    return True
                colour[v] = 0

    def graphColouring(self, m):
        colour = [0] * self.V
        if self.graphColourUtil(m, colour, 0) == False:
            return False

        # Print the solution
        print("Solution exist and Following are the assigned colours:")
        for idx, val in enumerate(colour):
            ResultDictionary[stateDictionary[str(idx + 1)]] = colorDictionary[str(val)]
        return True

stateDictionary["1"] = "New South Wales"
stateDictionary["2"] = "Northern Territory"
stateDictionary["3"] = "Queensland"
stateDictionary["4"] = "South Australia"
stateDictionary["5"] = "Tasmania"
stateDictionary["6"] = "Victoria"
stateDictionary["7"] = "Western Australia"

# create the state and integer mapping dictionary
# createStateDictionary()

# Driver Code
g = Graph(7)  # number of states 7

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