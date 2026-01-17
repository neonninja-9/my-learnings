#include <iostream>
#include <vector>
#include <queue>
#include <list>
using namespace std;

class Graph
{
    int V;
    list<int> *l;

public:

    Graph(int v)
    {
        this->V = v;
        l = new list<int>[V];
    }

    //an undirected graph
    void addEdge(int u, int v)
    {
        l[u].push_back(v);
        l[v].push_back(u);
    }
    void print()
    {
        for (int u = 0; u < V; u++)
        {
            list<int> neighbour = l[u];
            cout << u << ":";
            for (int v : neighbour)
            {
                cout << v << " ";
            }
            cout << endl;
        }
    }
    void bfs()
    {
        queue<int> Q;
        vector<bool> vis(V, false);
        Q.push(0);
        vis[0] = true;
        while (Q.size() > 0)
        {
            int u = Q.front();
            Q.pop();
            cout << u << ": ";
            list<int> neighbour = l[u];
            for (int v : neighbour)
            {
                if (!vis[v])
                {
                    vis[v] = true;
                    Q.push(v);
                }
            }
        }
        cout << endl;
    }
};

int main()
{
    int V = 5;
    Graph graph(V);
    graph.addEdge(0, 1);
    graph.addEdge(1, 2);
    graph.addEdge(1, 3);
    graph.addEdge(3, 4);
    graph.print();

    return 0;
}
