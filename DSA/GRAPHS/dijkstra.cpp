#include "graph.h"
#include <iostream>
#include <vector>
#include <queue>
#include <climits>

void dijkstra(Graph& g, int start) {
    std::vector<int> dist(g.V, INT_MAX);
    dist[start] = 0;
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> pq;
    pq.push({0, start}); // {distance, vertex}

    while (!pq.empty()) {
        int u = pq.top().second;
        int d = pq.top().first;
        pq.pop();
        if (d > dist[u]) continue;
        for (auto& p : g.l[u]) {
            int v = p.first;
            int weight = p.second;
            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }

    std::cout << "Dijkstra's shortest paths from " << start << ":" << std::endl;
    for (int i = 0; i < g.V; ++i) {
        if (dist[i] == INT_MAX) {
            std::cout << i << ": INF" << std::endl;
        } else {
            std::cout << i << ": " << dist[i] << std::endl;
        }
    }
}
