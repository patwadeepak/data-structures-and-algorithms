n = int(input())
a = list(map(int, input().split()))

b = set(range(1, n+1))

process = True
for num in a:
    if num != -1:
        if num in b:
            b.discard(num)
        else:
            print('No')
            process = False
            break

b = list(b)
if process:
    output = []
    for num in a:
        if num == -1:
            item = b.pop()
            output.append(item)
        else:
            output.append(num)
    print('Yes')
    print(*output)
