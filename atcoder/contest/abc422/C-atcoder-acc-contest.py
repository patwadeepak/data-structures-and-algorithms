def solve():
    a, b, c = map(int, input().split(' '))
    m = None
    if a < c:
        b += c-a
        m = a
    else:
        b += a-c
        m = c
    
    if b >= m:
        print(m)
    else:
        print(b + (2*(m-b))//3)

if __name__ == "__main__":
    t = int(input())

    for i in range(1, t+1):
        solve()