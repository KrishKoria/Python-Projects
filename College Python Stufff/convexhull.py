import random as rd


class ConvexHull:
    def __init__(self, pts):
        self.pts = pts
        self.hull = self.compute_convex_hull()

    @staticmethod
    def get_cross_product(p1, p2, p3):
        return ((p2[0] - p1[0]) * (p3[1] - p1[1])) - ((p2[1] - p1[1]) * (p3[0] - p1[0]))

    def compute_convex_hull(self):
        hull = []
        self.pts.sort(key=lambda x: [x[0], x[1]])
        start = self.pts.pop(0)
        hull.append(start)
        self.pts.sort(key=lambda p: (-p[1], p[0]))
        for pt in self.pts:
            hull.append(pt)
            while len(hull) > 2 and self.get_cross_product(hull[-3], hull[-2], hull[-1]) < 0:
                hull.pop(-2)
        return hull


points = [(rd.randint(0, 100), rd.randint(0, 100)) for _ in range(10)]

convex = ConvexHull(points)
print(convex.hull)
