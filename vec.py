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

def get_standard_form(line)
  point1, point2 = line
  A = point2[1] - point1[1]
  B = -1 * (point2[0] - point1[0])
  C = A * point1[0] + B * point1[1]
  return (A,B,C)

def find_intersection(line1, line2):
  if line_line_intersect(line1, line2):
    A_1, B_1, C_1 = get_standard_form(line1)
    A_2, B_2, C_2 = get_standard_form(line2)

    # cramer's rule
    det = A_1 * B_2 - A_2 * B_1
    if det == 0:
      return None
    else:
      return (float(C_1 * B_2 - B_1 * C_2) / det, float(A_1 * C_2 - C_1 * A_2) / det)
  else:
    return None

# return a center point and radius, so (tuple, float)
def circle(point1, point2, point3):
  A_1, B_1, _ = get_standard_form((point1, point2))
  mid_x_1, mid_y_1 = (float(point2[0] + point1[0]) / 2, \
       float(point2[1] + point1[1]) / 2)

  orthog_line_1 = (-1 * B_1, A_1)

  D_1 = orthog_line_1[0] * mid_x_1 + orthog_line_1[1] * mid_y_1

  A_2, B_2, _ = get_standard_form((point2, point3))

  mid_x_2, mid_y_2 = (float(point2[0] + point3[0]) / 2, \
       float(point2[1] + point3[1]) / 2)

  orthog_line_2 = (-1 * B_2, A_2)

  D_2 = orthog_line_2[0] * mid_x_2 + orthog_line_2[1] * mid_y_2

  # we now have two lines. -B_1x + A_1y = D, -B_2x + A_2y = D
  det = orthog_line_1[0] * orthog_line_2[1] - orthog_line_2[0] * orthog_line_1[1]
  center_x = float(D_1 * orthog_line_2[1] - D_2 * orthog_line_1[1]) / det
  center_y = float(orthog_line_1[0] * D_2 - orthog_line_2[0] * D_1) / det
  center = (center_x, center_y)

  return (center, dist(center, (mid_x_1, mid_y_1)))


