# Backtracking

Backtracking is a problem-solving technique, particularly useful for problems that involve finding a solution among many possible configurations. It works by systematically trying to build a solution incrementally, and whenever a path is found to be invalid or non-optimal, it "backtracks" (reverts) to a previous state and explores a different path.

> **Analogy:**  
> Think of it like navigating a maze: you follow a path, and if you hit a dead end, you retrace your steps to the last junction and try another turn.

---

## Why Use Backtracking?

You should use backtracking when you need to solve problems that can be broken down into a series of choices, where each choice leads you closer to a solution. It's particularly well-suited for problems involving constraint satisfaction or optimization.

### Common Use Cases

- **Puzzles and Games:**  
  Sudoku solvers, N-Queens problem, solving mazes.

- **Combinatorial Problems:**  
  Generating permutations, combinations, and subsets.

- **Graph Problems:**  
  Finding all paths between two nodes, graph coloring.

---

## Pros and Cons vs. Similar Techniques

Backtracking is often compared to other search algorithms like Depth-First Search (DFS) and Breadth-First Search (BFS). In fact, backtracking is essentially a specialized form of DFS, as it explores one path completely before moving on to the next.

### Pros 👍

- **Finds all solutions:**  
  Unlike some greedy algorithms, backtracking can explore all possible paths to find all valid solutions to a problem, not just one.

- **Space-efficient:**  
  It generally uses less memory than BFS because it only needs to store the current path being explored, not all the paths at a given level.

- **Versatile:**  
  It's applicable to a wide range of problems with a clear decision-making structure.

### Cons 👎

- **Time-consuming:**  
  The worst-case time complexity can be exponential, as it may explore a vast number of incorrect paths before finding a solution. This makes it inefficient for problems with a massive state space.

- **Can be difficult to implement:**  
  The recursive nature of backtracking can be tricky to get right, especially handling the "backtrack" step correctly.

---

## The Backtracking "Recipe"

Thinking about backtracking involves three key components:

1. **Choice:**  
   What are the possible options at the current step?

2. **Constraints:**  
   What conditions must be met for a choice to be valid?

3. **Goal:**  
   What defines a successful solution?

### General Algorithm (Recursive)

1. **Base Case:**  
   If you've reached a state where you've found a solution (or a dead end), handle it (e.g., store the solution, or return).

2. **Recursive Step:**  
   For each valid choice you can make from the current state:
   - Make the choice.
   - Recurse: Call the function on the new state.
   - Undo the choice: This is the "backtracking" part. Revert the state to what it was before you made the choice, so you can explore other options.

---

## Example in generate_permutations.py
