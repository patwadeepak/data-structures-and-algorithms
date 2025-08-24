# A. Redstone?

def solve(a, n):
    my_set = set()
    for num in a:
        if num not in my_set:
            my_set.add(num)
        else:
            print('YES')
            return
    print('NO')


if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        solve(a, n)
