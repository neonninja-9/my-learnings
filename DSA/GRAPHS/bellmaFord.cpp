#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Edge
{
public:
    int v;
    int wt;
    Edge(int v, int wt)
    {
        this->v = v;
        this->wt = wt;
    }
};
void bellmanFord(vector<vector<Edge>> &g, int src)
{
    int V = g.size();
    vector<long long> dist(V, LLONG_MAX);
    dist[src] = 0;

    // Relax edges V-1 times
    for (int iter = 0; iter < V - 1; iter++)
    {
        for (int u = 0; u < V; u++)
        {
            if (dist[u] == LLONG_MAX) continue;
            
            for (Edge &e : g[u])
            {
                if (dist[u] + e.wt < dist[e.v])
                {
                    dist[e.v] = dist[u] + e.wt;
                }
            }
        }
    }

    // Check for negative cycle
    bool hasNegativeCycle = false;
    for (int u = 0; u < V; u++)
    {
        if (dist[u] == LLONG_MAX) continue;
        
        for (Edge &e : g[u])
        {
            if (dist[u] + e.wt < dist[e.v])
            {
                hasNegativeCycle = true;
                break;
            }
        }
        if (hasNegativeCycle) break;
    }

    if (hasNegativeCycle)
    {
        cout << "Negative cycle detected!" << endl;
        return;
    }

    // Print results
    cout << "Vertex\tDistance from " << src << endl;
    for (int i = 0; i < V; i++)
    {
        cout << i << "\t";
        if (dist[i] == LLONG_MAX)
            cout << "INF" << endl;
        else
            cout << dist[i] << endl;
    }
}

int main()
{
    vector<vector<Edge>> g(5);
    g[0].push_back({Edge(1, 2)});
    g[0].push_back({Edge(2, 4)});
    g[1].push_back({Edge(2, -4)});
    g[2].push_back({Edge(2, 3)});
    g[3].push_back({Edge(4, 4)});
    g[4].push_back({Edge(1, -1)});

    bellmanFord(g, 0);

    return 0;
}