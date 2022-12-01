from pathlib import Path


def main():
    counter: list[int] = [0]
    with open(Path(__file__, '..', 'input.txt'), 'r') as f:
        for line in f:
            if not line.strip():
                counter.append(0)
                continue
            counter[-1] += int(line)

    counter.sort(reverse=True)

    return f"the maximum is {counter[0]}", f"the sum of best 3 is {sum(counter[:3])}"


if __name__ == "__main__":
    main()
