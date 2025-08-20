"""
Generate Parentheses
https://neetcode.io/problems/generate-parentheses?list=neetcode150

You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

Example 1:

Input: n = 1

Output: ["()"]
Example 2:

Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]
You may return the answer in any order.
"""

from typing import List


class Solution:
    """
    NOT A SOLUTION.
    A pathetic attempt to generate parentheses combinations with
    no regard for the actual problem requirements or
    any tact for algorithmic efficiency or technique.
    Yes, I am a very hard critique of my own code & skills.
    """
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        for i in range(2*n):
            if i == 0:
                output.append('(')
                continue

            for item in output:
                old = output.pop()
    
                output.append(old+')')
    
                if len(output[-1]) < 2*n:
                    output.append(old+'(')
        
        return output


class Solution1:
    """
    A perfect solution that uses backtracking to generate all combinations of well-formed parentheses.
    """
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res


class Solution2:
    """
    Fully original solution from scratch.
    Has 2 flaws in efficiency -
        1. It generates all combinations of parentheses without checking if they are valid and needs result.count() to check validity.
        2. It uses a set to store results, which is not necessary and adds overhead.
    However, it does generate all valid combinations of parentheses.
    """
    def generateParenthesis(self, n: int) -> List[str]:
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

        results = set([''])

        while len(list(results)[0]) < 2*n:
            results = add_2_new_variations(results, n)

        return list(results)


if __name__ == "__main__":
    n = 3
    solution = Solution1()
    solutionSet = set(["((()))","(()())","(())()","()(())","()()()"])
    solution1 = set(solution.generateParenthesis(n))
    print(solution1)

    if solution1 == solutionSet:
        print("Solution1 is correct.")
    else:
        print("Solution1 is incorrect.")
