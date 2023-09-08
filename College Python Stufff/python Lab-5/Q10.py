test_list = [(15, 6), (16, 7), (16, 8), (16, 10), (17, 13)]

print("The original list is : " + str(test_list))
temp_dict = {}
for x in test_list:
    temp_dict[x[0]] = temp_dict.get(x[0], []) + list(x[1:])

res = [(k,) + tuple(v) for k, v in temp_dict.items()]

print("The extracted elements : " + str(res))
