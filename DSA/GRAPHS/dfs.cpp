#include <iostream>
#include <stack>
#include <vector>
#include "graph.h"

using namespace std;
//DFS Iterative Approch
void DFS(Graph &g, int start)
{
    stack<int> s;
    vector<bool> visited(g.V, false);
    s.push(start);
    visited[start] = true;
    cout << "DFS Traversal starting from " << start << ": ";
    while (!s.empty())
    {
        int current = s.top();
        s.pop();
        cout << current << " ";
        for (auto &p : g.l[current])
        {
            int neighbor = p.first;
            if (!visited[neighbor])
            {
                visited[neighbor] = true;
                s.push(neighbor);
            }
        }
    }
    cout << endl;
}

//DFS recursive Approch
void DFShelper(Graph &g, int node, vector<bool> &visited)
{
    visited[node] = true;
    cout << node << " ";
    for (auto &p : g.l[node])
    {
        int neighbor = p.first;
        if (!visited[neighbor])
        {
            DFShelper(g, neighbor, visited);
        }
    }
}
void DFSrecursive(Graph &g, int start)
{
    vector<bool> visited(g.V, false);
    cout << "DFS Traversal starting from " << start << ": ";
    // handling disconnected components
    for (int i = 0; i < g.V; i++)
    {
        if (!visited[i])
        {
            DFShelper(g, i, visited);
        }
    }

    cout << endl;
}

int main()
{
    Graph g(5);
    g.addEdge(0, 1, 10);
    g.addEdge(0, 2, 5);
    g.addEdge(1, 2, 3);
    g.addEdge(1, 3, 1);
    g.addEdge(2, 3, 8);
    g.addEdge(2, 4, 2);
    g.addEdge(3, 4, 4);
    DFS(g, 0);
    DFSrecursive(g, 0);
    return 0;
}