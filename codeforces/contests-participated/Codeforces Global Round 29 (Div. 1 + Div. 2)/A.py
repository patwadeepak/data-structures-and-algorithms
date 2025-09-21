def solve(x, y):
    if x < y:
        print(2)
        return

    if y == 1 or x == y:
        print(-1)
        return

    if x > y:
        if 1 < y < x - 1:
            print(3)
            return
        else:
            print(-1)
            return

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        x, y = list(map(int, input().split(' ')))
        solve(x, y)
