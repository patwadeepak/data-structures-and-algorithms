def solve(s):
    zero = 0
    ones = 0
    for ch in s:
        if ch == '0':
            zero += 1
        else:
            ones += 1

    for ch in s:
        if ch == '0':
            if ones > 0:
                ones -= 1
            else:
                break
        else:
            if zero > 0:
                zero -= 1
            else:
                break
    
    return zero + ones


if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        s = input()
        print(solve(s))
