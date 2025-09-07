def solve(k, x):
    return (2**k)*x

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        k, x = list(map(int, input().split(' ')))
        print(solve(k, x))
