# Algorithm: 
# - A Graph is defined as a list, along with two empty arrays as visited_bfs and queue.
# - Define a function bfs with three parameters- an empty array to store visited elements, the graph and the starting node.
# - The node is appended to the queue and visited arrays.
# - A while loop is initiated with the condition queue is TRUE, and variable s is assigned with the zeroth element of the queue popped.
# - S is printed and a for loop is initialized inside the while loop  with the condition that the iterator doesn’t exceed the elements in the graph of s.
# - If the iterator is not in the visited array, it gets added to the visited and queue arrays.
# - Define a function dfs and a set called visited.
# - The function dfs has three params– visited, graph and node.
# - If node is not visited, it is printed and added to the set of visited.
# - A for loop is initialized with the condition that the graph node is not null, and it calls the dfs function with an iterator as the new node.
# - The functions BFS and DFS are called. 

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}
 
visit_BFS = []
queue = []
 
def bfs(visit_BFS, graph, node):
  visit_BFS.append(node)
  queue.append(node)
 
  while queue:
    s = queue.pop(0)
    print (s, end = " ")
 
    for nearNode in graph[s]:
      if nearNode not in visit_BFS:
        visit_BFS.append(nearNode)
        queue.append(nearNode)
 
visit_DFS = set()
 
def dfs(visit_DFS, graph, node):
    if node not in visit_DFS:
        print (node, end=" ")
        visit_DFS.add(node)
        for nearNode in graph[node]:
            dfs(visit_DFS, graph, nearNode)
 
print("BFS:" , end =" ")
bfs(visit_BFS, graph, 'A')
print('\n')
print("DFS:" , end =" ")
dfs(visit_DFS, graph, 'A')