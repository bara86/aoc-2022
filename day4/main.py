import pathlib


def main():
    with open(pathlib.Path(__file__, '..', 'input.txt'), 'r') as f:
        lines = [line.strip() for line in f]

    tot_part_1 = tot_part_2 = 0
    for line in lines:
        first_range, second_range = map(set,
                                        map(lambda interval: range(int(interval.split('-')[0]),
                                                                   int(interval.split('-')[1]) + 1), line.split(',')))
        tot_part_1 += int(not first_range - second_range or not second_range - first_range)
        tot_part_2 += int(bool(first_range & second_range))

    return tot_part_1, tot_part_2


if __name__ == "__main__":
    print(f"Result: {main()}")
