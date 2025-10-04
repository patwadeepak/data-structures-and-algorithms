def solve(a, n):
    a = set(a)
    return 2*len(a) - 1 

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        print(solve(a, n))
