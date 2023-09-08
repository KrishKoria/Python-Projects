test_list = [[5, 6], [4, 7, 10, 17]]

single = [(x, ) for sub in test_list for x in sub]

print(single)