def f(num):
    return int(str(num)[::-1])

def solve(x, y):
    a = [-1]*10
    a[0] = x
    a[1] = y
    
    for i in range(2, 10):
        a[i] = f(a[i-1] + a[i-2])
    
    return a[-1]

if __name__ == '__main__':
    x, y = list(map(int, input().split(' ')))
    result = solve(x, y)
    print(result)
