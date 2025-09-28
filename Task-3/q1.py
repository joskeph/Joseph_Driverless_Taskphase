# Let (x,y) represent coordinate of a point in a 2-D space. Assume that you are given a list that contains coordinates in it. Create a sort function to sort the coordinates of the based on proximity to a reference point that is not there in the input list. This reference point is to be given by the user. Output the sorted list using the sort function.
# Eg : Coordinate List : [(0,1) , (0,3) , (1,2)]
# Reference Point : (0,0)
# Output : [(0,1) , (1,2) , (0,3)]

# P(l,ref)
#l[[],[]] #ref[,]
import math

def distance(x,y,p,q):
    return math.sqrt((x-p)**2+(y-q)**2)

def Sort(l,ref):

    F=l
    n=len(F)
    X,Y=ref[0],ref[1]
    for i in range(0,n-1):
        p=i
        for j in range (i,n):
            x,y=F[j][0],F[j][1]
            a,b=F[p][0],F[p][1]
            if distance(x,y,X,Y) < distance(a,b,X,Y):
                p=j
        F[p],F[i]=F[i],F[p]


    return F

N=int(input("Enter number of elements: "))
L=[]
for i in range(N):
    t=[]
    t.append(int(input("x: ")))
    t.append(int(input("y: ")))
    print("next")
    L.append(t)
ref=[]
ref.append(int(input("Reference point X:")))
ref.append(int(input("Reference point Y:")))

print(Sort(L,ref))