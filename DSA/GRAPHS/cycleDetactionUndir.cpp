#include <iostream>
#include <vector>
#include "graph.h"

using namespace std;
bool helper(Graph &g, int src, int par , vector<bool>&visited){
    visited[src] = true;
    for (auto &p : g.l[src]) {//loop on neighbours of source node
        int neigh = p.first;
        if (!visited[neigh]) {
            if (helper(g, neigh, src, visited)) return true;
        } else if (neigh != par) {
            return true;  // Back edge found
        }
    }
    return false;
}
bool hasCycle(Graph &g, int src)
{
    vector<bool> visited(g.V , false);
    return helper(g , src , -1 , visited);

}
int main()
{
    Graph g(5);
    g.addEdge(0, 1);
    g.addEdge(1, 2);
    g.addEdge(2, 3);
    g.addEdge(3, 4);
    g.addEdge(4, 0);  // Creates a cycle

    if (hasCycle(g, 0)) {
        cout << "Graph contains a cycle." << endl;
    } else {
        cout << "Graph does not contain a cycle." << endl;
    }

    return 0;
}