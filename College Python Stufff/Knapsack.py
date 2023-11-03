def knapsack(val, wt, cap):
    index = list(range(len(val)))
    ratio = [v / w for v, w in zip(val, wt)]
    index.sort(key=lambda i: ratio[i], reverse=True)
    max_val = 0
    fraction = [0] * len(val)
    for i in index:
        if wt[i] <= cap:
            max_val += val[i]
            cap -= wt[i]
        else:
            max_val += val[i] * cap / wt[i]
            break

    return max_val, fraction


n = int(input("Enter Number of items :- "))
profit = input(f'Enter the profits of the {n} item(s) in order: ').split()
profit = [int(v) for v in profit]
weight = input(f'Enter the positive weights of the {n} item(s) in order: ').split()
weight = [int(w) for w in weight]
capacity = int(input('Enter maximum weight: '))

max_value, fractions = knapsack(profit, weight, capacity)
print('The maximum value of items that can be carried:', max_value)
