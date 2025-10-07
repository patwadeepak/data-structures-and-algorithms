import io
from contextlib import redirect_stdout

"""
Not Part of the solution
"""
def walk(grid, start):
    n = len(grid)
    vis = [[False]*n for _ in range(n)]
    x, y = start
    pos = [x, y]
    cycle = False
    while (pos[0] < n and pos[0] >= 0) and (pos[1] < n and pos[1] >= 0):
        cell = grid[pos[0]][pos[1]]

        if not vis[pos[0]][pos[1]]:
            vis[pos[0]][pos[1]] = True
        else:
            cycle = True
            break

        if cell == 'U':
            pos[0] -= 1
        elif cell == 'L':
            pos[1] -= 1
        elif cell == 'R':
            pos[1] += 1
        else:
            pos[0] += 1
    
    return not cycle

"""
Not Part of the solution
"""
def test_case_generator(p):
    for i in range(p):
        # ith test case
        # Use redirect_stdout to temporarily redirect sys.stdout to the buffer
        n = i+2
        for k in range(4*n):
            # Create a StringIO object to act as a buffer for the output
            output_buffer = io.StringIO()
            with redirect_stdout(output_buffer):
                solve(n, k)

            # After the 'with' block, sys.stdout is restored to its original state.
            # You can now get the captured output from the buffer.
            captured_output = output_buffer.getvalue()

            solution = captured_output.splitlines()
            if solution[0] == 'YES':
                grid = solution[1:]
                outs = 0
                for i in range(n):
                    for j in range(n):
                        if i == 0 or i == n-1 or j == 0 or j == n-1:
                            got_out = walk(grid, (i,j))
                            if got_out:
                                outs += 1
                if outs == k:
                    # print(n, k, 'PERFECT')
                    pass
                else:
                    print(n, k, 'WRONG')
            elif solution[0] == 'NO':
                if k > (4*n - 4):
                    print(n, k, 'NO', 'ok')
                else:
                    print(n, k, 'NOOO', 'Check this case')

"""
Only code below this comment is suppose to be submitted
"""
def solve(n, k):
    # edge cell count
    edge_cells = 4*(n-1)

    if n == 2 and k == 3:
        print('NO')
        return

    if k > edge_cells:
        print('NO')
        return
    
    print('YES')
    if k == edge_cells:
        print('U'*n)
        for _ in range(n-2):
            print('L'+'U'*(n-2)+'R')
        print('D'*n)
        return
 
    if k >= n:
        print('U'*n)
        k -= n
    else:
        print(('U'*k) + 'D'*(n-k))
        k = 0

    for _ in range(n-2):
        s = ''
        if k <= 0:
            s = 'R'+'L'*(n-1)
        elif k > 0:
            s += 'L'
            k -= 1

            if (n-3) > 0:
                s += 'R'+'L'*(n-3)
            else:
                s += 'D'*(n-2)

            if k > 0:
                s += 'R'
                k -= 1
            else:
                s += 'L'
                k -= 1
        print(s)
    
    if k >= n:
        print('D'*n)
        k -= n
    else:
        if k <= 0:
            print('R'+'L'*(n-1))
        else:
            if k == n-1:
                print('D'*(n-2) + 'UR')
                k = 0
            else:
                p = 'D'*k
                if n-k-1 > 0:
                    p += 'R' + 'L'*(n-k-1)
                else:
                    p += 'U' + 'L'*(n-k-1)
                print(p)
                k = 0

if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n, k = map(int, input().split())
        solve(n, k)

    # test_case_generator(50)

"""
I spent 2+ hours in contest to figure out how come such easy problem
I am not able to solve. I wanted to solve it since it was much easier
that the next C problem in the contest. but I had read the problem wrong.
I thought abraham would enter the maze from one of the edges. But in problem
he can start by appearing anywhere within the maze :(
"""
