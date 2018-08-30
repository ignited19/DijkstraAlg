#Dijkstra's Algorithm written in python

import sys

class Graph(): 
    def __init__(self, vertices):
        #Assigns a total number of vertices for given object
        self.V=vertices
        #Creates a graph for current object, study more
    
        self.map= [[0 for column in range(vertices)]
                    for row in range(vertices)]
    

    #Iterates through
    def minDistance(self,dist,sptSet):
        print "SPT:" ,dist
        shortest_distance =sys.maxint
        
        
        #Iterates through vertices to find new vertex to visit. 
        #Must have a value of false in sptSet
        for v in range(self.V):
            if dist[v]< shortest_distance and sptSet[v] ==False:
                shortest_distance = dist[v]
                shortest_distance_vertex = v
                print'Check vertex:' ,shortest_distance_vertex
        return shortest_distance_vertex
    
    def dijkstraAlgo(self, src):
        #dist=list DS
        dist = [sys.maxint]*self.V 
        dist[src]=0
        #Intializes Shortest Path Tree. 
        sptSet= [False]*self.V
        
        for cout in range(self.V):
            #returns the smallest vertice 
            u= self.minDistance(dist, sptSet)
            #puts smallest vertice into shortest path set
            sptSet[u] = True
            
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                            dist[v] = dist[u] + self.graph[u][v]
        


map  = Graph(4)
map.graph = [[0, 1, 2, 0],
           [1, 0, 0, 10],
           [2, 0, 0, 5],
           [0, 10, 5, 0],
          ];
map.dijkstraAlgo(0);