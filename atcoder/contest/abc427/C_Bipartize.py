from collections import defaultdict as DD

n, m = map(int, input().split())
edges = [0]*m

deg = [0]*n

g = DD(set)

for i in range(m):
  u,v = map(int, input().split())
  u -= 1
  v -= 1
  edges[i] = (u, v)
  deg[u] += 1
  deg[v] += 1
  g[u].add(v)
  g[v].add(u)

def find_root(p, node):
  k = 0
  max_deg = deg[node]
  max_deg_node = node
  while p[node] >= 0:
    node = p[node]
    k += 1
    if max_deg < deg[node]:
      max_deg = max(max_deg, deg[node])
      max_deg_node = node
  return node, k, max_deg_node

def findCycles(V, edges):
  p = [-1] * V

  for edge in edges:
    u, v = edge

    if p[u] == -1 and p[v] == -1:
      p[v] = u
      p[u] = -2

    elif p[v] == -1:
      p[v] = u
      root_u,_,_ = find_root(p, u)
      p[root_u] = p[root_u] - 1
    
    elif p[u] == -1:
      p[u] = v
      root_v,_,_ = find_root(p, v)
      p[root_v] = p[root_v] - 1

    else:
      root_u,len_u,max_deg_node1 = find_root(p, u)
      root_v,len_v,max_deg_node2 = find_root(p, v)

      good_cycle = False
      if root_u == root_v:
        cycle_length = len_u + len_v + 1
        if cycle_length%2 == 0:
          good_cycle = True
        else:
          node_to_remove = None
          if deg[max_deg_node1] > deg[max_deg_node2]:
            node_to_remove = max_deg_node1
          else:
            node_to_remove = max_deg_node2

          connected_nodes = g[node_to_remove]
          if connected_nodes:
            otherNodeToBeRemoved = None
            max_deg = -1
            for otherNode in connected_nodes:
              if max_deg < deg[otherNode]:
                max_deg = deg[otherNode]
                otherNodeToBeRemoved = otherNode
            

            # removing the edge from otherNodeToBeRemoved to node_to_remove
            g[node_to_remove].discard(otherNodeToBeRemoved)
            g[otherNodeToBeRemoved].discard(node_to_remove)
            deg[node_to_remove] -= 1
            deg[otherNodeToBeRemoved] -= 1
            return True

      if good_cycle or root_u != root_v:
        if p[root_u] > p[root_v]:
          p[root_u] = root_v
          p[root_v] = p[root_v] - 2
        else:
          p[root_v] = root_u
          p[root_u] = p[root_u] - 2

  return False

wasAnEdgeRemoved = True
removedEdges = 0
while wasAnEdgeRemoved:
  wasAnEdgeRemoved = findCycles(n, edges)
  removedEdges += 1

print(removedEdges)

"""
This solution may or may not work
as I was not able to complete this in contest.
"""