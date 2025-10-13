def solve(n, a):
  dec = 1 
  ne = 2
  arr = [1]
  s = 1
  for i in range(1, n):
    arr_len = len(arr)
    value_for_different_element = arr_len*ne + arr_len+1 - s
    if a[i] == value_for_different_element:
      dec += 1
      arr.append(ne)
      s += ne
      ne += 1
    else:
      value = arr[value_for_different_element - a[i] - 1]
      arr.append(value)
      s += value
  return arr

if __name__=='__main__':
  t = int(input())
  while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    print(*solve(n, a))
    t -= 1
