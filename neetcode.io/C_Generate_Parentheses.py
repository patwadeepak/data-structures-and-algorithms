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
