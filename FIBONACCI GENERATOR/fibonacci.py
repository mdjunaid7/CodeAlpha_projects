#FIBONACCI GENERATOR BY RECURRENCE RELATIONSHIP.

def fibo(i):
    if i==0:
        return 0
    elif i==1:
        return 1
    else:
        return fibo(i-2) +fibo(i-1)
    
x=10
for i in range(x):
    print(fibo(i))