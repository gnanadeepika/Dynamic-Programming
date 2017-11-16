str1='sunday'
str2='saturday'

ed=[[None]*(len(str1)+1) for i in range(len(str2)+1)]

for i in range(len(str2)+1):
    for j in range(len(str1)+1):
        if i==0:
            ed[i][j]=j
        elif j==0:
            ed[i][j]=i
        else:
            if str1[j-1]==str2[i-1]:
                ed[i][j]=ed[i-1][j-1]
            else:
                ed[i][j]=min(ed[i-1][j],ed[i][j-1],ed[i-1][j-1])+1



for i in ed:
    print(i)