# first attempt
def minTimeToVisitAllPoints(points: list[list[int]]) -> int:
    time = 0
    for i in range(len(points) - 1):
        current_pos = points[i]
        target_pos = points[i + 1]
        while current_pos != target_pos:
            if current_pos[0] < target_pos[0]:
                current_pos[0] += 1
            elif current_pos[0] > target_pos[0]:
                current_pos[0] -= 1
            if current_pos[1] < target_pos[1]:
                current_pos[1] += 1
            elif current_pos[1] > target_pos[1]:
                current_pos[1] -= 1
            time += 1
    return time


# O(n) solution
# the min number of moves is the max diff between x's and y's between two points
def attempt_two(points: list[list[int]]) -> int:
    time = 0
    x1, y1 = points.pop()
    while points:
        x2, y2 = points.pop()
        time += max(abs(y2-y1), abs(x2-x1))
        x1, y1 = x2, y2
    return time
