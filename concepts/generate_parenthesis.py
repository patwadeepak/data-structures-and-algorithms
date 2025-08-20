"""
Coming back to the problem of generating all combinations of well-formed parentheses.
After going through BFS, DFS traversal techniques.
"""


"""
lets say n = 3 -
(
(), ((
()(, (((, (()
()(), (((), (()), ()((, (((), (())
()()(, ((()), (())), ()((), ((()), (())(, ()()(, ((()), (())), ()((), ((()), (()))
.... some of the combinations could go wrong and some may repeat. We will need to handle that in code.
"""

"""
This has worked pretty good. The solution is correct and working.
"""

# add 2 varieties of this
def add_2_new_variations(results, n):
    results_new = set()
    for result in results:
        opens = result.count('(')
        closes = result.count(')')
        if (opens < n):
            v1 = result + '('
            results_new.add(v1)

        if closes < n and closes < opens:
            v2 = result + ')'
            results_new.add(v2)

    return results_new

def generate_parenthesis(n):
    results = set([''])

    while len(list(results)[0]) < 2*n:
        results = add_2_new_variations(results, n)
    
    print('results\n', results)

if __name__ == '__main__':
    generate_parenthesis(3)
    