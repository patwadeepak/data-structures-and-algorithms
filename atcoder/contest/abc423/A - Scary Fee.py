def solve(x, c):
    k = 1000*x/(1000 + c)
    return int((k//1000)*1000)

if __name__ == '__main__':
    x, c = map(int, input().split(' '))
    print(solve(x, c))
