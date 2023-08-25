a = []
not_stop_input = True
while not_stop_input:
    i = int(input("Enter an integer number (0 to stop) :- "))
    if i == 0:
        not_stop_input = False
    else:
        a.append(i)

print(f"The sum of your entered input is {sum(a)} and average is {sum(a)/len(a)}")
