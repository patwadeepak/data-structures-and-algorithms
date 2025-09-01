# https://codeforces.com/problemset/problem/1900/A

def solve(a, n):
    dots = 0
    max_dots = 0
    run_max_dots = 0
    for ch in a:
        if ch == '.':
            dots += 1
            run_max_dots += 1
            max_dots = max(run_max_dots, max_dots)
        else:
            run_max_dots = 0
    
    if max_dots >= 3:
        print(2)
    else:
        print(dots)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = input()
        solve(a, n)
