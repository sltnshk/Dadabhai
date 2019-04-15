


def my_function():
    count = 0
    start = int(input("play your dice"))
    list = set(1,2,3,4,5,6,7,8,9,10)
    if ((start == 6) or (start >= 11)):
        #print("play again")
        my_function()
    elif start == list:
        count += 1
        return count
        print(count)
        my_function()


my_function()