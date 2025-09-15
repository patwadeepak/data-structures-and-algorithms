def solve(n, k, a):
    if k in a:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, k = list(map(int, input().split(' ')))
        a = list(map(int, input().split(' ')))
        solve(n, k, a)
