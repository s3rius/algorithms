from typing import List, Any

from prettytable import PrettyTable


class TableItem(object):
    """
    Class needs to be implemented if you want to wrap object in table row.
    """

    def row(self, show: bool) -> List[Any]:
        """
        Method to represent object for inserting in row.
        :param show: If true - You can print something before creating tables.
        :return List with values.
        :rtype: List[Any]
        """
        return []


def create_table(title: str, columns: List[str]) -> PrettyTable:
    table = PrettyTable()
    table.title = title
    table.field_names = columns
    return table


def fill_table(table: PrettyTable, items: List[TableItem], show=False):
    for item in items:
        row = item.row(show)
        table.add_row(row)


def print_table(table: PrettyTable, sort: str, reverse: bool):
    table.sortby = sort
    table.reversesort = reverse
    print(table)
