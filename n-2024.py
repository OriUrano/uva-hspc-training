from collections import deque

def is_blocking(p1, p2, p3): 
    x1, y1 = p1 # Start
    x2, y2 = p2 # End
    x3, y3 = p3 # Is Blocking

    slope1 = (y2 - y1) * (x3 - x2)
    slope2 = (y3 - y2) * (x2 - x1)
    if slope1 != slope2:
        return False

    if x1 != x2:
        return min(x1, x2) <= x3 <= max(x1, x2)
    else:
        return min(y1, y2) <= y3 <= max(y1, y2)

def solve():
    n = int(input())
    points = []
    for _ in range(n):
        points.append(tuple(map(int, input().split()))) # tuple due to not needing to modify the points

    start = points[0] # (0,0)
    end = points[1] # (2020, 0)

    q = deque([(start, [start])])  # (current_point, path_so_far)
    visited = {start}

    while q:
        current_point, path = q.popleft()

        if current_point == end:
            print(len(path))
            for p in path:
                print(p[0], p[1]) # x, y
            return

        for next_point in points:
            if next_point != current_point and next_point not in visited:
                valid_move = True
                for other_point in points:
                    if other_point != current_point and other_point != next_point:
                        if is_blocking(current_point, next_point, other_point):
                            valid_move = False
                            break
                if valid_move:
                    visited.add(next_point)
                    q.append((next_point, path + [next_point]))
solve() 