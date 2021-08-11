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
from collections import namedtuple
import sys

# Input formats
init_cost_fmt = "Input the initial cost of the {} house: "
annual_fuel_cost_fmt = "What is the annual fuel cost of the {} house?: "
tax_rate_fmt = "Tax rate of the {} house?: "

# Table formats
dollar_fmt = "${:,.2f}"
dollar_rounded_fmt = "${:,.0f}"
table_fmt = "{init_cost:>20} {fuel_cost:>20} {taxes:>10} {total:>15}"

# Data types
House = namedtuple("House", "init_cost annual_fuel_cost tax_rate")
Bill = namedtuple("Bill", "init_cost fuel_cost taxes total")
Houses = dict[str, House]
Bills = dict[str, Bill]

# Example data
example_houses = {
    "first": House(init_cost=175_000, annual_fuel_cost=2500, tax_rate=0.025),
    "second": House(init_cost=200_000, annual_fuel_cost=2800, tax_rate=0.025),
    "third": House(init_cost=210_000, annual_fuel_cost=2050, tax_rate=0.020),
}


def int_input(text="> ") -> int:
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Not a valid whole number!")
        except KeyboardInterrupt:
            sys.exit(1)


def float_input(text="> ") -> float:
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Not a valid real number!")
        except KeyboardInterrupt:
            sys.exit(1)


def input_three_houses() -> Houses:
    """
    Take in input of 3 houses with proper error handling and type casting.
    """
    houses = {}
    for house_name in ("first", "second", "third"):
        houses[house_name] = House(
            init_cost=int_input(init_cost_fmt.format(house_name)),
            annual_fuel_cost=int_input(annual_fuel_cost_fmt.format(house_name)),
            tax_rate=float_input(tax_rate_fmt.format(house_name)),
        )
        print()  # Space between inputs.
    return houses


def calculate_bills(houses: Houses, *, years: int = 1) -> Bills:
    """
    Calculate bills over x amount of years following problem description.

    1. Add the fuel costs for x years
    2. Calculate taxes for x years
    3. Add to total with both fuel and taxes.
    """
    bills = {}
    for house_name, (init_cost, annual_fuel_cost, tax_rate) in houses.items():
        fuel_cost = annual_fuel_cost * years
        taxes = init_cost * tax_rate * years
        total = init_cost + fuel_cost + taxes

        bills[house_name] = Bill(init_cost, fuel_cost, taxes, total)
    return bills


def print_bills(houses: Bills) -> None:
    """
    Print a "recipt" table following the format of the example output.
    """
    print(
        table_fmt.format(
            init_cost="INITITAL HOUSE COST",
            fuel_cost="ANNUAL FUEL COST",
            taxes="TAXES",
            total="TOTAL COST",
        )
    )

    for house_name, (init_cost, fuel_cost, tax_rate, total) in houses.items():
        print(
            table_fmt.format(
                init_cost=dollar_fmt.format(init_cost),
                fuel_cost=dollar_fmt.format(fuel_cost),
                taxes=dollar_rounded_fmt.format(tax_rate),
                total=dollar_fmt.format(total),
            )
        )


if __name__ == "__main__":
    if len(sys.argv) > 1:
        houses = input_three_houses()
    else:
        houses = example_houses

    all_bills = calculate_bills(houses, years=5)
    print_bills(all_bills)
