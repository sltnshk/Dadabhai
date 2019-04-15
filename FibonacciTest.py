def Fib():
    y = 0
    a = int(input("input a number"))
    for x in range(1,a-1):
        y = x+y
#        x,y = x,x+y
        print(x,y)
Fib()

