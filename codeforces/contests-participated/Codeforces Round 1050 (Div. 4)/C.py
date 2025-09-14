def solve(n, total_m, req):
    score = 0
    prev_m = 0
    zero = True
    for m,b in req:
        M = m
        if b == 0 and zero:
            if m%2 == 0 and m > 2:
                m -= prev_m
                score += m - 2
                zero = True
            elif m%2 != 0:
                m -= prev_m
                score += m - 1
                zero = False
        else:
            if m%2 == 0:
                m -= prev_m
                score += m - 1
                zero = not zero
            else:
                m -= prev_m
                score += m
        
        prev_m = M
    
    if total_m < prev_m:
        score += total_m - prev_m

    return score


if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, M = list(map(int, input().split(' ')))
        req = []
        for _ in range(n):
            m, b = list(map(int, input().split(' ')))
            req.append((m, b))
        output = solve(n, M, req)
        print(output)

