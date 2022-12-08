import itertools
import pathlib


def main():
    with open(pathlib.Path(__file__, '..', 'input.txt').resolve()) as f:
        lines = [list(map(int, line.strip())) for line in f]

    for_col = [list(lines[col][row] for col in range(len(lines[0]))) for row in range(len(lines))]

    def isOnEdge(row, col):
        return row in (0, len(lines) - 1) or col in (0, len(lines[0]) - 1)

    def isVisible(e, row, col):
        if isOnEdge(row, col):
            return True

        r = for_col[col]
        return e > max(lines[row][:col]) or e > max(lines[row][col+1:]) or e > max(r[:row]) or e > max(r[row + 1:])

    def multiply(row, col):
        if isOnEdge(row, col):
            return 0

        e = lines[row][col]

        r = for_col[col]
        tot = 1
        for group in (lines[row][:col], lines[row][col+1:][::-1], r[:row], r[row + 1:][::-1]):
            for i, el in enumerate(group[::-1]):
                if el >= e:
                    tot *= (i + 1)
                    break
            else:
                tot *= len(group)

        return tot

    count = 0
    best_tot = 0
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            count += int(isVisible(lines[row][col], row, col))
            best_tot = max(best_tot, multiply(row, col))

    return count, best_tot


if __name__ == "__main__":
    print(f"Result: {main()}")
