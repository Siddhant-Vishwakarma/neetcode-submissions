class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for ch in s:
            if ch in '([{':
                stack.append(ch)
            
            elif ch in ')]}':
                if not stack:
                    return False
                top = stack.pop()
                if top != dict[ch]:
                    return False
        return len(stack) == 0