class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == "{":
                stack.append("}")
            elif c == "(":
                stack.append(")")
            elif c == "[":
                stack.append("]")
            elif not stack:
                return False
            elif stack.pop() != c:
                return False
        if not stack:
            return True
        return False
