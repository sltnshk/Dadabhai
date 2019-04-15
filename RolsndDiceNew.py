


def my_function():
    count = 0
    start = int(input("play your dice"))
    if start == 6:
        print("play Again")
        my_function()
    elif start == 1:
        count = count + 1
        return count
        my_function()
        print(count)
    elif start == 2:
        count += 1
        return count
        my_function()
        print(count)
    elif start == 3:
        count += 1
        my_function()
        print(count)
    elif start == 4:
        count += 1
        my_function()
        print(count)
    elif start == 5:
        count += 1
        my_function()
        print(count)
    elif start == 7:
        count += 1
        my_function()
        print(count)
    elif start == 8:
        count += 1
        my_function()
        print(count)
    elif start == 11:
        count += 1
        my_function()
        print(count)
    else:
        print("invalid")
        print(count)
my_function()