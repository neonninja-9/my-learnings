#include <iostream>
#include <queue>
#include <vector>
#include <stack>
#include "graph.h"

using namespace std;

/*
    Kahn's Algorithm (BFS) for Topological Sort
    Works only for DAG (Directed Acyclic Graph)

    Time Complexity:  O(V + E)
    Space Complexity: O(V)
*/

// Calculate in-degree for each vertex in a directed graph
vector<int> calcIndegree(Graph &g)
{
    if (!g.dir)
    {
        cerr << "Error: In-degree only applies to directed graphs!" << endl;
        return {};
    }

    vector<int> indegrees(g.V, 0);

    for (int u = 0; u < g.V; u++)
    {
        auto &neigh = g.l[u]; // reference: no copy
        for (auto &p : neigh)
        {
            int v = p.first;
            indegrees[v]++;
        }
    }

    return indegrees;
}

// Topological sort using Kahn’s algorithm
// Returns empty vector if cycle exists
vector<int> topoSort(Graph &g)
{
    vector<int> indegrees = calcIndegree(g);

    // if graph is invalid or not directed
    if (indegrees.empty())
        return {};

    queue<int> q;

    // Push all nodes with indegree 0
    for (int i = 0; i < g.V; i++)
    {
        if (indegrees[i] == 0)
            q.push(i);
    }

    vector<int> order;
    int processed = 0;

    while (!q.empty())
    {
        int curr = q.front();
        q.pop();

        order.push_back(curr);
        processed++;

        auto &neigh = g.l[curr]; // reference: no copy
        for (auto &p : neigh)
        {
            int nxt = p.first;

            indegrees[nxt]--;

            if (indegrees[nxt] == 0)
                q.push(nxt);
        }
    }

    // Cycle check: if all vertices are not processed, cycle exists
    if (processed != g.V)
        return {};

    return order;
}

// Utility function to print topo order
void printTopo(Graph &g)
{
    vector<int> order = topoSort(g);

    if (order.empty() && g.V > 0)
    {
        cout << "Cycle detected! Topological sort not possible." << endl;
        return;
    }

    for (int x : order)
        cout << x << " ";
    cout << endl;
}

int main()
{
    // ===== TEST CASE 1: Simple Linear Dependency =====
    cout << "Test Case 1: Simple Linear Dependency (5->4->3->2->1->0)" << endl;
    Graph g1(6, true);
    g1.addEdge(5, 4);
    g1.addEdge(4, 3);
    g1.addEdge(3, 2);
    g1.addEdge(2, 1);
    g1.addEdge(1, 0);
    cout << "Topological Order: ";
    printTopo(g1);
    cout << endl;

    // ===== TEST CASE 2: Diamond Dependency =====
    cout << "Test Case 2: Diamond Dependency" << endl;
    //      0
    //     / \
    //    1   2
    //     \ /
    //      3
    Graph g2(4, true);
    g2.addEdge(0, 1);
    g2.addEdge(0, 2);
    g2.addEdge(1, 3);
    g2.addEdge(2, 3);
    cout << "Topological Order: ";
    printTopo(g2);
    cout << endl;

    // ===== TEST CASE 3: Complex Graph =====
    cout << "Test Case 3: Complex Graph with Multiple Levels" << endl;
    //    5   4
    //    |   |
    //    2   3
    //     \ /
    //      1
    //      |
    //      0
    Graph g3(6, true);
    g3.addEdge(5, 2);
    g3.addEdge(4, 3);
    g3.addEdge(2, 1);
    g3.addEdge(3, 1);
    g3.addEdge(1, 0);
    cout << "Topological Order: ";
    printTopo(g3);
    cout << endl;

    // ===== TEST CASE 4: Single Vertex =====
    cout << "Test Case 4: Single Vertex (No Edges)" << endl;
    Graph g4(1, true);
    cout << "Topological Order: ";
    printTopo(g4);
    cout << endl;

    // ===== TEST CASE 5: Complete DAG =====
    cout << "Test Case 5: Complete DAG (All Earlier Vertices Point to Later Ones)" << endl;
    Graph g5(4, true);
    g5.addEdge(0, 1);
    g5.addEdge(0, 2);
    g5.addEdge(0, 3);
    g5.addEdge(1, 2);
    g5.addEdge(1, 3);
    g5.addEdge(2, 3);
    cout << "Topological Order: ";
    printTopo(g5);
    cout << endl;

    // ===== TEST CASE 6: Cycle Case =====
    cout << "Test Case 6: Cycle Graph (0->1->2->0)" << endl;
    Graph g6(3, true);
    g6.addEdge(0, 1);
    g6.addEdge(1, 2);
    g6.addEdge(2, 0);
    cout << "Topological Order: ";
    printTopo(g6);
    cout << endl;

    return 0;
}
