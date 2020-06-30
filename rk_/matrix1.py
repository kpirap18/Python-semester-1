# Матрица по спирали(по часовой, снаружи)
n = 5
L = [[0]*5 for i in range (5)]
N =5*5
k = 1
i = j = 0

while k<=N:
    L[i][j] = k
    if i<=j+1 and i+j<n-1:
        j+=1
    elif i<j and i+j>=n-1:
        i+=1
    elif i>=j and i+j>n-1:
        j-=1
    else:
        i-=1
    k+=1

for i in range(5):
    for j in range(5):
        print (L[i][j], end=' ')
    print()
