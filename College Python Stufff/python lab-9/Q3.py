import itertools


class Subsets:
    def __init__(self, set):
        self.set = set

    def get_subsets(self):
        subsets = []
        for i in range(len(self.set) + 1):
            for subset in itertools.combinations(self.set, i):
                subsets.append(list(subset))
        return subsets


set = {1, 2, 3}
subset = Subsets(set)
print(subset.get_subsets())
