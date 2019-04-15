#
# a = [5, 10, 15, 20, 25]
# def Prog(a):
#
#     return [a[0],a[-1]]
# Prog(a)
#
# print(a)


# def list_ends(a_list):
#     return [a_list[0], a_list[-1]]
# a_list = [1,2,3,45,5,6]
# list_ends(a_list)
#
# print(a_list)



def PrimeOrNot():
    a = int(input("Enter your number"))
    for i in range(1,a-1):
        if (a % i != 0) and (a % i == 0):
            print("not a prime")
        else:
            print("prime")
PrimeOrNot()