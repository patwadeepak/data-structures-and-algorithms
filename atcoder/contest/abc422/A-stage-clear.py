def solve(s: str):
  w,l  = map(int, s.split('-'))

  if l < 8:
    return f'{w}-{l+1}'
  else:
    return f'{w+1}-1'

if __name__ == '__main__':
  S = input()
  print(solve(S))
