#include <iostream>
#include <string>
#include "graph.h"
using namespace std;

void pathelper(Graph &g, int src, int des, vector<bool> &vis, string path)
{
    vis[src] = true;
    path += to_string(src);
    
    if(src == des){
        cout << path << endl;
        vis[src] = false;
        return;
    }
    
    for (auto &p : g.l[src])
    {
        int neigh = p.first;
        if (!vis[neigh])
        {
            pathelper(g, neigh, des, vis, path);
        }
    }
    vis[src] = false;
}

void allPaths(Graph &g, int src, int des)
{
    vector<bool> visited(g.V, false);
    string path = "";
    pathelper(g, src, des, visited, path);
}

int main()
{
    int V = 6;
    Graph g(V);
    g.addEdge(1, 2);
    g.addEdge(0, 1);
    g.addEdge(1, 3);
    g.addEdge(3, 4);
    g.addEdge(2, 5);
    allPaths(g, 2, 4);

    return 0;
}