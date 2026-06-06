class Solution:

    def primeFactors(self, n: int):
        vf=[]
        while(n%2==0):
            n=n//2
            vf.append(2)
        
        i=3
        while i*i <= n:
            if n%i==0:
                vf.append(i)
            else:
                i=i+2
        if n>1:
            vf.append(n)
            
        for i in range(len(vf)):
            print(vf[i],end=" ")

# main
if __name__ == "__main__":
    n = int(input("Enter number: "))
    
    obj = Solution()
    obj.primeFactors(n)