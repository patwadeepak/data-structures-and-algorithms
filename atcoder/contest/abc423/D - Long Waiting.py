def solve(n, k, g):
    people = 0
    for i in range(n):
        if i == 0:
            print(g[i][0])
            people += g[i][2]
        # elif people + g[i][2] - g[]:

if __name__ == '__main__':
    n, k = list(map(int, input().split(' ')))
    g = []
    for _ in range(n):
        g.append(list(map(int, input().split(' '))))
    print(solve(n, k, g))

"""
Not a solution
Attempted when only 4 mins were left.
Not attempted properly.
Need to speed up to be able to solve all problems of the contest.
"""