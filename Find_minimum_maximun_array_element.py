def getMinMax( a, n):
    min = a[0]
    max = a[1]
    for i in range(0,len(a)):
        if a[i]>max:
            max = a[i]
        elif a[i]<min:
            min = a[i]
    return min,max
  
a=[2,3,5,7,8,10]
n=6
print(getMinMax(a,n))
