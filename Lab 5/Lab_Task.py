import heapq

# --- TASK 1: Representing the Graph (Adjacency List) ---
# Note: Based on the provided image, there are two nodes labeled 'B'. 
# I will name them 'B_top' and 'B_bot' to distinguish them.
graph = {
    'S': [('B_top', 2), ('C', 4), ('B_bot', 4)],
    'B_top': [('G', 5), ('C', 5)],
    'C': [('G', 3), ('F', 3)],
    'B_bot': [('C', 1)],
    'E': [('B_bot', 4)],
    'F': [('B_bot', 1)],
    'G': [('C', 2)]
}

# --- TASK 2: DFS and BFS (Unweighted) ---

def run_dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    expanded_count = 0
    
    while stack:
        (node, path) = stack.pop()
        if node not in visited:
            expanded_count += 1
            if node == goal:
                return path, expanded_count
            visited.add(node)
            # Add neighbors to stack
            for (neighbor, _) in graph.get(node, []):
                stack.append((neighbor, path + [neighbor]))
    return None, expanded_count

def run_bfs(graph, start, goal):
    queue = [(start, [start])]
    visited = {start}
    expanded_count = 0
    
    while queue:
        (node, path) = queue.pop(0)
        expanded_count += 1
        if node == goal:
            return path, expanded_count
            
        for (neighbor, _) in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None, expanded_count

# --- TASK 3: A* Implementation ---

# Heuristic: Using h(n) = 0 (Dijkstra mode) as per your notes
# This is guaranteed to be admissible and consistent.
def h(n):
    return 0

def run_a_star(graph, start, goal):
    # openSet is a priority queue: (fScore, node)
    openSet = []
    heapq.heappush(openSet, (0 + h(start), start))
    
    cameFrom = {}
    gScore = {node: float('inf') for node in ['S', 'B_top', 'C', 'B_bot', 'E', 'F', 'G']}
    gScore[start] = 0
    
    fScore = {node: float('inf') for node in gScore}
    fScore[start] = h(start)
    
    expanded_count = 0
    
    while openSet:
        # Get node with lowest fScore
        current_f, current = heapq.heappop(openSet)
        expanded_count += 1
        
        if current == goal:
            # Reconstruct path
            path = []
            temp = current
            while temp in cameFrom:
                path.append(temp)
                temp = cameFrom[temp]
            path.append(start)
            return path[::-1], expanded_count, gScore[goal]

        for (neighbor, weight) in graph.get(current, []):
            tentative_gScore = gScore[current] + weight
            
            if tentative_gScore < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + h(neighbor)
                
                # Add to openSet if not already there
                # (Simple way: just push it, the lowest fScore will be popped first)
                heapq.heappush(openSet, (fScore[neighbor], neighbor))
                
    return None, expanded_count, 0

# --- TASK 4: Printing Results ---

start_node = 'S'
end_node = 'G'

print("--- DFS Results ---")
path_dfs, exp_dfs = run_dfs(graph, start_node, end_node)
print(f"Path: {path_dfs}\nNodes Expanded: {exp_dfs}\n")

print("--- BFS Results ---")
path_bfs, exp_bfs = run_bfs(graph, start_node, end_node)
print(f"Path: {path_bfs}\nNodes Expanded: {exp_bfs}\n")

print("--- A* Results ---")
path_astar, exp_astar, cost = run_a_star(graph, start_node, end_node)
print(f"Path: {path_astar}\nNodes Expanded: {exp_astar}\nTotal Cost: {cost}")