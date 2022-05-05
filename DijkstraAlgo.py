'''
    Dijkstra's Algorithm

    find the shortest path in  a graph using Dijkstra's algorithm
'''

def dijkstra(adjacency_matrix):

    '''
        find the shortest path in  a graph using Dijkstra's algorithm

        Args:
            adjacency_matrix (list): adjacency matrix of the graph

        Returns:
            list: list of the shortest path from the source to all the other nodes
    '''

    # find the number of nodes in the graph
    num_nodes = len(adjacency_matrix)

    # initialize the distance of the nodes to infinity
    distance = [float('inf')] * num_nodes

    # initialize the parent of the nodes to None
    parent = [None] * num_nodes

    # initialize the visited nodes to False
    visited = [False] * num_nodes

    # initialize the source node to 0
    source = 0

    # initialize the distance of the source node to 0
    distance[source] = 0

    # while there are still unvisited nodes
    while sum(visited) != num_nodes:

        # find the unvisited node with the smallest distance
        min_distance = float('inf')
        min_index = None
        for i in range(num_nodes):
            if not visited[i] and distance[i] < min_distance:
                min_distance = distance[i]
                min_index = i

        # mark the node as visited
        visited[min_index] = True

        # update the distance of the adjacent nodes
        for i in range(num_nodes):
            if adjacency_matrix[min_index][i] != 0 and distance[i] > distance[min_index] + adjacency_matrix[min_index][i]:
                distance[i] = distance[min_index] + adjacency_matrix[min_index][i]
                parent[i] = min_index

    # return the distance and parent list
    return distance, parent

if __name__ == "__main__":

    adjacency_matrix = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]
    distance, parent = dijkstra(adjacency_matrix)
    print(distance, parent)