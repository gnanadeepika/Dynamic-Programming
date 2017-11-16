sum=10
coins=[2,3,5,6]

ccl=[[None]*(sum+1) for i in coins]

for i in range(len(coins)):
    for j in range(sum+1):
        if j==0:
            ccl[i][j]=1
        elif i==0:
            if j%coins[i]==0:
                ccl[i][j]=1
            else:
                ccl[i][j]=0
        else:
            if j<coins[i]:
                ccl[i][j]=ccl[i-1][j]
            else:
                ccl[i][j]=ccl[i-1][j]+ccl[i][j-(coins[i])]



for i in ccl:
    print(i)