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

lets go into the details of step - 
sum from min_number_of_digit_order to last_num

lets say digit_order - 2, min_num = 100 & last_num = 256

ones places = 0, 1, 2, 3, 4, 5, 6         - 7 possibile choices
2s places   = 0, 1, 2, 3, 4, 5            - 6 possibile choices
3s plces    = 1, 2 (zero not allowed here)- 2 possibile choices

3s places - 1
2s places - 0 to 9
1s places - 0 to 9

45 + (10+45) + 20+45 + 30+45 ... + 90+45
10 + 20 + 30 + ... + 80 + 90 = 450
450 + 45 * 10 = 495

10 to 99

a[i] = (a[i-1] * 9) + 45*10**(i-1) = 405 + 450 = 855

855 + 180*1 = 1035

3s places - 2
2s places - 0 to 4
1s places - 0 to 9


S()

"""
import math

def sumOfDigits(n, a):
    if n < 10:
        return (n * (n + 1) // 2)

    d = int(math.log10(n))
    p = int(math.ceil(math.pow(10, d)))
    m = n // p

    return (m * a[d]) + ((m * (m - 1) // 2) * p) + (m * (1 + n % p)) + sumOfDigits(n % p, a)


def solve(n, a):
    digit_order = 1
    sum = 0

    # handle case of single digits
    if n <= 9:
        sum += n * (n + 1) / 2
        return sum
    n -= 9

    while True:
        digit_order += 1
        # handle case of double digits and further
        total_digit_count = digit_order * 9 * 10**(digit_order-1)
        if n <= total_digit_count:
            last_num = n // digit_order
            sum += sumOfDigits(last_num, a)

if __name__ == '__main__':
    "Not the correct solution yet"
    d = 16 # since n can vary till 10**15
    a = [0] * (d + 1)
    a[0] = 0
    a[1] = 45

    t = int(input())

    for i in range(2, d + 1):
        a[i] = a[i - 1] * 10 + 45 * int(math.ceil(math.pow(10, i - 1)))

    for i in range(1, t+1):
        n = int(input())

        solve(n, a)
