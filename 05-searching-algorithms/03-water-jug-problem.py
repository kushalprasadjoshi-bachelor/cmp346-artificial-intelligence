###################### WATER JUG PROBLEM ######################
# Problem Statement:
    # Two jugs with capacities A and B
    # Unlimited water supply
    # Measure exactly T liters
    # Allowed operations:
        # Fill a jug
        # Empty a jug
        # Pour water from one jug to another

from collections import deque

def water_jug_problem(capacity_a, capacity_b, target):
    # Set to keep track of already visited states
    # Each state is represented as (water_in_jug_A, water_in_jug_B)
    visited = set()

    # Queue for BFS
    # Each element contains: (current_state_A, current_state_B, path_taken)
    queue = deque()

    # Initial state: both jugs are empty
    queue.append((0, 0, []))

    # Continue BFS until queue is empty
    while queue:
        # Remove the front state from the queue
        a, b, path = queue.popleft()

        # If the target amount is found in either jug
        if a == target or b == target:
            # Add final state to path and return solution
            path.append((a, b))
            return path

        # Skip state if already visited
        if (a, b) in visited:
            continue

        # Mark current state as visited
        visited.add((a, b))

        # Add current state to the path
        path = path + [(a, b)]

        # Generate all possible next states using allowed operations
        next_states = [

            # Fill Jug A completely
            (capacity_a, b),

            # Fill Jug B completely
            (a, capacity_b),

            # Empty Jug A
            (0, b),

            # Empty Jug B
            (a, 0),

            # Pour water from Jug A to Jug B
            # Amount poured is the minimum of:
            #   - water available in A
            #   - remaining capacity in B
            (a - min(a, capacity_b - b),
             b + min(a, capacity_b - b)),

            # Pour water from Jug B to Jug A
            (a + min(b, capacity_a - a),
             b - min(b, capacity_a - a))
        ]

        # Add all unvisited next states to the BFS queue
        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    # If BFS completes without finding target
    return None

# Example usage:
if __name__ == "__main__":
    solution = water_jug_problem(
        capacity_a = int(input("Enter capacity of Jug A: ")),
        capacity_b = int(input("Enter capacity of Jug B: ")),
        target = int(input("Enter target amount of water: "))
    )

    print("Steps to reach target:", end=' ')
    if solution:
        for step in solution:
            print(step, end=' ')
    else:
        print("No solution exists.")