matrix=[[1,2,3],[4, 8,2],[1,5,3]]

temp=[[None]*len(matrix[0]) for i in range(len(matrix))]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i ==0 and j==0:
            temp[i][j]=matrix[i][j]
        elif i==0 and j>0:
            temp[i][j]=temp[i][j-1]+matrix[i][j]
        elif j==0 and i>0:
            temp[i][j]=temp[i-1][j]+matrix[i][j]
        else:
            temp[i][j]=min(temp[i-1][j-1],temp[i][j-1],temp[i-1][j])+matrix[i][j]


for x in temp:
    print(x)