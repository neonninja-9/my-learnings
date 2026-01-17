#include "graph.h"
#include <iostream>
#include <vector>
#include <queue>
#include <climits>

void primMST(Graph& g) {
    std::vector<int> key(g.V, INT_MAX);
    std::vector<bool> inMST(g.V, false);
    std::vector<int> parent(g.V, -1);
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> pq;

    key[0] = 0;
    pq.push({0, 0}); // {key, vertex}

    std::cout << "Prim's MST:" << std::endl;
    int totalWeight = 0;
    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();
        if (inMST[u]) continue;
        inMST[u] = true;
        if (parent[u] != -1) {
            std::cout << parent[u] << " - " << u << " : " << key[u] << std::endl;
            totalWeight += key[u];
        }
        for (auto& p : g.l[u]) {
            int v = p.first;
            int weight = p.second;
            if (!inMST[v] && weight < key[v]) {
                key[v] = weight;
                parent[v] = u;
                pq.push({key[v], v});
            }
        }
    }
    std::cout << "Total MST weight: " << totalWeight << std::endl;
}
