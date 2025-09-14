def solve(a, n):
    if n%2 == 0:
        print(0)
    else:
        print(a)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        a, n = list(map(int, input().split(' ')))
        solve(a, n)
