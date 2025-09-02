memo = set()

def solve(s, n):
    if s in memo:
        return
    if n == 0:
        return
    if n == 1:
        memo.add(s)
        return

    memo.add(s)

    s1 = s[1:]
    s2 = ''.join([s[0], s[2:]])

    if s1 not in memo:
        solve(s1, n-1)

    if s2 not in memo and s1 != s2:
        solve(s2, n-1)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        try:
            memo = set()
            n = int(input())
            s = input()
            solve(s, n)
            print(len(memo))
        except Exception as e:
            print(e)

"""
Solution logic is correct but Not AC
as the there are test cases with N=1000_000 string length
and causing recursion limit hits.
"""
