import sys
n = int(input())
if n <= 2:
  print(n)
  sys.exit()

a = [0]*(n+1)
a[0] = 1
a[1] = 1

def f(x):
  ans = 0
  while x > 0:
    ans += x%10
    x = x//10
  return ans

for i in range(2, n+1):
  a[i] = a[i-1] + f(a[i-1])

print(a[n])
"""
Solved
"""