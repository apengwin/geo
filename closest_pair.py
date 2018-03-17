from math import sqrt
from bisect import bisect_right, bisect_left, insort
import pdb

class Tree:
    def __init__(self):
         self.values = []

    def insert(self, val):
        insort(self.values, val)

    def delete(self, val):
        index = bisect_left(self.values, val)
        if index < len(self.values) and self.values[index] == val:
            self.values.pop(index)
    def range_query(self, left, right):
        l = bisect_left(self.values, left)
        r = bisect_right(self.values, right)
        return (l,r)
    def position(self, val):
        pos = bisect_left(self.values, val)
        if pos < len(self.values) and self.values[pos] == val:
            return pos
        return -1

def dist(point1, point2):
    return sqrt((point2[1] - point1[1]) * (point2[1] - point1[1]) + (point2[0] - point1[0]) * (point2[0] - point1[0]))

def closest_pair(points):
    tree = Tree()
    points.sort()
    min_so_far = float("inf")
    closest_pair = (None, None)
    tree.insert(points[0])
    for i in range(1, len(points)):
        x, y = points[i]
        l, r = tree.range_query((x - min_so_far, y - min_so_far), (x + min_so_far, y + min_so_far))
        print "{} {}".format(l, r)
        for j in range(l, r):
            if dist(tree.values[j], points[i]) < min_so_far:
                min_so_far = dist(tree.values[j], points[i])
                closest_pair = tree.values[j], points[i]
        tree.insert(points[i])
    return closest_pair

lst = [(0,0), (1,0), (1,1), (1,10), (0.2, 0.1)]
