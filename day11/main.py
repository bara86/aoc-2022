import pathlib
import typing


class NewMonkey(typing.NamedTuple):
    monkey_id: int
    item_value: int


class Operation:
    _value: typing.Optional[int]

    def __init__(self, value: str) -> None:
        if value == "old":
            self._value = None
        else:
            self._value = int(value)

    def __call__(self, old: int) -> int:
        return self._do(old)

    def _do(self, old: int) -> int:
        raise NotImplementedError


class Sum(Operation):

    def _do(self, old) -> int:
        return old + self._value


class Multiply(Operation):

    def _do(self, old: int) -> int:
        if self._value is None:
            return old * old
        return old * self._value


class Monkey:
    def __init__(self, init_values: list[str]) -> None:
        self._id = int(init_values[0].split()[1][:-1])
        self._items: list[int] = list(map(int, init_values[1].strip()[len('starting items:'):].split(', ')))
        self._operation: Operation = self.__createOperation(init_values[2])
        self._divisible_by: int = int(init_values[3].split()[-1])
        self._if_true_throw_to: int = int(init_values[4].split()[-1])
        self._if_false_throw_to: int = int(init_values[5].split()[-1])

        self._inspected = 0
        self._initial_items = list(self._items)

    def reset(self):
        self._inspected = 0
        self._items = list(self._initial_items)

    @staticmethod
    def __createOperation(line: str) -> Operation:
        v = line[len('Operation: new = '):]
        value = v.split()[-1]
        if '+' in v:
            return Sum(value=value)
        return Multiply(value=value)

    def __repr__(self) -> str:
        return f"Monkey {self._id}: items {self._items}"

    def inspectItems(self, i_feel_fine=False) -> list[NewMonkey]:
        new_values: list[NewMonkey] = []

        divisor = 1 if i_feel_fine else 3

        for old_value in self._items:
            self._inspected += 1
            new_value = self._operation(old_value) // divisor
            if not (new_value % self._divisible_by):
                new_values.append(NewMonkey(self._if_true_throw_to, new_value))
            else:
                new_values.append(NewMonkey(self._if_false_throw_to, new_value))

        self._items = []

        return new_values

    def addItem(self, new_item: int) -> None:
        self._items.append(new_item)

    def totalInspected(self) -> tuple[int, int]:
        return self._id, self._inspected


def main():
    monkeys: list[Monkey] = []

    with open(pathlib.Path(__file__, '..', 'input.txt').resolve()) as f:
        init_values: list[str] = []
        for line in f:
            if not line.strip():
                monkeys.append(Monkey(init_values))
                init_values = []
            else:
                init_values.append(line.strip())
        monkeys.append(Monkey(init_values))

    all_divisible = 1
    for monkey in monkeys:
        all_divisible *= monkey._divisible_by

    for i in range(20):

        for monkey in monkeys:
            for item in monkey.inspectItems():
                monkeys[item.monkey_id].addItem(item.item_value)

    more_inspected_step1 = sorted([monkey.totalInspected() for monkey in monkeys], key=lambda x: x[1], reverse=True)[:2]

    for monkey in monkeys:
        monkey.reset()

    for i in range(10000):

        for monkey in monkeys:
            for item in monkey.inspectItems(i_feel_fine=True):
                value = item.item_value % all_divisible
                if value == 0:
                    value = all_divisible
                monkeys[item.monkey_id].addItem(value)

    more_inspected_step2 = sorted([monkey.totalInspected() for monkey in monkeys], key=lambda x: x[1], reverse=True)[:2]

    return more_inspected_step1[0][1] * more_inspected_step1[1][1], more_inspected_step2[0][1] * more_inspected_step2[1][1]


if __name__ == "__main__":
    print(f"Result: {main()}")
