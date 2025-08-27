# A. Painting With Two Colors

def solve(n, a, b):
    m = n%2
    if b%2 != m:
        print('NO')
    else:
        if a%2 != m:
            if b%2 == m and b > a:
                print('YES')
            else:
                print('NO')
        else:
            print('YES')

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, a, b = list(map(int, input().split(' ')))
        solve(n, a, b)
