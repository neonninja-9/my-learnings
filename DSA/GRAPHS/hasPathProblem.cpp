#include <iostream>
#include <vector>
#include "graph.h"

using namespace std;

bool hasPathHelper(Graph& g, int src, int dst, vector<bool>& visited) {
    if (src == dst) {
        return true;
    }
    visited[src] = true;
    for (auto& p : g.l[src]) {
        int neighbor = p.first;
        if (!visited[neighbor]) {
            if (hasPathHelper(g, neighbor, dst, visited)) {
                return true;
            }
        }
    }
    return false;
}

bool hasPath(Graph& g, int src, int dst) {
    vector<bool> visited(g.V, false);
    return hasPathHelper(g, src, dst, visited);
}

int main() {
    Graph g(5);
    g.addEdge(0, 1, 1);
    g.addEdge(1, 2, 1);
    g.addEdge(2, 3, 1);
    g.addEdge(3, 4, 1);
    
    if (hasPath(g, 0, 4)) {
        std::cout << "Path exists from 0 to 4" << std::endl;
    } else {
        std::cout << "No path from 0 to 4" << std::endl;
    }
    return 0;
}