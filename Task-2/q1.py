def Multiply(A,B):
    m=len(A)
    n=len(A[0])
    p=len(B)
    q=len(B[0])

    if n!=p:
        return 0
    C=[]
    
    for i in range(0,m):
        r=[]
        for j in range(0,q):
            s=0
            for k in range(0,n):
                s+=A[i][k]*B[k][j]
            r.append(s)
        C.append(r)
    return C

matA=[
    [1,2,3],
    [3,4,3]
]
matB=[
    [1,1],
    [3,4]
]
matC=Multiply(matA,matB)

print(matC or "not multipliable")