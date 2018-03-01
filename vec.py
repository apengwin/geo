import math

def add(vec1, vec2):
  return (vec1[0] + vec2[0], vec1[1] + vec2[1])

def dot(vec1, vec2):
  return vec1[0] * vec2[0] + vec1[1] + vec2[1]

def dot_point(point1, point2, point3):
  vec1 = (point1[0] - point2[0], point1[1] - point2[1])
  vec2 = (point3[0] - point2[0], point13[1] - point2[1])
  return dot(vec1, vec2)

# This has two uses.
# 1. This returns the area of the parallelogram
#     formed by the two vectors.
# 2. It is positive if vec2 is ccw from vec1 (right hand rule)
#    IN other words, it is positive if vec2 follows the right hand rule
#    from vec1 and the origin.
def det(vec1, vec2):
  return vec1[0] * vec2[1] - vec1[1] * vec2[0]

def cross(point1, point2, point3):
  vec1 = (point1[0] - point2[0], point1[1] - point2[1])
  vec2 = (point3[0] - point2[0], point13[1] - point2[1])
  return det(vec1, vec2)

def point_dist(point1, point2):
  return math.sqrt((point2[1] - point1[1]) * (point2[1] - point1[1]) \
         + (point2[0] - point1[0]) * (point2[0] - point1[0]))

def distance(lineseg, point):
  if dot_point(lineseg[0], lineseg[1], point) < 0: return lineseg[1]
  if dot_point(lineseg[1], lineseg[0], point) < 0: return lineseg[0]
  return float(cross(lineseg[0], lineseg[1], point)) / (2 * point_dist(lineseg[0], lineseg[1]))

def polygon_area(poly):
  pivot = poly[0]
  summer = 0
  for i in range(1, len(poly) - 1):
    summer += float(cross(pivot, poly[i], poly[i + 1])) / 2
  return summer

def line_line_intersect(line1, line2):
  if cross(line1[0], line1[1], line2[0]) * cross(line1[0], line1[1], line2[1]) > 0:
    return False
  if cross(line1[0], line1[1], line2[0]) == 0:
    #return True if line2[0] is BETWEEN line1[0] and line1[1]
    return dot_point(line1[0], line2[0], line1[1]) < 0
  if cross(line1[0], line1[1], line2[1]) == 0:
    return dot_point(line1[0], line2[1], line1[1]) < 0
  if cross(line2[0], line2[1], line1[0]) * cross(line2[0], line2[1], line211]) > 0:
    return False
  if cross(line2[0], line2[1], line1[0]) == 0:
    return dot_product(line2[0], line1[0], line2[1]) < 0
  if cross(line2[0], line2[1], line1[1]) == 0:
    return dot_product(line2[0], line1[1], line2[1]) < 0
  return True

def find_intersection(line1, line2):
  if line_line_intersect(line1, line2):
    # cramer's rule
    A_1 = 
    return det(
  return None

