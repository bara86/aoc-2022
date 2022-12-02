from pathlib import Path
from enum import IntEnum, auto

POINTS_FOR_WIN = 6
POINTS_FOR_DRAW = 3
POINTS_FOR_LOST = 0


class MyShapes(IntEnum):
    X = auto()  # rock
    Y = auto()  # paper
    Z = auto()  # scissor


class OpponentShapes(IntEnum):
    A = MyShapes.X  # rock
    B = MyShapes.Y  # paper
    C = MyShapes.Z  # scissor


class FinishStatus(IntEnum):
    Z = POINTS_FOR_WIN  # win
    Y = POINTS_FOR_DRAW  # draw
    X = POINTS_FOR_LOST  # lost


def main():
    with open(Path(__file__, '..', 'input.txt'), 'r') as f:
        moves = f.readlines()

    wins_with = {MyShapes(i): OpponentShapes(((i + 1) % 3) + 1) for i in range(1, 4)}
    lost_with = {v: k for k, v in wins_with.items()}

    # Part 1
    score_part_1 = 0
    for play in moves:
        opponent_shape, my_shape = (getattr(shape, v) for shape, v in zip((OpponentShapes, MyShapes), play.split()))

        if opponent_shape == my_shape:
            score_for_round = POINTS_FOR_DRAW
        elif wins_with[my_shape] == opponent_shape:
            score_for_round = POINTS_FOR_WIN
        else:
            score_for_round = POINTS_FOR_LOST

        score_part_1 += score_for_round + int(my_shape)

    # Part 2
    score_part_2 = 0
    for play in moves:
        opponent_shape, result = (getattr(shape, v) for shape, v in zip((OpponentShapes, FinishStatus), play.split()))
        match result:
            case FinishStatus.X:
                my_move = MyShapes(wins_with[MyShapes(opponent_shape)])
            case FinishStatus.Z:
                my_move = MyShapes(lost_with[opponent_shape])
            case FinishStatus.Y:
                my_move = MyShapes(opponent_shape)
            case _:
                raise Exception
        score_part_2 += int(my_move) + int(result)

    return score_part_1, score_part_2


if __name__ == "__main__":
    print(f"Result: {main()}")
