class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
        
        return not stack

if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        "()", 
        "()[]{}", 
        "(]", 
        "([])", 
    ]
    
    for s in test_cases:
        result = sol.isValid(s)
        print(f"Input: {s} => Output: {result}")
