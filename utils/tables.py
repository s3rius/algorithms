from typing import List

from prettytable import PrettyTable

from arrays_algos.Types import Search, Sort
from utils import FunType, registered_functions
from utils.TableItem import TableItem


def create_table(title: str, columns: List[str]) -> PrettyTable:
    """
    Creates new table. With given columns.
    :param title: Table title.
    :param columns: List of strings (Column names).
    :return: table.
    """
    table = PrettyTable()
    table.title = title
    table.field_names = columns
    return table


def fill_table(table: PrettyTable, items: List[TableItem], show=False):
    """
    Fill table with data.
    :param table: table to fill.
    :param items: items to add.
    :param show: if True ~> data will be printed before table.
    """
    for item in items:
        row = item.row(show)
        table.add_row(row)


def print_table(table: PrettyTable, sort: str, reverse: bool):
    """
    Prints generated table.
    :param table: table to print.
    :param sort: sort parameter. Name of table row to sort.
    :param reverse: print table in reverse order.
    """
    table.sortby = sort
    table.reversesort = reverse
    print(table)


def register(name, f_type):
    """
    Adds function in registered_functions.
    :param name: Name of function that will be displayed in table.
    :param f_type: type of function.
    :return: function.
    """

    def decor(func):
        if f_type == FunType.search:
            registered_functions[f_type].append(Search(name, func))
        elif f_type == FunType.sort:
            registered_functions[f_type].append(Sort(name, func))
        else:
            raise Exception("Can't find that kind of functions: '{t}'. Use FunType enum.")
        return func

    return decor
