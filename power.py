class Power:
    def __init__(self):
        None
    def power(self,x,n):
        ans=1
        for i in range(n):
            ans=ans*x
        print(ans)
    
result=Power()
result.power(5,3)

