import pathlib


def main():
    with open(pathlib.Path(__file__, '..', 'input.txt').resolve()) as f:
        lines = f.readlines()

    i = 0
    x = 1
    total = 0
    is_right_moment = 20

    rows = []
    row = []

    def addRow(row: list[str]) -> list[str]:

        pixel_position = len(row)
        if pixel_position in range(x - 1, x + 2):
            row.append('#')
        else:
            row.append('.')

        if len(row) == 40:
            rows.append(row)
            return []

        return row

    for line in lines:

        if line.strip() == 'noop':
            i += 1
            if i % is_right_moment == 0:
                total += i * x
                is_right_moment += 40
            row = addRow(row)
        else:
            to_add = int(line.split()[1])

            for _ in range(2):
                i += 1
                if i % is_right_moment == 0:
                    total += i * x
                    is_right_moment += 40
                row = addRow(row)
            x += to_add

    for row in rows:
        print(f'{"".join(row)}')
    print()

    return total, 'BGKAEREZ'


if __name__ == "__main__":
    print(f"Result: {main()}")
