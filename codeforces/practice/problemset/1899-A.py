def solve(n):
    ans = False
    if (n - 1)%3 == 0 or (n + 1)%3 == 0:
        ans = True
    print('First' if ans else 'Second')

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        solve(n)
