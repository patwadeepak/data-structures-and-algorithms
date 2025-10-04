# O S L
m = { 'O': 1, 'S': 2, 'L': 3}
a, b = input().split()
if m[a[0]] >= m[b[0]]:
	print('Yes')
else:
	print('No')