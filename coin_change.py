sum=6
coins=[1,2,3]

ccl=[[None]*(sum+1) for i in coins]

for i in range(len(coins)):
    for j in range(sum+1):
        if i==0 or j==0:
            ccl[i][j]=1
        else:
            if j<=i:
                ccl[i][j]=ccl[i-1][j]
            else:
                ccl[i][j]=ccl[i-1][j]+ccl[i][j-(i+1)]

for i in ccl:
    print(i)