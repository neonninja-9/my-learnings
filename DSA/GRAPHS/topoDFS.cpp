#include <iostream>
#include <vector>
#include <stack>
using namespace std;
class Graph
{
public:
    int V;
    vector<vector<int>> l;
    Graph(int v)
    {
        V = v;
        l.resize(v);
    }
    void addEdge(int u, int v)
    {
        l[u].push_back(v);
    }
};
void topologicalSort(const Graph &g, int &src, vector<int> &vis, stack<int> &s)
{
    vis[src] = true;
    for (int v : g.l[src])
    {
        if (!vis[v])
        {
            topologicalSort(g, v, vis, s);
        }
    }
    s.push(src);
}

void topoSort(Graph &g)
{
    vector<int> vis(g.V, false);
    stack<int> s;
    for (int i = 0; i < g.V; i++)
    {
        if (!vis[i])
        {
            topologicalSort(g, i, vis, s);
        }
    }
    while(!s.empty()){
        cout<<s.top()<<endl;
        s.pop();
    }
}
int main()
{
    Graph g(6);
    g.addEdge(5, 0);
    g.addEdge(5, 2);
    g.addEdge(4, 0);
    g.addEdge(4, 1);
    g.addEdge(2, 3);
    g.addEdge(1, 3);
    topoSort(g);

    return 0;
}