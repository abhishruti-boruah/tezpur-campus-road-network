class Graph:

    def __init__(self, n, nodes):

        self.n = n
        self.nodes = nodes

        self.adj_matrix = [[0 for _ in range(n)] for _ in range(n)]

        self.edges = []


    def add_edge(self, u, v):

        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

        self.edges.append((u, v))


    def print_adjacency_matrix(self):

        for row in self.adj_matrix:
            print(row)


    def print_incidence_matrix(self):

        m = len(self.edges)

        incidence = [[0 for _ in range(m)] for _ in range(self.n)]

        for idx, (u, v) in enumerate(self.edges):
            incidence[u][idx] = 1
            incidence[v][idx] = 1

        for row in incidence:
            print(row)
