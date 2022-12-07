import pathlib
from collections import defaultdict

TOTAL_SPACE_ON_DISK = 70000000
REQUESTED_SPACE = 30000000


def main():
    with open(pathlib.Path(__file__, '..', 'input.txt').resolve()) as f:
        lines = [line.strip() for line in f]

    sizes = defaultdict(int)

    current_path = pathlib.Path('/')

    for line in lines[1:]:
        if line.startswith('$ ls'):
            continue
        if line.startswith('$ cd'):
            change_dir_to = line[len('$ cd '):]
            current_path = (current_path / change_dir_to).resolve()
        elif not line.startswith('dir'):
            size = int(line.split()[0])
            parts = list(current_path.parts)
            for i in range(1, len(parts) + 1):
                dir_ = '/'.join(parts[:i]).replace('//', '/')
                sizes[dir_] += size

    tot_part_1 = sum(filter(lambda x: x <= 100000, sizes.values()))

    left_space = TOTAL_SPACE_ON_DISK - sizes['/']
    directory_to_be_removed = min([(k, v) for k, v in sizes.items() if v + left_space >= REQUESTED_SPACE],
                                  key=lambda x: x[1])

    return tot_part_1, directory_to_be_removed[1]


if __name__ == "__main__":
    print(f"Result: {main()}")
