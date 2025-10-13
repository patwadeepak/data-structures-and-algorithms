from collections import Counter

def solve(n, a):
  f = Counter(a)
  keys = set(f.keys())

  if len(keys) == 1 and f[0] > 0:
    return 1
  
  i = 0
  while f[i] > 0:
    i += 1

  return i


if __name__=='__main__':
  t = int(input())
  while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
    t -= 1
