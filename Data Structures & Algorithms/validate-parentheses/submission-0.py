class Solution:
    def isValid(self, s: str) -> bool:

        char_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char not in char_map:
                stack.append(char)
            else:
                if stack and stack[-1] == char_map[char]:
                    stack.pop()
                else:
                    return False

        return not stack

        