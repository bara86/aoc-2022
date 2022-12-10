import pathlib


def main():
    with open(pathlib.Path(__file__, '..', 'input.txt').resolve()) as f:
        lines = f.readlines()

    i = 0
    x = 1
    total = 0
    is_right_moment = 20

    for line in lines:

        if line.strip() == 'noop':
            i += 1
            if i % is_right_moment == 0:
                total += i * x
                is_right_moment += 40
        else:
            to_add = int(line.split()[1])

            for _ in range(2):
                i += 1
                if i % is_right_moment == 0:
                    total += i * x
                    is_right_moment += 40
            x += to_add

    return total


if __name__ == "__main__":
    print(f"Result: {main()}")
