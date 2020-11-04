# -*- coding: utf-8 -*-

graph = {'A':['D','C','B'],
	 'B':['E'],
	 'C':['G','F'],
	 'D':['H'],
	 'E':['I'],
	 'F':['J']}

# The correct order is: ['A', 'B', 'E', 'I', 'C', 'F', 'J', 'G', 'D', 'H']

def depthFirstSearch(graph,source):
	stack = [source]
	array = []
	while len(stack) > 0:
# 		print("Current stack: %s" % stack)
		s = stack.pop()
# 		print("Popped: %s" % s)
		if s not in graph:
			array.append(s)
		if s not in array:
			array.append(s)
			for c in graph[s]:
				stack.append(c)
# 		else:
# 			print("%s was in array" % s)
	return array

if __name__ == '__main__':
    result = depthFirstSearch(graph,'A')
    print(result)