from dataclasses import dataclass


@dataclass
class Item:
    name: str
    category: str
    price: float
    quantity: int


ITEMS = [
    Item("screwdriver", "tools", 25.0, 4),
    Item("drill", "tools", 320.0, 1),
    Item("tape", "supplies", 6.5, 0),
    Item("sandpaper", "supplies", 2.0, 30),
]


def total_value(items: list[Item]) -> float:
    return sum(item.price * item.quantity for item in items)


def report(items: list[Item]) -> None:
    for item in items:
        print(f"{item.name}\t{item.category}\t{item.price}\t{item.quantity}")
    print(f"total\t{total_value(items)}")


if __name__ == "__main__":
    report(ITEMS)
