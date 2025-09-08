# https://atcoder.jp/contests/abc422/editorial/13838

def main():
    """
    This solution is reverse of the operations mentioned in the problem.
    This way works even when time complexity is 2^N because N < 20 in contraint.
    """
    n, k = map(int, input().split())

    # Initialize the list with K
    ans = [k]

    # Perform the iterative division process N times
    for _ in range(n):
        nxt = []
        for a in ans:
            # Append two new values to the list: a divided by 2, and the remaining part
            nxt.append(a // 2)
            nxt.append(a - a // 2)
        ans = nxt

    # Find the maximum and minimum values in the final list
    max_val = max(ans)
    min_val = min(ans)

    # Print the difference between the maximum and minimum values
    print(max_val - min_val)

    # Print the final list of numbers
    print(*ans)

if __name__ == "__main__":
    main()