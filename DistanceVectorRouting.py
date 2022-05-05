'''
Distance vector routing in python
'''
class table:

    def __init__(self, graph) -> None:
        
        self.graph = graph
        self.table = {}

    def update(self, node):
        
        for curr_node in range(0, len(self.graph)):

            distance = self.graph[node][curr_node]
            self.table[curr_node] = [distance, curr_node]
    
    def printTable(self):

        print(self.table)

class graph:

    def __init__(self, graph) -> None:
        
        self.nodes = len(graph)
        self.graph = graph
        self.tables = {}
        self.update_infinity()
        self.make_tables()
    
    def update_infinity(self):

        # update non existing edges between two nodes with infinity
        for i in range(0, len(self.graph)):

            for j in range(0, len(self.graph[i])):

                if(i != j and self.graph[i][j] == 0):

                    self.graph[i][j] =  float('inf')

    def make_tables(self):

        # make table for distance routing

        for curr_node in range(0, len(self.graph)):

            self.tables[curr_node] = table(self.graph)
            self.tables[curr_node].update(curr_node)

    def print_tables(self):

        for node in range(0, len(self.graph)):

            curr_table = self.tables[node]
            print("table", node, curr_table.table)

    def distanceVectorRouting(self, source):

        # update the table of the source node
       pass

                
if __name__ == "__main__":

    route = [
        [0, 2, 0, 1],
        [2, 0, 3, 7],
        [0, 3, 0, 11],
        [1, 7, 11, 0]
    ]

    route2 = [
        [0, 3, 5, 99],
        [3, 0, 99, 1],
        [5, 4, 0, 2],
        [99, 1, 2, 0]

    ]

    curr_graph = graph(route2)
    curr_graph.print_tables()