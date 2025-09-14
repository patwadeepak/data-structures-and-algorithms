def solve(n, r, l):
    ops = 0
    # find first unlocked door from left
    first_left_unlocked_door = None
    for i, door in enumerate(l):
        if door == 0:
            first_left_unlocked_door = i
            break
    
    if first_left_unlocked_door is None:
        return 0

    # go till that door and keep unlocking on the way
    if first_left_unlocked_door < r:
        doors_unlocked = sum(l[first_left_unlocked_door:r])
        ops += doors_unlocked

        # then lock that door keep locking all door till you reach your start position 
        ops += r-first_left_unlocked_door

    # first first unlocked door from right
    first_right_unlocked_door = None
    for i, door in enumerate(l):
        i = len(l)-i-1
        if l[i] == 0:
            first_right_unlocked_door = i
            break

    if first_right_unlocked_door is None:
        return 0
    # go till that unlocked door and keep locking on the way previous doors and keep unlocking till we reach the last unlocked door
    if r <= first_right_unlocked_door:
        doors_locked = sum(l[r:first_right_unlocked_door])
        ops += doors_locked

        # lock the first unlocked door
        ops += 1
        # then lock that door keep locking all door till you reach your start position 
        ops += first_right_unlocked_door-r
    
    return ops

if __name__ == '__main__':
    n, r = list(map(int, input().split(' ')))
    l = list(map(int, input().split(' ')))
    print(solve(n, r, l))
