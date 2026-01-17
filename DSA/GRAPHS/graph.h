#ifndef GRAPH_H
#define GRAPH_H

#include <vector>
#include <list>
#include <utility>
#include <iostream>

class Graph
{
public:
    int V;
    bool dir;
    std::vector<std::list<std::pair<int, int>>> l; // adjacency list: list of (neighbor, weight)

    Graph(int v, bool dir = false) : V(v), dir(dir), l(v) {}

    void addEdge(int u, int v, int weight = 1)
    {
        if (u < 0 || u >= V || v < 0 || v >= V) return;


        l[u].push_back({v, weight});
        if (dir == false)
        {
            l[v].push_back({u, weight});
        }
    }

    void print()
    {
        if (dir)
        {
            std::cout << "Directed Graph: " << std::endl;
        }
        else
        {
            std::cout << "Undirected Graph: " << std::endl;
        }
        for (int u = 0; u < V; u++)
        {
            std::cout << u << ":";
            for (auto &p : l[u])
            {
                std::cout << "(" << p.first << "," << p.second << ") ";
            }
            std::cout << std::endl;
        }
    }
};

#endif // GRAPH_H
