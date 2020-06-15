//
//  BFS1.cpp
//  BFS
//
//  Created by Olivier Chen on 6/12/20.
//  Copyright © 2020 Project. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <list>

using namespace std;

class Graph
{
    int V;
    list <int> *adj;
    bool *visited;
public:
    Graph(int V);
    void addEdge(int v, int w);
    void BFS1(int source);
};

Graph::Graph(int V)
{
    this -> V = V;
    adj = new list<int>[V];
}

void Graph::addEdge(int v, int w)
{
    adj[v].push_back(w);
}

void Graph::BFS1(int source)
{
    visited = new bool[V];
    for (int i = 0; i < V; i++)
    {
        visited[i] = false;
    }
    
    list <int> queue;
    list <int>::iterator i;
    
    visited[source] = true;
    queue.push_back(source);
    
    while (!queue.empty())
    {
        int curr = queue.front();
        cout << curr << " ";
        queue.pop_front();
        
        for (i = adj[curr].begin(); i != adj[curr].end(); i++)
        {
            int adjV = *i;
            if (!visited[adjV])
            {
                visited[adjV] = true;
                queue.push_back(adjV);
            }
        }
    }
}

int main()
{
    Graph jacky(6);
    jacky.addEdge(1,2);
    jacky.addEdge(1,3);
    jacky.addEdge(2,4);
    jacky.addEdge(2,5);
    jacky.addEdge(3,5);
    jacky.addEdge(4,5);
    jacky.addEdge(4,6);
    jacky.addEdge(5,6);
    jacky.BFS1(1);
    
    return 0;
}
