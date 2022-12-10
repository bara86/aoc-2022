from __future__ import annotations

import pathlib
from typing import NamedTuple


class Position(NamedTuple):
    x: int = 0
    y: int = 0

    def move(self, direction: str) -> Position:
        match direction:
            case 'U':
                return self._replace(y=self.y + 1)
            case 'D':
                return self._replace(y=self.y - 1)
            case 'R':
                return self._replace(x=self.x + 1)
            case 'L':
                return self._replace(x=self.x - 1)

    def onSameCol(self, other):
        return self.y == other.y

    def onSameRow(self, other):
        return self.x == other.x


def main():
    with open(pathlib.Path(__file__, '..', 'input.txt').resolve()) as f:
        moves = f.readlines()

    head_position = tail_position = Position(0, 0)
    visited_position = {tail_position}
    long_visited_position = {tail_position}
    positions: list[Position] = [head_position] * 10

    def dist(head: tuple[int, int], tail: tuple[int, int]) -> int:
        return sum(abs(h - t) for h, t in zip(head, tail))

    def areDiagonal(head: tuple[int, int], tail: tuple[int, int]) -> bool:
        return all(abs(h - t) == 1 for h, t in zip(head, tail))

    for move in moves:
        direction, counter = move.strip().split()

        for c in range(int(counter)):
            previous_head_position = head_position
            head_position = head_position.move(direction)

            if (distance := dist(head_position, tail_position)) and distance != 1 and not areDiagonal(head_position,
                                                                                                      tail_position):
                tail_position = previous_head_position
                visited_position.add(tail_position)

            positions[0] = head_position
            for i in range(1, len(positions)):
                previous, node = positions[i - 1], positions[i]

                if previous == node:
                    break

                if dist(previous, node) == 1:
                    break

                if node.onSameRow(previous):
                    if previous.y > node.y:
                        diff_y = 1
                    else:
                        diff_y = -1
                    positions[i] = node._replace(y=node.y + diff_y)
                elif node.onSameCol(previous):
                    if previous.x > node.x:
                        diff_x = 1
                    else:
                        diff_x = -1
                    positions[i] = node._replace(x=node.x + diff_x)
                elif not areDiagonal(node, previous):
                    if previous.x > node.x:
                        diff_x = 1
                    else:
                        diff_x = -1
                    if previous.y > node.y:
                        diff_y = 1
                    else:
                        diff_y = -1
                    positions[i] = node._replace(x=node.x + diff_x, y=node.y + diff_y)

            long_visited_position.add(positions[-1])

    return len(visited_position), len(long_visited_position)


if __name__ == "__main__":
    print(f"Result: {main()}")
