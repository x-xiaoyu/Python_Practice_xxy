// Problem: 547.number-of-provinces
// Medium 2pts
// 04/24/2024
// Topics: DFS, BFS, Graph, Union Find

// Description: There are n cities. Some of them are connected, while some are not. 
// If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
// A province is a group of directly or indirectly connected cities and no other cities outside of the group.
// You are given an n x n matrix isConnected where isConnected[i][j] = 1 
// if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
// Return the total number of provinces

// Links:https://leetcode.com/problems/number-of-provinces/description/


void dfs(int** isConnected, int isConnectedSize, int* visited, int i) {
    for (int j = 0; j < isConnectedSize; j++) {
        if (isConnected[i][j] == 1 && !visited[j]) {
            visited[j] = 1;
            dfs(isConnected, isConnectedSize, visited, j);
        }
    }
}

int findCircleNum(int** isConnected, int isConnectedSize, int* isConnectedColSize) {
    int* visited = (int*)calloc(isConnectedSize, sizeof(int));
    int count = 0;

    for (int i = 0; i < isConnectedSize; i++) {
        if (!visited[i]) {
            dfs(isConnected, isConnectedSize, visited, i);
            count++;
        }
    }

    free(visited);
    return count;
}
