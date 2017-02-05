class Solution(object):
    def decodeString(self, s):
        stack = []
        stack.append(["",0])
        num=""
        for ch in s:
            if ch.isdigit():
                num+=ch
            elif ch=="[":
                stack.append(["",int(num)])
                num=""
            elif ch=="]":
                cur,times=stack.pop()
                stack[-1][0]+=cur*times
            else:
                stack[-1][0]+=ch
        return stack[0][0]