def solve(n):
    if n%3 == 0:
        return 0
    return 3-n%3

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        print(solve(n))
        t -= 1