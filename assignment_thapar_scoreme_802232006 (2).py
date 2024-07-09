# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1njcHedYfSPKN_AOCtD6_4uhcLP2STPpj
"""

#here is code
def longest_path(graph):
    n = len(graph)
    def topological_sort(graph):
        n = len(graph)
        indegree = [0] * n
        for node in range(n):
            for neighbor, weight in graph[node]:
                indegree[neighbor] += 1

        sources = [node for node in range(n) if indegree[node] == 0]
        topo_order = []

        while sources:
            node = sources.pop(0)
            topo_order.append(node)
            for neighbor, weight in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    sources.append(neighbor)

        return topo_order

    topo_order = topological_sort(graph)
    dist = [-float('inf')] * n
    dist[topo_order[0]] = 0

    for node in topo_order:
        if dist[node] != -float('inf'):
            for neighbor, weight in graph[node]:
                if dist[neighbor] < dist[node] + weight:
                    dist[neighbor] = dist[node] + weight


    return max(dist)