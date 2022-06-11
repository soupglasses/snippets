"""
# House Formatter

Example solution to a problem called House cost calculator.

Output:
```
 INITITAL HOUSE COST     ANNUAL FUEL COST      TAXES      TOTAL COST
         $175,000.00           $12,500.00    $21,875     $209,375.00
         $200,000.00           $14,000.00    $25,000     $239,000.00
         $210,000.00           $10,250.00    $21,000     $241,250.00
```
"""
import sys
from dataclasses import dataclass
from typing import Callable, TypeVar

# Input formats
INITAL_COST_FMT = "Input the initial cost of the {} house: "
ANNUAL_FUEL_COST_FMT = "What is the annual fuel cost of the {} house?: "
TAX_RATE_FMT = "Tax rate of the {} house?: "

# Table formats
DOLLAR_FMT = "${:,.2f}"
DOLLAR_ROUNDED_FMT = "${:,.0f}"
TABLE_FMT = "{init_cost:>20} {fuel_cost:>20} {taxes:>10} {total:>15}"

# Type variables
R = TypeVar("R")

# Data classes
@dataclass
class House:
    init_cost: int
    annual_fuel_cost: int
    tax_rate: float


@dataclass
class Bill:
    init_cost: int
    fuel_cost: int
    taxes: float
    total: float


def cast_input(func: Callable[[str], R], err_text: str, input_text: str) -> R:
    while True:
        try:
            return func(input(input_text))
        except ValueError:
            print(err_text)


def int_input(input_text: str = "> ") -> int:
    return cast_input(int, err_text="Not a valid whole number!", input_text=input_text)


def float_input(input_text: str = "> ") -> float:
    return cast_input(float, err_text="Not a valid real number!", input_text=input_text)


def input_three_houses() -> list[House]:
    """
    Take an input of 3 houses with proper error handling and type casting.
    """
    houses = []
    for house_name in ("first", "second", "third"):
        try:
            houses.append(
                House(
                    init_cost=int_input(INITAL_COST_FMT.format(house_name)),
                    annual_fuel_cost=int_input(ANNUAL_FUEL_COST_FMT.format(house_name)),
                    tax_rate=float_input(TAX_RATE_FMT.format(house_name)),
                )
            )
        except KeyboardInterrupt:
            sys.exit(1)
        print()  #  Add some space between the sets of inputs.
    return houses


def calculate_bills(houses: list[House], *, years: int = 1) -> list[Bill]:
    """
    Calculate bills over x amount of years following problem description.

    1. Add the fuel costs for x years
    2. Calculate taxes for x years
    3. Add to total with both fuel and taxes.
    """
    bills = []
    for house in houses:
        fuel_cost = house.annual_fuel_cost * years
        taxes = house.init_cost * house.tax_rate * years
        total = house.init_cost + fuel_cost + taxes

        bills.append(Bill(house.init_cost, fuel_cost, taxes, total))
    return bills


def print_bills(bills: list[Bill]) -> None:
    """
    Print a "recipt" table following the format of the example output.
    """
    print(
        TABLE_FMT.format(
            init_cost="INITITAL HOUSE COST",
            fuel_cost="ANNUAL FUEL COST",
            taxes="TAXES",
            total="TOTAL COST",
        )
    )

    for bill in bills:
        print(
            TABLE_FMT.format(
                init_cost=DOLLAR_FMT.format(bill.init_cost),
                fuel_cost=DOLLAR_FMT.format(bill.fuel_cost),
                taxes=DOLLAR_ROUNDED_FMT.format(bill.taxes),
                total=DOLLAR_FMT.format(bill.total),
            )
        )


def main():
    example_houses = [
        House(init_cost=175_000, annual_fuel_cost=2500, tax_rate=0.025),
        House(init_cost=200_000, annual_fuel_cost=2800, tax_rate=0.025),
        House(init_cost=210_000, annual_fuel_cost=2050, tax_rate=0.020),
    ]

    # Dirty way to differenciate between taking input or using example data.
    if len(sys.argv) > 1:
        houses = input_three_houses()
    else:
        houses = example_houses

    all_bills = calculate_bills(houses, years=5)
    print_bills(all_bills)


if __name__ == "__main__":
    main()
