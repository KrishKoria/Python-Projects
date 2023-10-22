def perfectNum(stop):
    sum_num = 0
    mylist = []
    for i in range(1, stop):
        if stop % i == 0:
            sum_num += i
        if stop == sum_num:
            mylist.append(sum_num)
    return mylist


for items in perfectNum(5000):
    print(items)
