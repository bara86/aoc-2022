import pathlib


def main():
    with open(pathlib.Path(__file__, '..', 'input.txt')) as f:
        chars = f.read().strip()

    res_part_1 = res_part_2 = None
    for i in range(len(chars)):
        if res_part_1 is None and len(set(chars[i: i + 4])) == 4:
            res_part_1 = i + 4
        if res_part_2 is None and len(set(chars[i: i + 14])) == 14:
            res_part_2 = i + 14

        if res_part_1 is not None and res_part_2 is not None:
            break

    return res_part_1, res_part_2


if __name__ == "__main__":
    print(f"Result: {main()}")
