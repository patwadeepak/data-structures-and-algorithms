def solve(n, a):
    a = set(a)
    print(len(a))
    return

if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        a = map(int, input().split())
        solve(n, a)
