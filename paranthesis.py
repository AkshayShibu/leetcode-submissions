class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=[]
        count=0
        for i in s:
            if i=='(':
                if count>0:
                    res.append(i)
                count=count+1
            else:
                count=count-1
                if count>0:
                    res.append(i)
        return "".join(res)

obj = Solution()
print(obj.removeOuterParentheses("(()())(())"))   