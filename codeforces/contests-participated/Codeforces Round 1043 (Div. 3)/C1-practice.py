# C1. The Cunning Seller (easy version)

def decimal_to_arbitrary_base(decimal_num, base):
    digits = "012"
    result = ""
    current_num = decimal_num

    while current_num > 0:
        remainder = current_num % base
        result = digits[remainder] + result
        current_num //= base

    return result

def solve(n):
    output = decimal_to_arbitrary_base(n, 3)
    cost = 0
    for x, ch in enumerate(output[::-1]):
        cost += (3**(x+1) + (x * 3**(x-1)))*int(ch)
    print(int(cost))

if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n = int(input())

        solve(n)

# this was learning lesson on how to use ternary representation of number to solve problems.
# I looked at the solution for this one.