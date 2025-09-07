def solve(arr, h, w):
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '#':
                count = 0

                if i+1 < h and arr[i+1][j] == '#':
                    count += 1
                if i-1 >= 0 and arr[i-1][j] == '#':
                    count += 1
                if j-1 >= 0 and arr[i][j-1] == '#':
                    count += 1
                if j+1 < w and arr[i][j+1] == '#':
                    count += 1
                
                if count != 2 and count != 4:
                    return 'No'
    return 'Yes'

if __name__ == "__main__":
    h, w = map(int, input().split(' '))
    arr = []
    for _ in range(h):
        arr.append(input())

    print(solve(arr, h, w))
