from typing import List

from prettytable import PrettyTable

from arrays_algos.Types import Search, Sort
from utils import FunType
from utils.TableItem import TableItem


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


class Manager(object):
    registered_functions = {
        FunType.sort: [],
        FunType.search: []
    }

    def register(self, name, f_type):
        def decor(func):
            if f_type == FunType.search:
                self.registered_functions[f_type].append(Search(name, func))
            elif f_type == FunType.sort:
                self.registered_functions[f_type].append(Sort(name, func))
            else:
                raise Exception("Can't find that kind of functions: '{t}'. Use FunType enum.")
            return func

        return decor
