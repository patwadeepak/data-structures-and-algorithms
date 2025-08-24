# D. From 1 to Infinity
# https://codeforces.com/contest/2132/problem/D

"""
n can be 10^15, so we can't loop over numbers as it will be TLE

sum of first k digit in 1 to infinity series.

0 1 2 3 4 5 6 7 8 9
1 1 1 1 ...       9
0 1 2 3 ...       9


single digit numbers = 10 (digit count 9 only here as start from 0) = 9
                sum1 = n * (n + 1) / 2 = 45

double digit numbers = 10 to 99 -> 99 - 10 + 1 = 90 , digit count = 2 * 90 = 180
                sum2 = 855 = 19 * 45

three digit numbers = 100 to 999 -> 999 - 100 + 1 = 900 , digit count = 3 * 900) = 2700
                sum3 = 12600 = 280 * 45

last_num = 20//digit_order
sum from min_number_of_digit_order to 20//(digit_order)
digits_left = 20%digit_order

final_num = last_num + 1
while digits_left != 0:
    sum += final_num//(10**digits_left)
    digits_left -= 1

"""
import math

def sumOfDigits(n, a):
    if n < 10:
        return (n * (n + 1) // 2)

    d = int(math.log10(n))
    p = 10**d
    m = n // p

    return (m * a[d]) + ((m * (m - 1) // 2) * p) + (m * (1 + n % p)) + sumOfDigits(n % p, a)


def solve(n, a):
    i = 0
    last_full_num_sum = None
    last_full_num = None
    while n > 0:
        i += 1

        digit_in_i = i * 9 * 10**(i-1)
        if digit_in_i <= n:
            n -= digit_in_i
        else:
            if n <= i:
                last_full_num_sum = 1
                last_full_num = 10**(i-1) - 1
            else:
                last_full_num = (n//i - 1) * 10**(i-1)
                partial_num_digits = n%i
                partial_num = last_full_num + 1
            break
    
    total = sumOfDigits(last_full_num, a)
    if last_full_num_sum is not None:
        total += last_full_num_sum
    else:
        total += sum(map(int, list(str(partial_num)[:partial_num_digits])))

    print(total)


if __name__ == '__main__':
    """
    There is some logical bug in this solution still.
    Will attempt this after CF competition today.
    """
    d = 16 # since n can vary till 10**15
    a = [0] * (d + 1)
    a[0] = 0
    a[1] = 45

    for i in range(2, d + 1):
        a[i] = a[i - 1] * 10 + 45 * int(math.ceil(math.pow(10, i - 1)))

    t = int(input())
    for i in range(1, t+1):
        n = int(input())

        solve(n, a)
