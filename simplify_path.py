class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        stack = []

        for part in parts:
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        
        return "/" + "/".join(stack)

# Driver code
if __name__ == "__main__":
    test_paths = [
        "/home/",                       # Output: "/home"
        "/home//foo/",                 # Output: "/home/foo"
        "/home/user/Documents/../Pictures",  # Output: "/home/user/Pictures"
        "/../",                        # Output: "/"
        "/.../a/../b/c/../d/./",       # Output: "/.../b/d"
    ]
    
    solution = Solution()
    for path in test_paths:
        simplified = solution.simplifyPath(path)
        print(f"Input: {path}\nSimplified: {simplified}\n")
