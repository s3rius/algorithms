from typing import List, Any

from prettytable import PrettyTable


class TableItem(object):

    def row(self, show: bool) -> List[Any]:
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
