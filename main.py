from argparse import ArgumentParser

from day1.main import main as main_day1
from day2.main import main as main_day2
from day3.main import main as main_day3
from day4.main import main as main_day4
from day5.main import main as main_day5


def main():
    arg_parser = ArgumentParser()
    arg_parser.add_argument('--day-to-run', '-d', type=int, required=False)

    args = arg_parser.parse_args()

    def runDay(day: int) -> bool:
        try:
            main_day = globals()[f"main_day{day}"]
            res = main_day()
            print('*' * 40, f'Day {day}', '*' * 40)
            print(" " * 20, f"Part 1: {res[0]}")
            print(" " * 20, f"Part 2: {res[1]}")
            print('*' * 87)
        except KeyError:
            return False
        else:
            return True

    if (day := getattr(args, 'day_to_run')) is None:
        for i in range(1, 26):
            if not runDay(i):
                break
    else:
        runDay(day)


if __name__ == "__main__":
    main()
