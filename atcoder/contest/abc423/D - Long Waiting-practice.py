import heapq

def solve(n, k, g):
    occ = 0
    t = []

    # process first customer group
    print(g[0][0])
    heapq.heappush(t, ((g[0][0]+g[0][1], g[0][2])))    
    occ = g[0][2]

    max_time = float('-inf')
    for i in range(1, n):
        while occ+g[i][2] > k:
            x, y = heapq.heappop(t)
            occ -= y
            max_time = max(x, max_time)

        # finally let new group enter restaurant
        if max_time == float('-inf'):
            print(g[i][0])
            heapq.heappush(t, ((g[i][0]+g[i][1], g[i][2])))    
            occ += g[i][2]
        else:
            value = max(g[i][0], max_time)
            print(value)
            heapq.heappush(t, ((value+g[i][1], g[i][2])))    
            occ += g[i][2]


if __name__ == '__main__':
    n, k = list(map(int, input().split(' ')))
    g = []
    for _ in range(n):
        g.append(list(map(int, input().split(' '))))
    solve(n, k, g)
