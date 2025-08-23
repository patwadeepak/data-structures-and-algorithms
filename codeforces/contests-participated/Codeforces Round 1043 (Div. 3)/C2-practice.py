# C2. The Cunning Seller (hard version)

def decimal_to_arbitrary_base(decimal_num, base):
    digits = "012"
    result = ""
    current_num = decimal_num

    while current_num > 0:
        remainder = current_num % base
        result = digits[remainder] + result
        current_num //= base

    return result


def solve(n, k):
    output = list(map(int, list(decimal_to_arbitrary_base(n, 3))))
    cost = 0

    for x, ch in enumerate(output):
        min_deals = sum(output)
        if min_deals < k and x < len(output)-1:
            while output[x] > 0 and min_deals+2 <= k:
                output[x+1] += 3
                output[x] -= 1
                min_deals = sum(output)

    N = 0
    for x, ch in enumerate(output[::-1]):
        cost += (3**(x+1) + (x * 3**(x-1)))*int(ch)
        N += (3**(x)) * int(ch)

    if int(N) == int(n) and sum(output) <= k:
        print(int(cost))
    else:
        print(-1)


if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n, k = tuple(map(int, input().split(' ')))

        solve(n, k)

"""
Seems like a correct solution but CF is throwing TLE for now.
Lets see if we can make it more efficient.
"""