def solve():
    n = int(input())
    a = [-1]*(n+1)
    for i in range(1, n+1):
        a[i] = input()

    x, y = input().split(' ')
    x = int(x)
    if a[x] == y:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    solve()
