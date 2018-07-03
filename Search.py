import sys
from queue import PriorityQueue

#Read input file
def readFile():
	
	commandArguments = (sys.argv)
	fo = open(commandArguments[1], "r")
	graphFile = fo.read()
	fo.close()
	inputList = graphFile.split()
	return inputList


def makeGraphWithoutWeights(inputList):
	graphDict = {}
	loopCounter = 0
	firstNumber = -1
	secondNumber = -1
	thirdNumber = -1
	for i in inputList:
		if (loopCounter == 0):
			firstNumber = i
			loopCounter += 1
		elif (loopCounter == 1):
			secondNumber = i
			loopCounter += 1
		elif (loopCounter == 2):
			thirdNumber = i
			loopCounter = 0

			if (firstNumber in graphDict):
				temp = graphDict[firstNumber]
				graphDict[firstNumber].add(secondNumber)
			else:
				graphDict[firstNumber] = {secondNumber}
	return(graphDict)


def makeGraphWithWeights(inputList):
	graphDict = {}
	loopCounter = 0
	firstNumber = -1
	secondNumber = -1
	thirdNumber = -1
	for i in inputList:
		if (loopCounter == 0):
			firstNumber = i
			loopCounter += 1
		elif (loopCounter == 1):
			secondNumber = i
			loopCounter += 1
		elif (loopCounter == 2):
			thirdNumber = i
			loopCounter = 0

			if (firstNumber in graphDict):
				temp = graphDict[firstNumber]
				graphDict[firstNumber][secondNumber] = thirdNumber
			else:
				graphDict[firstNumber] = {secondNumber: thirdNumber}
	return(graphDict)

def bfsPaths(graphDict, startNode, endNode):
	queue = [(startNode, [startNode])]
	while queue:
		(vertex, path) = queue.pop(0)
		for next in graphDict[vertex] - set(path):
			if next == endNode:
				yield path + [next]
			else:
				queue.append((next, path + [next]))


def breadthFirstSearch(graphDict, startNode, endNode):

	shortestPath = (next(bfsPaths(graphDict, startNode, endNode)))
	intShortestPath = [int(value) for value in shortestPath]
	return intShortestPath


def depthFirstSearch(graphDict, startNode, endNode, path = []):

	path = path + [startNode]
	if (startNode == endNode):
		return path
	if startNode not in graphDict:
		return None
	for node in graphDict[startNode]:
		if node not in path:
			newPath = depthFirstSearch(graphDict, node, endNode, path)
			if newPath:
				shortestPath = newPath
				intShortestPath = [int(value) for value in shortestPath]
				return intShortestPath


def uniformCostSearch(graphDict, startNode, endNode):

	queue = PriorityQueue()
	queue.put((0, [startNode]))

	while not queue.empty():
		node = queue.get()
		current = node[1][len(node[1]) - 1]

		if endNode in node[1]:
			intShortestPath = [int(value) for value in node[1]]
			return intShortestPath

		cost = node[0]
		if current in graphDict:
			for neighbor in graphDict[current]:
				temp = node[1][:]
				temp.append(neighbor)
				queue.put((cost + int(graphDict[str(current)][str(neighbor)]), temp))


def main():
	
	#Read command line arguments
	graphInput = readFile()
	startNode = (sys.argv)[2]
	endNode = (sys.argv)[3]
	searchType = (sys.argv)[4]

	if (searchType == "BFS"):
		shortestPath = breadthFirstSearch(makeGraphWithoutWeights(graphInput), startNode, endNode)
	elif (searchType == "DFS"):
		shortestPath = depthFirstSearch(makeGraphWithoutWeights(graphInput), startNode, endNode, [])
	elif (searchType == "UCS"):
		shortestPath = uniformCostSearch(makeGraphWithWeights(graphInput), startNode, endNode)
	else:
		shortestPath = "Please select a valid search type\n"

	print(shortestPath)
	#return shortestPath
	

main()

