def base_three(n):
    if(n==0):
        return 0
    a = n%3
    n=n//3
    if(a<0):
        n+=1
    base_three(n)
    if(a<0):
        print(a+(3*-1),end="")
    else:
        print(a,end="")
        
n = int(input())
base_three(n)
   
