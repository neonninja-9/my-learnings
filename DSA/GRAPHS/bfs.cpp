#include "graph.h"
#include <iostream>
#include <queue>
#include <vector>

void bfs(Graph& g, int start) {
    std::vector<bool> visited(g.V, false);
    std::queue<int> q;
    q.push(start);
    visited[start] = true;
    std::cout << "BFS Traversal starting from " << start << ": ";
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        std::cout << u << " ";
        for (auto& p : g.l[u]) {
            int v = p.first;
            if (!visited[v]) {
                visited[v] = true;
                q.push(v);
            }
        }
    }
    std::cout << std::endl;
}
