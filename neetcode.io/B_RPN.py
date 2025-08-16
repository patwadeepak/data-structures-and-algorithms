# RPN stands for Reverse Polish Notation.
# It is a mathematical notation in which every operator follows all of its operands.
# For example, the expression "3 + 4" would be written as "3 4 +" in RPN.

class Solution1:
    """
    ***NOT A SOLUTION***
    This class fails to solve the problem correctly because it does not
    consider the case like ["1","2", "3", "+", "*"].

    Classic falling for the simple example trap,
    """
    def evalRPN(self, tokens):
        first_value = int(tokens[0])

        looped_tokens = tokens[1:][::-1]

        while len(looped_tokens) > 0:
            second_value = int(looped_tokens.pop())
            operation = looped_tokens.pop()
    
            if operation == '+':
                first_value  = first_value + second_value
            elif operation == '*':
                first_value = first_value * second_value
            elif operation == '-':
                first_value = first_value - second_value
            elif operation == '+':
                first_value = first_value + second_value
            
        return first_value

class Solution2:
    """
    VERY CLOSE TO A SOLUTION. But Still INCORRECT.
    This class solves the problem correctly by using a stack to evaluate the RPN expression.
    It processes each token, pushing numbers onto the stack and applying operations when operators are encountered.

    Fails for cases like ["1","2","+","3","*","4","-"]
    """
    def evalRPN(self, tokens):

        stack = []
        
        i = 0
        while i < len(tokens):
            item = tokens[i]

            if len(stack) < 2 or item not in '+-*/':
                stack.append(int(item)) 
            else:
                operation = item
                first_value = stack.pop()
                second_value = stack.pop()
                if operation == '+':
                    result = first_value + second_value
                elif operation == '*':
                    result = first_value * second_value
                elif operation == '-':
                    result = first_value - second_value
                elif operation == '/':
                    result = first_value // second_value
                
                stack.append(result)
            i += 1
                    
        return stack[0]