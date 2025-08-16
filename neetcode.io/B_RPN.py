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
    output should be 5 but it is -5. while storing in stack then taking values out of stack.
    We need to ensure which is the first value and which is the second value.
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


class Solution3:
    """ALSO INCORRECT, BUT CORE SOLUTION IS CORRECT.
    Ensure integer division truncates towards zero. We used // operator which truncates towards toward negative infinity.
    This is problematic for cases where one of values is negative in division operation and the question mentions to truncate towards zero.
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
                second_value = stack.pop()
                first_value = stack.pop()
                if operation == '+':
                    result = first_value + second_value
                elif operation == '*':
                    result = first_value * second_value
                elif operation == '-':
                    result = first_value - second_value
                elif operation == '/':
                    result = first_value // second_value # only line with the problem
                
                stack.append(result)
            i += 1
                    
        return stack[0]


class Solution4:
    """
    This class solves the problem correctly by using a stack to evaluate the RPN expression.
    It processes each token, pushing numbers onto the stack and applying operations when operators are encountered.
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
                second_value = stack.pop()
                first_value = stack.pop()
                if operation == '+':
                    result = first_value + second_value
                elif operation == '*':
                    result = first_value * second_value
                elif operation == '-':
                    result = first_value - second_value
                elif operation == '/':
                    result = int(float(first_value) / second_value) # Ensure integer division truncates towards zero
                
                stack.append(result)
            i += 1
                    
        return stack[0]


if __name__ == "__main__":

    tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    solution = Solution4()
    print(solution.evalRPN(tokens))
