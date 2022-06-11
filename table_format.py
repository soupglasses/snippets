"""
# Table Formatter

My submission for the Summer Codejam 2021 qualifer[1].

1: https://github.com/python-discord/cj8-qualifier

Example output:
    ┌────────────┬───────────┬─────────┐
    │ User       │ Messages  │ Role    │
    ├────────────┼───────────┼─────────┤
    │ Lemon      │ 183285    │ Owner   │
    │ Sebastiaan │ 183285.1  │ Owner   │
    │ KutieKatj  │ 15000     │ Admin   │
    │ Jake       │ MoreThanU │ Helper  │
    │ Joe        │ -12       │ Idk Tbh │
    └────────────┴───────────┴─────────┘
"""
from collections import namedtuple
from typing import Any, Iterable, Optional

FormatLine = namedtuple("FormatLine", "begin pad sep end")
TableFormat = namedtuple("TableFormat", "top data middle bottom")


TABLE_FORMAT = TableFormat(
    top=FormatLine("┌", "─", "┬", "┐"),
    data=FormatLine("│", " ", "│", "│"),
    middle=FormatLine("├", "─", "┼", "┤"),
    bottom=FormatLine("└", "─", "┴", "┘"),
)


def center(text: str, length: int) -> str:
    """Alternative to str.center that will lean left instead of right."""
    return f"{text:^{length}}"


def format_line(
    line: FormatLine,
    widths: list,
    row: Optional[Iterable] = None,
    centered: bool = False,
) -> str:
    """Returns a single row formatted using a `FormatLine` object."""
    output = line.begin
    if row:
        for col, width in zip(row, widths):
            col = center(col, width) if centered else col.ljust(width)
            output += f" {col} {line.sep}"
    else:
        for width in widths:
            output += line.pad * (width + 2) + line.sep

    # We always add a `line.sep` to the end of each column
    # generation. But since we are now done adding all the
    # columns, we will replace the last seperator character
    # with a `line.end` to complete the formatting.
    return output[:-1] + line.end


def make_table(
    rows: list[list[Any]],
    labels: Optional[list[Any]] = None,
    centered: bool = False,
) -> str:
    """
    :param rows: 2D list containing objects that have a single-line
                 representation (via `str`). All rows must be of the
                 same length.
    :param labels: List containing the column labels. If present,
                   the length must equal to that of each row.
    :param centered: If the items should be aligned to the center,
                     else they are left aligned.
    :return: A table representing the rows passed in.
    """
    if not rows:
        return ""
    if not all(len(row) == len(rows[0]) for row in rows):
        raise ValueError("Rows are not all the same length!")
    if labels and len(labels) != len(rows[0]):
        raise ValueError("Labels and rows are different length!")

    # columns: Rotates by 90° to create the columns of the table.
    # width: Finds each maximum width for each column.
    columns = list(zip(*[labels] + rows if labels else rows))
    widths = [max(map(len, map(str, column))) for column in columns]

    output = [format_line(TABLE_FORMAT.top, widths)]
    if labels:
        output.append(
            format_line(
                TABLE_FORMAT.data, widths, row=map(str, labels), centered=centered
            )
        )
        output.append(format_line(TABLE_FORMAT.middle, widths))

    for row in rows:
        output.append(
            format_line(TABLE_FORMAT.data, widths, row=map(str, row), centered=centered)
        )
    output.append(format_line(TABLE_FORMAT.bottom, widths))

    return "\n".join(output)


if __name__ == "__main__":
    ans_1 = make_table(
        rows=[["Lemon"], ["Sebastiaan"], ["KutieKatj9"], ["Jake"], ["Not Joe"]]
    )
    ans_2 = make_table(
        rows=[
            ["Lemon", 18_3285, "Owner"],
            ["Sebastiaan", 18_3285.1, "Owner"],
            ["KutieKatj", 15_000, "Admin"],
            ["Jake", "MoreThanU", "Helper"],
            ["Joe", -12, "Idk Tbh"],
        ],
        labels=["User", "Messages", "Role"],
    )
    ans_3 = make_table(
        rows=[
            ["Ducky Yellow", 3],
            ["Ducky Dave", 12],
            ["Ducky Tube", 7],
            ["Ducky Lemon", 1],
        ],
        labels=["Name", "Duckiness"],
        centered=True,
    )
    print("Example 1:", ans_1, "Example 2:", ans_2, "Example 3:", ans_3, sep="\n")
