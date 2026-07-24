class Solution(object):
    def isValid(self, s):
        stack = []
        dic = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for ele in s :
            if ele not in dic:
                stack.append(ele)
            else :
                if not stack:
                    return False
                First = stack.pop()
                if First != dic[ele]:
                    return False
        return len(stack) == 0