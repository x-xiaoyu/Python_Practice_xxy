// Problem: 797. All Paths from Source to Target
// Medium 2pts
// 04/24/2024

// Topics: DFS, BFS, Graph, Backtracking

//Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
//find all possible paths from node 0 to node n - 1 and return them in any order.
//The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., 
//there is a directed edge from node i to node graph[i][j]).

// Links: https://leetcode.com/problems/all-paths-from-source-to-target/

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

void backtrack(int** graph, int graphSize, int* graphColSize, int* path, int pathSize, int current, int*** result, int* returnSize, int** returnColumnSizes) {
    path[pathSize++] = current;  // Append current node to path

    // If the current node is the target node
    if (current == graphSize - 1) {
        // Allocate space for a new path in results
        (*result)[*returnSize] = (int*)malloc(sizeof(int) * pathSize);
        // Copy the path to the results
        for (int i = 0; i < pathSize; i++) {
            (*result)[*returnSize][i] = path[i];
        }
        // Set the column size for this path
        (*returnColumnSizes)[*returnSize] = pathSize;
        // Increment the count of paths found
        (*returnSize)++;
        // Dynamically increase memory allocation if necessary
        if (*returnSize % 100 == 0) {
            *result = realloc(*result, sizeof(int*) * (*returnSize + 100));
            *returnColumnSizes = realloc(*returnColumnSizes, sizeof(int) * (*returnSize + 100));
        }
    } else {
        // Recur for all the vertices adjacent to the current vertex
        for (int i = 0; i < graphColSize[current]; i++) {
            backtrack(graph, graphSize, graphColSize, path, pathSize, graph[current][i], result, returnSize, returnColumnSizes);
        }
    }

    pathSize--;  // Remove current node from path, backtrack
}

int** allPathsSourceTarget(int** graph, int graphSize, int* graphColSize, int* returnSize, int** returnColumnSizes) {
    // Allocate initial memory for results
    int** result = (int**)malloc(sizeof(int*) * 100);
    *returnSize = 0;
    *returnColumnSizes = (int*)malloc(sizeof(int) * 100);
    int* path = (int*)malloc(sizeof(int) * graphSize);  // To store the current path
    int pathSize = 0;

    backtrack(graph, graphSize, graphColSize, path, pathSize, 0, &result, returnSize, returnColumnSizes);

    return result;
}