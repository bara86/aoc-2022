import collections
import heapq
import pathlib
import string


def calculatePath(squares: list[str], initial_point: tuple[int, int], destination_point: tuple[int, int]) -> tuple[tuple[int, int]]:
    rows = len(squares)
    cols = len(squares[0])
    values = string.ascii_lowercase

    distances: dict[tuple[int, int], int] = collections.defaultdict(lambda: rows * cols + 1)
    parents = {}

    distances[initial_point] = 0
    queue: list[tuple[int, tuple[int, int]]] = [(0, initial_point)]
    visited: set[tuple[int, int]] = set()

    while queue:
        node = heapq.heappop(queue)[1]

        if node in visited:
            continue

        if node == destination_point:
            break

        for row_inc, col_inc in (0, 1), (1, 0), (-1, 0), (0, -1):
            row = node[0] + row_inc
            col = node[1] + col_inc

            if row == rows or col == cols or row == -1 or col == -1:
                continue

            def convertValue(value):
                if value == 'E':
                    value = 'z'
                if value == 'S':
                    value = 'a'
                return value

            next_height = values.index(convertValue(squares[row][col]))
            current_height = values.index(convertValue(squares[node[0]][node[1]]))
            if current_height - next_height < -1:
                continue

            new_distance = 1 + distances[node]
            if new_distance < distances[(row, col)]:
                distances[(row, col)] = new_distance
                parents[(row, col)] = node

                heapq.heappush(queue, (new_distance, (row, col)))

    nodes = tuple()
    current = destination_point
    while current in parents:
        if current == initial_point:
            break
        nodes = (current,) + nodes
        current = parents[current]

    return nodes


def main():
    with open(pathlib.Path(__file__, '..', 'input.txt').resolve()) as f:
        lines = [line.strip() for line in f]

    cols = len(lines[0])
    rows = len(lines)

    initial_point = None
    destination_point = None
    possible_initial_points = set()
    for row in range(rows):
        for col in range(cols):
            v = lines[row][col]
            if v == 'S':
                initial_point = (row, col)
                possible_initial_points.add((row, col))
            if v == 'E':
                destination_point = (row, col)
            if v == 'a':
                possible_initial_points.add((row, col))

    part_1 = calculatePath(lines, initial_point, destination_point)

    max_length = 10000000
    part_2 = None
    for possible_initial_point in possible_initial_points:
        path = calculatePath(lines, possible_initial_point, destination_point)
        if path and len(path) < max_length:
            part_2 = path
            max_length = len(path)

    return len(part_1), len(part_2)


if __name__ == "__main__":
    print(f"Result: {main()}")
