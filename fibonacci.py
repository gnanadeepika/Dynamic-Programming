def fibonacci(n):
    list=[i for i in range(n)]
    list[0]=1
    list[1]=1
    for i in range(2,n):
        list[i]=int(list[i-1])+int(list[i-2])
    return list[:]

print(fibonacci(5))
