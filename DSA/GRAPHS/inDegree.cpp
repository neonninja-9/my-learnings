#include <iostream>
#include "graph.h"
using namespace std;

vector<int> calcIndegree(Graph &g)
{
    if (!g.dir) {
        cerr << "Error: In-degree only applies to directed graphs!" << endl;
        return vector<int>();
    }

    vector<int> indegrees(g.V, 0);
    for (int u = 0; u < g.V; u++)
    {
        list<pair<int, int>> neigh = g.l[u];
        for (auto &p : neigh)
        {
            int v = p.first;
            indegrees[v]++;
        }
    }
    return indegrees;
}
int main(){
    return 0;
}