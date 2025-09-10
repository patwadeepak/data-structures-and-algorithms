from collections import Counter

def solve(a, n):
    c = Counter(a)

    misplaced = 0
    for i, ch in enumerate(a, 1):
        if ch == '1' and i <= (n-c['1']):
            misplaced += 1
    
    print(misplaced)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = input()
        solve(a, n)

"""
Although my logic was exactly what was written in editorial.
I solved this one in contest as well. But I was not confident 
about my solution for some reason. It was a happy surprise that
it passed all the pretests.

It helps when you have solved similar problems where an arrangement
was provided and you have to sort or create a new arrangement
and solution is based on how many or misplaced or how far the displacement
of each item is with their target position.
"""