from collections import Counter
s = input()
c = Counter(s)
keys = list(c.keys())
if c[keys[0]] > c[keys[1]]:
	print(keys[1])
else:
	print(keys[0])