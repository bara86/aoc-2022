import pathlib
import string


def main():
    with open(pathlib.Path(__file__, '..', 'input.txt')) as f:
        lines = [l.strip() for l in f]

    priorities = {c: i + 1 for i, c in enumerate(string.ascii_lowercase + string.ascii_uppercase)}

    tot_first_part = 0
    for line in lines:
        line_len = len(line)
        first_part = set(line[:line_len // 2])
        second_part = set(line[line_len // 2:])

        tot_first_part += priorities[next(iter(first_part.intersection(second_part)))]

    tot_second_part = 0
    for first, second, third in zip(lines[::3], lines[1::3], lines[2::3]):
        tot_second_part += priorities[next(iter(set(first).intersection(set(second).intersection(set(third)))))]

    return tot_first_part, tot_second_part


if __name__ == "__main__":
    print(f"Result: {main()}")
