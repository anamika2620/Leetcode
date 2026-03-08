
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping= {"(":")", "{":"}", "[":"]"}
        if len(s)%2!=0:
            return False
        else:
            for ch in s:
                if ch=="(" or ch=="{" or ch=="[":
                    stack.append(ch)
                else:
                    if stack and ch== mapping[stack[-1]]:
                        stack.pop()
                    else:
                        return False
        if len(stack)==0:
            return True
        else:
            return False
                
