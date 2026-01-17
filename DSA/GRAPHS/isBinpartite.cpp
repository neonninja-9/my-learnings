#include <iostream>
#include <vector>
#include <queue>
#include "graph.h"

using namespace std;
//assuming graph is conected 
bool isBipartite(Graph &g, int src){
    vector<bool> visited(g.V, false);
    queue<int> q;
    // 1 -> red, 0 -> black
    vector<int> color(g.V, -1);
    
    q.push(src);
    visited[src] = true;
    color[src] = 1;
    
    while(!q.empty()){
        int u = q.front();
        q.pop();
        
        for(auto& p : g.l[u]){
            int v = p.first;
            if(!visited[v]){
                visited[v] = true;
                color[v] = !color[u];  // Alternate color
                q.push(v);
            } else {
                // If already visited, check if color is different
                if(color[v] == color[u]){
                    return false;  // Same color means not bipartite
                }
            }
        }
    }
    return true;
}

//assuming graph is conected 
bool isBipartite2(Graph &g, int src){
    queue<int> q;
    // 1 -> red, 0 -> black, -1 -> unvisited
    vector<int> color(g.V, -1);
    
    q.push(src);
    color[src] = 1;
    
    while(!q.empty()){
        int u = q.front();
        q.pop();
        
        for(auto& p : g.l[u]){
            int v = p.first;
            if(color[v] == -1){
                // Not visited yet, assign alternate color
                color[v] = !color[u];
                q.push(v);
            } else {
                // If already visited, check if color is different
                if(color[v] == color[u]){
                    return false;  // Same color means not bipartite
                }
            }
        }
    }
    return true;
}

//use Bipartite using cycles

//              graph
//              /   \
//          cycle   noCycle
//         /     \        \
//      even    odd       bipartite
//      /           \
//    bipartite     not partite

bool isBipartiteUsingCycle(Graph &g){
    vector<int> distance(g.V, -1);  // -1 means unvisited
    queue<int> q;
    
    // Handle all components
    for(int start = 0; start < g.V; start++){
        if(distance[start] != -1) continue;  // Already processed
        
        q.push(start);
        distance[start] = 0;
        
        while(!q.empty()){
            int u = q.front();
            q.pop();
            
            for(auto& p : g.l[u]){
                int v = p.first;
                if(distance[v] == -1){
                    // Not visited, assign distance
                    distance[v] = distance[u] + 1;
                    q.push(v);
                } else {
                    // Back edge found (cycle detected)
                    // If distance difference is even, cycle length is odd
                    if((distance[u] - distance[v]) % 2 == 0){
                        return false;  // Odd cycle found -> Not bipartite
                    }
                }
            }
        }
    }
    return true;  // No odd cycles -> Bipartite
}

int main() {
    Graph g(5);
    g.addEdge(0,1);
    g.addEdge(0,2);
    g.addEdge(1,3);
    g.addEdge(3,4);
    g.addEdge(2,4);
    
    
    if(isBipartiteUsingCycle(g)){
        cout << "Graph is Bipartite" << endl;
    } else {
        cout << "Graph is NOT Bipartite" << endl;
    }
    
    return 0;
}