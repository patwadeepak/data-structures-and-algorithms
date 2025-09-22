from collections import defaultdict

n, m, k = map(int, input().split(' '))
ans = []
d = defaultdict(int)
for ki in range(k):
	i, q = map(int, input().split(' '))
	d[i] += 1	
	if d[i] == m:
		ans.append(i)

print(*ans)
