# C2. The Cunning Seller (hard version)

def decimal_to_arbitrary_base(decimal_num, base):
    digits = [0, 1, 2]
    result = []
    current_num = decimal_num

    min_deals = 0
    while current_num > 0:
        remainder = current_num % base
        result.append(digits[remainder])
        current_num //= base
        min_deals += result[-1]

    return result[::-1], min_deals


def solve(n, k):
    output, min_deals = decimal_to_arbitrary_base(n, 3)
    cost = 0

    if min_deals > k:
        print(-1)
        return

    k -= min_deals
    for x, ch in enumerate(output):
        if x < len(output) - 1 and output[x] > 0:
            if output[x] <= k/2:
                max_removal = output[x]
            else:
                max_removal = k//2

            increase_in_min_deals = max_removal*2
            increase_in_next_power_deals = max_removal*3
            output[x] -= max_removal
            min_deals += increase_in_min_deals
            output[x+1] += increase_in_next_power_deals
            k -= increase_in_min_deals

        y = len(output) - x - 1
        three_x = 3**y
        cost += ((three_x*3) + (y*three_x/3))*output[x]

    print(int(cost))


if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, k = tuple(map(int, input().split(' ')))

        solve(n, k)
