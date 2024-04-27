from typing import List, Any
from tabulate import tabulate  # type: ignore
from datetime import datetime
import uuid


def is_promo_day(str_date: str, order_promo_day: str) -> bool:
    """
    Check if a given date falls on a promotional day.

    Args:
        str_date (str): A date string in the format '%Y-%m-%d %H:%M:%S.%f'.
        order_promo_day (str): The promotional day string (e.g., 'MON', 'TUE', etc.).

    Returns:
        bool: True if the given date falls on the promotional day, False otherwise.
    """
    date_object = datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S.%f")
    day_of_week = date_object.strftime("%a")
    return day_of_week.upper() == order_promo_day.upper()


def unique_id() -> str:
    """
    Generate a unique identifier (UUIDv4) as a string.

    Returns:
        str: A unique identifier string generated using UUIDv4.
    """
    return str(uuid.uuid4())


def print_table(header_title: str, data_src: List[List[Any]], table_header: List[str]) -> None:
    """
    Print a tabulated table with a specified header title and column headers.

    Args:
    - header_title (str): The title of the table to be printed.
    - data_src (List[List[Any]]): A list of lists containing the data to be displayed in the table.
    - table_header (List[str]): A list of strings representing the column headers of the table.

    Returns:
    - None
    """
    print_boxed_title(header_title, 10, "title")
    print(tabulate(data_src, headers=table_header, tablefmt="fancy_grid"))


def print_boxed_title(box_caption: str = "This is a boxed title", box_gaps: int = 5,
                      title_case: str = "uppercase") -> None:
    """
    Print a string in a boxed format with the title centered.

    Args:
        box_caption (str): The title text to be displayed. Default is "This is a boxed title".
        box_gaps (int): The number of spaces on each side of the title text inside the box. Default is 5.
        title_case (str): The case format of the title text. Can be "uppercase", "lowercase", or "title". Default is "uppercase".

    Returns:
    - None
    """
    title_case = title_case.lower()
    title_length: int = len(box_caption)
    box_length: int = title_length + box_gaps * 2

    # Title text case format
    if title_case == "title":
        box_caption = box_caption.title()
    elif title_case == "uppercase":
        box_caption = box_caption.upper()
    else:
        box_caption = box_caption.lower()

    # Let's build the box with the title in the middle
    box_top = "╔" + "═" * box_length + "╗"
    box_bottom = "╚" + "═" * box_length + "╝"
    spacing = ' ' * box_gaps
    box_middle = f"║{spacing}{box_caption.center(box_length - (box_gaps * 2))}{spacing}║"

    print()
    print(box_top)
    print(box_middle)
    print(box_bottom)
    print()
