import collections

random_list = ['A', 'A', 'B', 'C', 'B', 'D', 'D', 'A', 'B']

frequency = collections.Counter(random_list)

print(dict(frequency))
