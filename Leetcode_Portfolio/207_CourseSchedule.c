// Problem: 207. Course Schedule
// Medium 2pts
// 04/24/2024
// Topics: DFS, BFS, Graph, Topological Sort

// Description: There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
// You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
// For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
// Return true if you can finish all courses. Otherwise, return false.



// Links:https://leetcode.com/problems/course-schedule/


bool canFinish(int numCourses, int** prerequisites, int prerequisitesSize, int* prerequisitesColSize) {
    // Allocate memory for the adjacency list and indegree array
    int* indegree = (int*) calloc(numCourses, sizeof(int));
    int** graph = (int**) malloc(numCourses * sizeof(int*));
    int* tempSizes = (int*) calloc(numCourses, sizeof(int));  // To track list sizes dynamically
    
    for (int i = 0; i < numCourses; ++i) {
        graph[i] = (int*) malloc(prerequisitesSize * sizeof(int));  // Allocate max possible size
        tempSizes[i] = 0;
    }
    
    // Build graph and compute indegree of each node
    for (int i = 0; i < prerequisitesSize; ++i) {
        int src = prerequisites[i][1];
        int dest = prerequisites[i][0];
        graph[src][tempSizes[src]++] = dest;  // Add destination to source's list
        indegree[dest]++;
    }
    
    // Queue for BFS
    int* queue = (int*) malloc(numCourses * sizeof(int));
    int front = 0, rear = 0;

    // Enqueue all vertices with indegree 0
    for (int i = 0; i < numCourses; ++i) {
        if (indegree[i] == 0) {
            queue[rear++] = i;
        }
    }
    
    // Process the queue
    int visitedCount = 0;
    while (front < rear) {
        int current = queue[front++];
        visitedCount++;
        for (int i = 0; i < tempSizes[current]; ++i) {
            int neighbor = graph[current][i];
            if (--indegree[neighbor] == 0) {
                queue[rear++] = neighbor;
            }
        }
    }
    
    // Clean up
    for (int i = 0; i < numCourses; ++i) {
        free(graph[i]);
    }
    free(graph);
    free(indegree);
    free(queue);
    free(tempSizes);
    
    // If count equals numCourses, all courses can be finished
    return visitedCount == numCourses;
}
