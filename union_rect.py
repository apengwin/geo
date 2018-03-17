# rectangle is given as tuple of bottom_left, top_right
def area_union(rects):
    bools = [False] * len(rects)
    horizontal_lines = []
    event_queue = []
    horizontal_lines = []
    sum_area = 0
    for i in range(len(rects)):
        left, bottom = rects[i][0]
        right, top = rects[i][1]
        event_queue.append((left, i, True))
        event_queue.append((right, i, False))
        horizontal_lines.append((bottom, i, True))
        horizontal_lines.append((top, i, False))

    horizontal_lines = sorted(horizontal_lines)
    event_queue.sort()

    prev_vert = 0
    i = 0
    while i < len(event_queue):
        vert_line, rect_number, start_line = event_queue[i]
        counter = 0
        for j in range(len(horizontal_lines)):
            line, index, is_start = horizontal_lines[j]
            if bools[index]:
                if is_start:
                    counter += 1
                    if counter == 1:
                        start_horizontal = line
                else:
                    counter -= 1
                    if counter == 0:
                        sum_area += (line - start_horizontal) * (vert_line - prev_vert)
        prev_vert = vert_line
        bools[rect_number] = start_line
        i += 1
    return sum_area

rects = [((-2, -1), (2,1)), ((-1, -2), (1,2)), ((300, 0), (330, 1))]

#print area_union(rects)
rects2 = [((0,0), (4, 1)), ((1, -1), (2,4)), ((0, 2), (4, 3)) ]
print area_union(rects2)

