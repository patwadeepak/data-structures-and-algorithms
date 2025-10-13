def solve(n):
  if n == 0 or n == 1:
    return 'YES'
  s = bin(n)[2:]
  s = s.rstrip('0')
  if s == s[::-1] and len(s) > 1:
    if len(s)%2 == 1:
      if s[len(s)//2] == '0':
        return 'YES'
      else:
        return 'NO'
    return 'YES'
  else:
    return 'NO'

if __name__=='__main__':
  t = int(input())
  while t > 0:
    n = int(input())
    print(solve(n))
    t -= 1

"""
Not a Solution. WA in contest
"""