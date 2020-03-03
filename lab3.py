#Ciag Fibonaciego
n = 20
n1 = 0
n2 = 1
print("Element 1:", n1)
print("Element 2:", n2)
for n0 in range(3, n+1):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print("Element %d: %d" % (n0, n3))

fibonacciIterations = 20
a1 = 0
a2 = 1
a3 = 0
for i in range(0,20):
    print('Step',i+1 ,'value',a3)
    a1=a2
    a2=a3
    a3=a1+a2
print('-------------------------------------------------')



