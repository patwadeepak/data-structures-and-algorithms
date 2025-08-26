def solve(a, n, k):
    is_sorted = a == sorted(a)
    if is_sorted:
        print('YES')
        return

    if k <= 1:
        print('NO')
        return
    
    print('YES')

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, k = list(map(int, input().split(' ')))
        a = list(map(int, input().split(' ')))
        solve(a, n, k)
