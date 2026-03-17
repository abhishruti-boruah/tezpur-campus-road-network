import csv
from graph import Graph

def load_nodes(filename):
    nodes = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            nodes.append(row[0])

    return nodes


def main():

    nodes = load_nodes("data.csv")

    g = Graph(len(nodes), nodes)

    print("Nodes in the graph:")
    print(nodes)

    print("\nAdd edges between buildings.")
    print("Type y for yes and n for no.\n")

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):

            ans = input(f"Is there a road between {nodes[i]} and {nodes[j]}? (y/n): ")

            if ans.lower() == 'y':
                g.add_edge(i, j)

    print("\nAdjacency Matrix:")
    g.print_adjacency_matrix()

    print("\nIncidence Matrix:")
    g.print_incidence_matrix()


if __name__ == "__main__":
    main()
