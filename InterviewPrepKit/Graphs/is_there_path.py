'''
Return true or false if there is a path between two vertices in a undirected graph
'''

def is_there_path(graph, from_vertex, to_vertex, visited=None):
    ''' Determines if there's a path between two vertices in a graph'''
    
    if not visited:
        visited = set()
    # Base Case
    if from_vertex == to_vertex:
        return True
    visited.add(from_vertex)
    neighbors = graph[from_vertex]
    for vertex in neighbors:
        if vertex not in visited:
            if is_there_path(graph, vertex, to_vertex, visited):
                return True      
    return False

def main():

    # Define our graph using an adjencey list
    graph = {}

    # Add the edges between the vertices
    graph['A'] = ['D', 'C']
    graph['D'] = ['A', 'F']
    graph['C'] = ['A']
    graph['F'] = ['D']
    graph['B'] = ['E']
    graph['E'] = ['B']

    is_there_path(graph, 'B', 'E')

if __name__ == "__main__":
    main()