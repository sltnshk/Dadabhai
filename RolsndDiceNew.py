


def my_function():
    count = 0
    start = int(input("play your dice"))
    mylist = {}
    mylist.add((start))
    if start == 6:
        mylist.add((start))
        print("play Again")
        print(mylist)
        my_function()
    elif start == 1:
        count += 1

        print(count)
    elif start == 2:
        count += 1

        print(count)
    elif start == 3:
        count += 1

        print(count)
    elif start == 4:
        count += 1

        print(count)
    elif start == 5:
        count += 1

        print(count)
    elif start == 7:
        count += 1

        print(count)
    elif start == 8:
        count += 1

        print(count)
    else:
        print(mylist)
       # print(count)
my_function()