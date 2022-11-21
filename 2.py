def find_occurances(s1,s2):
    s2 = s2[-1]
    count=0
    for i in s1:
        if i==s2:
            count+=1
    return count
        
s1 = input().strip()
s2 = input().strip()
print(find_occurances(s1,s2))
