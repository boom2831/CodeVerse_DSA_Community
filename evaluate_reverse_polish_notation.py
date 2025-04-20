from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                elif token == "/":
                    # Truncate division toward zero
                    result = int(a / b)

                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]

# Driver code
if __name__ == "__main__":
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    result = Solution().evalRPN(tokens)
    print("Result:", result)
