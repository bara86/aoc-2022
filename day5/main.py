import pathlib


def main():
    stacks = [
        list('BVSNTCHQ'),
        list('WDBG'),
        list('FWRTSQB'),
        list('LGWSZJDN'),
        list('MPDVF'),
        list('FWJ'),
        list('LNQBJV'),
        list('GTRCJQSN'),
        list('JSQCWDM'),
    ]

    stacks_part_2: list[list[str]] = list(list(stack) for stack in stacks)

    with open(pathlib.Path(__file__, '..', 'input.txt')) as f:
        moves = f.readlines()

    for move in moves:
        qta, from_, to = map(int, move.split(' ')[1::2])
        stacks[to - 1].extend(stacks[from_ - 1].pop() for _ in range(qta))
        stacks_part_2[to - 1] = stacks_part_2[to - 1] + stacks_part_2[from_ - 1][-qta:]
        stacks_part_2[from_ - 1] = stacks_part_2[from_ - 1][:-qta]

    result_part_1 = ''.join(stack[-1] for stack in stacks)
    result_part_2 = ''.join(stack[-1] for stack in stacks_part_2)
    return result_part_1, result_part_2


if __name__ == "__main__":
    print(f'Result: {main()}')
