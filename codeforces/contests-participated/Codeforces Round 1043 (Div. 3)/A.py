# A. Homework

def solve(n, a, m, b, c):
    result = [a]
    for i, ch in enumerate(c):
        if ch == 'V':
            result.insert(0, b[i])
        else:
            result.append(b[i])
    
    print(''.join(result))


if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n = int(input())
        a = input()
        m = int(input())
        b = input()
        c = input()

        solve(n, a, m, b, c)

# Correct