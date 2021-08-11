"""
# Quadratic Formula Solver

A short CLI tool to help solve a quadratic equation[1].

[1]: https://en.wikipedia.org/wiki/Quadratic_equation
"""
import argparse
from decimal import Decimal, getcontext

parser = argparse.ArgumentParser(description="Quadratic formula solver")
parser.add_argument("a", type=float)
parser.add_argument("b", type=float)
parser.add_argument("c", type=float)
parser.add_argument(
    "-p", "--precision", default=3, type=int, help="Decimal precision by number"
)
args = parser.parse_args()

getcontext().prec = args.precision

a, b, c = Decimal(args.a), Decimal(args.b), Decimal(args.c)

try:
    top = ((b * b) - (4 * a * c)).sqrt()
    bottom = 2 * a
    x1 = ((-b) + top) / bottom
    x2 = ((-b) - top) / bottom
except:
    print(f"No valid solution for a={a}, b={b}, c={c}.")
else:
    if x1 == x2:
        print(f"x0={x1}")
    else:
        print(f"x1={x1}\tx2={x2}")
