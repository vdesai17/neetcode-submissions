class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        value = 0
        ops = ("+", "-", "*", "/")

        for token in tokens:

            if token in ops:
                right_operand = stack.pop()
                left_operand = stack.pop()

                if token == "+":
                    value = left_operand + right_operand
                elif token == "-":
                    value = left_operand - right_operand
                elif token == "*":
                    value = left_operand * right_operand
                else:
                    value = int(left_operand / right_operand)
                
                stack.append(value)
                
            else:
                stack.append(int(token))
        
        return stack[-1]
                
                    