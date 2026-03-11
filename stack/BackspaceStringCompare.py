class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        t1=[]
        for ch in s:
            if ch!='#':
                s1.append(ch)
            elif ch=='#' and len(s1)>0:
                s1.pop()
        for ch in t:
            if ch!='#':
                t1.append(ch)
            elif ch=='#' and len(t1)>0:
                t1.pop()
        if t1== s1:
            return True
        else:
            return False

