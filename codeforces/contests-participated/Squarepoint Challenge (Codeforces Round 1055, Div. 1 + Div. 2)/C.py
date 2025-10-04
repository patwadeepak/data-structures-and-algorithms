def solve(n, q):
    a = list(map(int, input().split()))
    prefix_arr = [None]*n
    diff = [0]*n

    prefix_arr[0] = (1, 0) if a[0] == 0 else (0, 1)
    for i, ai in enumerate(a[1:], start=1):
        z, o  = prefix_arr[i-1]
        prefix_arr[i] = (z+1, o) if ai == 0 else (z, o+1)
        diff[i] = diff[i-1] + (a[i-1] == a[i])

    for _ in range(q):
        l, r = list(map(lambda x: int(x)-1, input().split()))

        z, o = prefix_arr[r]
        z1, o1 = prefix_arr[l-1] if l-1 >= 0 else (0,0)

        o -= o1
        z -= z1

        if o%3 != 0 or z%3 != 0:
            print(-1)
            continue

        ans = (r-l+1)//3
        if diff[r] == diff[l]:
            ans += 1

        print(ans)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, q = list(map(int, input().split()))
        solve(n, q)
