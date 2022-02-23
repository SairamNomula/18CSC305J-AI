# A* is one of the most successful search algorithms to find the shortest path between nodes or graphs.

def Aalgo(snode, enode):
         
        openst=set(snode)
        closest=set()
        g= {}
        prnt= {}
 
        g[snode]= 0
        prnt[snode]=snode
         
         
        while len(openst) > 0:
            n=None
 
            for vst in openst:
                if n == None or g[vst] + heuristic(vst) < g[n] + heuristic(n):
                    n = vst
             
                     
            if n == enode or Gnodes[n] == None:
                pass
            else:
                for (m, weight) in get_neighbors(n):
                    if m not in openst and m not in closest:
                        openst.add(m)
                        prnt[m] = n
                        g[m] = g[n] + weight
                         
     
                    else:
                        if g[m] > g[n] + weight:
                            g[m] = g[n] + weight
                            prnt[m] = n
                             
                            if m in closest:
                                closest.remove(m)
                                openst.add(m)
 
            if n == None:
                print('Path does not exist!')
                return None
 
            if n == enode:
                path = []
 
                while prnt[n] != n:
                    path.append(n)
                    n = prnt[n]
 
                path.append(snode)
 
                path.reverse()
 
                print('Path found: {}'.format(path))
                return path
 
 
           
            openst.remove(n)
            closest.add(n)
 
        print('Path does not exist!')
        return None
         
 
def get_neighbors(vst):
    if vst in Gnodes:
        return Gnodes[vst]
    else:
        return None
   
def heuristic(n):
        H_dist = {
            'A': 11,
            'B': 6,
            'C': 99,
            'D': 1,
            'E': 7,
            'G': 0,
             
        }
 
        return H_dist[n]
   
Gnodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1),('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
     
}
Aalgo('A', 'G')


# Path found: ['A', 'E', 'D', 'G']
# ['A', 'E', 'D', 'G']


# ------------------------------------------------
# State the real life applications of A* Algorithm
# It finds applications in diverse problems, including the problem of parsing using stochastic grammars in NLP. Pathfinding problem in applications such as video games
