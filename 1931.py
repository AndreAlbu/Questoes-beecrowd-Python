# Problem link: https://www.beecrowd.com.br/judge/pt/problems/view/1931
# Author: Alex Sousa Cruz (@alequisk)

import heapq
adj = []
INF = 0x3f3f3f3f

def init():
    global adj
    adj = [0] * (n + 1)
    for i in range(0, n + 1):
        adj[i] = []


def add_edge(u, v, c):
    adj[u].append([v, c])


def dijkstra(start, end):
    used = []
    dists = []
    for i in range(n + 1):
        used.append([False, False])
        dists.append([INF, INF])

    dists[start][0] = 0
    dists[start][1] = 0
    ## cost, u, state
    pq = [(0, start, 0)]
    heapq.heapify(pq)

    while len(pq) > 0:
        (cost, u, state) = heapq.heappop(pq)
        if used[u][state]:
            continue
        used[u][state] = True

        for x in adj[u]:
            [to, wei] = x
            if dists[to][1 - state] > cost + wei:
                dists[to][1 - state] = cost + wei
                heapq.heappush(pq, (dists[to][1 - state], to, 1 - state))

    if dists[end][0] == INF:
        return -1
    return dists[end][0]


n, m = map(int, input().split())
init()
for _ in range(m):
    u, v, c = map(int, input().split())
    add_edge(u, v, c)
    add_edge(v, u, c)

print(dijkstra(1, n))
