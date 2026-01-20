#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

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

void dijkstra(vector<vector<Edge>> g, int src, int des)
{
    // Min-heap: {distance, vertex}
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    
    const long long INF = 4e18;
    int v = g.size();
    vector<long long> dist(v, INF);
    vector<int> par(v, -1);

    dist[src] = 0;
    pq.push({0, src});

    while (!pq.empty()) {
        long long d = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        // If this distance is greater than already found, skip
        if (d > dist[u]) continue;

        // Check all neighbors
        for (Edge &e : g[u]) {
            int neighbor = e.v;
            long long weight = e.wt;

            // If we find a shorter path
            if (dist[u] + weight < dist[neighbor]) {
                dist[neighbor] = dist[u] + weight;
                par[neighbor] = u;
                pq.push({dist[neighbor], neighbor});
            }
        }
    }

    // Print results for destination
    cout << "Shortest distance from " << src << " to " << des << ": " << dist[des] << "\n";
    cout << "Path: ";
    
    if (dist[des] == INF) {
        cout << "No path exists\n";
    } else {
        vector<int> path;
        int curr = des;
        while (curr != -1) {
            path.push_back(curr);
            curr = par[curr];
        }
        reverse(path.begin(), path.end());
        for (int i = 0; i < path.size(); i++) {
            cout << path[i];
            if (i < path.size() - 1) cout << " -> ";
        }
        cout << "\n";
    }
}
int main()
{
    vector<vector<Edge>> g(7);

    // Edges: A-C(3), A-F(2), C-D(4), C-E(1), C-F(2), D-B(1), E-B(2), E-F(3), F-G(5), B-G(2)

    // From A (0)
    g[0].push_back(Edge(2, 3)); // A -> C (weight 3)
    g[0].push_back(Edge(5, 2)); // A -> F (weight 2)

    // From C (2)
    g[2].push_back(Edge(3, 4)); // C -> D (weight 4)
    g[2].push_back(Edge(4, 1)); // C -> E (weight 1)
    g[2].push_back(Edge(5, 2)); // C -> F (weight 2)

    // From D (3)
    g[3].push_back(Edge(1, 1)); // D -> B (weight 1)

    // From E (4)
    g[4].push_back(Edge(1, 2)); // E -> B (weight 2)
    g[4].push_back(Edge(5, 3)); // E -> F (weight 3)

    // From F (5)
    g[5].push_back(Edge(6, 5)); // F -> G (weight 5)

    // From B (1)
    g[1].push_back(Edge(6, 2)); // B -> G (weight 2)

    dijkstra(g, 0, 6);

    return 0;
}