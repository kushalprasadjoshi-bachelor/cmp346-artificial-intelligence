def dfs(graph, start):
    visited = set()
    stack = [start]

    print("DFS Traversal Order:", end=' ')

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            stack.extend(reversed([neighbor for neighbor in graph[node] if neighbor not in visited]))

# Example usage:
if __name__ == "__main__":
    graph = {
        'A' : ['B','C'],
        'B' : ['D', 'E'],
        'C' : ['F'],
        'D' : [],
        'E' : ['F'],
        'F' : []
    }

    dfs(graph, 'A')
