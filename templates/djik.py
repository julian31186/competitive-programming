'''
Used to find the shortest path from start node, to all other nodes within the graph (will not work with negative edges)

Returns the weight map of smallest costs from start node -> other nodes AND path map in a tuple
(weight_map,path_map)

graph -> adjacency list with (u : (c,v))

'''

def djik(graph,start,n):
    dists = {}
    prev = [-1] * n
    for i in range(1,n + 1):
        dists[i] = inf
    dists[start] = 0
    h = [(0,start)]
    while h:
        curr_cost,node = heapq.heappop(h)

        if dists[node] < curr_cost: continue

        for edge_cost,nei in graph[node]:
            if curr_cost + edge_cost < dists[nei]:
                dists[nei] = curr_cost + edge_cost
                prev[nei - 1] = node
                heapq.heappush(h,(curr_cost + edge_cost, nei))
    return (dists,prev)

def get_shortest_path(start_node,end_node,path_arr):
    path = [end_node]
    while start_node != end_node:
        to_end_node = path_arr[end_node - 1]
        path.append(to_end_node)
        end_node = to_end_node
    return path[::-1]