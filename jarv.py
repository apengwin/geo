class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def ccw(A, B, C):
    return (B.x - A.x) * (C.y - A.y) - (C.x - A.x) * (B.y - A.y) > 0

def jarvis(points):
    leftmost = points[0]
    results = []
    for i in points:
        if i.x < leftmost.x:
            leftmost = i
    pointOnHull = i
    while True:
        results.append(pointOnHull)
        candidate = points[0]
        for j in range(1, len(points)):
            if ccw(pointOnHull, candidate, points[j]):
                candidate = points[j]
        pointOnHull = candidate
        if pointOnHull == results[0]:
            return results
