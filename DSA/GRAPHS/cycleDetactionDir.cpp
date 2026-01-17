#include <iostream>
#include <vector>
#include "graph.h"
using namespace std;

// For directed graph cycle detection using DFS
bool hasCycleHelper(Graph& g, int node, vector<bool>& visited, vector<bool>& recStack) {
    visited[node] = true;
    recStack[node] = true;
    
    for (auto& p : g.l[node]) {
        int neighbor = p.first;
        if (!visited[neighbor]) {
            if (hasCycleHelper(g, neighbor, visited, recStack)) {
                return true;
            }
        } else if (recStack[neighbor]) {//if neighbbour is already in recursion path
            return true;  // Back edge found
        }
    }
    recStack[node] = false;
    return false;
}

bool hasCycle(Graph& g) {
    vector<bool> visited(g.V, false);
    vector<bool> recStack(g.V, false);
    
    for (int i = 0; i < g.V; i++) {
        if (!visited[i]) {
            if (hasCycleHelper(g, i, visited, recStack)) {
                return true;
            }
        }
    }
    return false;
}

int main() {
    Graph g(5,true);
    g.addEdge(0, 1);
    g.addEdge(1, 2);
    g.addEdge(2, 3);
    g.addEdge(3, 4);
    g.addEdge(4, 0);  // Creates a cycle
    g.print();
    
    return 0;
}