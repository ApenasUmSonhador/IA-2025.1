# Min-Heap implementation
import heapq

# Uniform Cost Search Algorithm: This algorithm finds the least cost path in a weighted graph.
def uniform_cost_search(graph, start, end):
    # Set to keep track of visited nodes
    visited = set()
    # Priority queue to store the nodes to be explored and their costs
    # Each element is a tuple (cost, node, path)
    # The path is a list of nodes from start to the current node
    priority_queue = [(0, start, [start])]

    # While there are nodes to explore
    while priority_queue:
        # Get the node with the lowest cost
        cost, node, path = heapq.heappop(priority_queue)

        # If the node has already been visited, skip it
        if node in visited:
            continue
        
        # Mark the node as visited
        visited.add(node)
        
        # If the end node is reached, return the cost and the path
        if node == end:
            return cost, path

        # Explore the neighbors of the current node
        for neighbor, new_cost in graph[node]:
            # Skip if the neighbor has already been visited
            if neighbor not in visited:
                # Add the neighbor to the priority queue with the updated cost and path
                heapq.heappush(priority_queue, (cost + new_cost, neighbor, path + [neighbor]))

    # If the end node is not reachable, return None
    return None

# Example usage, based on the graph structure of the question 1 in ../Aula-02/Aula_Pratica_02.pdf
if __name__ == "__main__":
    graph = {
        1: [(2, 4), (3, 2)],
        2: [(4, 3), (5, 7)],
        3: [(5, 1), (6, 6)],
        4: [(7, 2)],
        5: [(7, 3)],
        6: [(8, 4)],
        7: [(9, 2)],
        8: [(9, 1)],
        9: [(10, 3)],
        10: [(11, 2)],
        11: []
    }

    start = 1
    end = 11
    result = uniform_cost_search(graph, start, end)
    if result:
        cost, path = result
        print(f"Cost: {cost}, Path: {path}")
    else:
        print("No path found.")