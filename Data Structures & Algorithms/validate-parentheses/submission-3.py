class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if not stack or c in {'(','{','['}:
                stack.append(c)
                continue
            if stack[-1] + c in {'()','[]','{}'}:
                stack.pop()
            else:
                return False
        return not stack
        