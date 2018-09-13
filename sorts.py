import time
from typing import List

from prettytable import PrettyTable


class Sort(object):
    mas: List

    def __init__(self, name, sort_function):
        self.sort_name = name
        self.sort_function = sort_function
        self.n = len(self.mas)

    def row(self):
        t = time.process_time()
        mas = self.sort_function(self.mas)
        elapsed_time = time.process_time() - t
        # print(mas)
        return [self.sort_name, self.n, elapsed_time]


def insertion_sort(massive: List[int]):
    array = massive.copy()
    for j in range(1, len(array)):
        element = array[j]
        i = j - 1
        while i >= 0 and array[i] <= element:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = element
    return array


def run_sorts(sort_by: str, mas: List[int], reverse=False):
    """
    Prints all sorts results.
    :param reverse: reverse sort
    :param mas: array of int elements to sort.
    :param sort_by: parameter to sort printed tables. Possible values:
        - time
        - name
        - other value will be ignored.
    """

    Sort.n = len(mas)
    Sort.mas = mas
    sorts = []
    table = PrettyTable()

    table.title = 'Sorts results'
    table.field_names = ['Sort name', 'n', 'time (seconds)']

    sorts.append(Sort("insertion sort", insertion_sort))

    for sort in sorts:
        table.add_row(sort.row())

    print_table(reverse, sort_by, table)


def print_table(reverse, sort_by, table):
    if sort_by != "none":
        if sort_by == "time":
            sort_by = "time (seconds)"
        elif sort_by == "name":
            sort_by = "Sort name"
        table.sortby = sort_by
        table.reversesort = reverse

    print(table)
