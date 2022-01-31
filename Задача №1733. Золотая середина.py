def median(lst):

    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2
   
    if (lstLen > 1):
       #if (lstLen % 2):
            return sortedLst[index]
       # else:
           # return (sortedLst[index] + sortedLst[index + 1])/2.0
    else:
        return (lst[-1])
        
n = int(input())

s = list(map(int, input().split()))[:n]

res = []
for i in range(len(s)):
    sub = s[:i+1]
    res.append(median(sub))
    
print (*res)
