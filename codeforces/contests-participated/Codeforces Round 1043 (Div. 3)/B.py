# B. The Secret Number

def solve(n):
    k = 1

    divisor = 1+(10**k)

    x = 0.1    
    values = []
    while divisor < n:
        if n % divisor == 0:
            values.append(n//divisor)
        k += 1
        divisor = 1+(10**k)

    if len(values) == 0:
        print(0)
    else:
        print(len(values))
        print(' '.join(map(str, values[::-1])))


if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n = int(input())

        solve(n)

# Incorrect