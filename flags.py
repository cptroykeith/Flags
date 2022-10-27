def solution(A):
    if(len (A)<3):
        return 0
    p=[]
    for i in range(1, len(A)-1):
        if A[i]>A[i-1]and A[i]>A[i]>A[i+1]:
            p.append(i)

    if len(p)==0:
        return 0
    elif len(p)==1:
        return 1

    c=1
    m=0

    for k in range(min(len(p), int(len(A)**0.5)) +1,0,-1):
        lastF=0
        c=1
        for i in range(1,len(p)):
            if(p[i]-p[lastF]) >= k and c<k:
                c+=1
                lastF =1

        if c<m:
            return m
        elif m<c:
            m=c
    return m


