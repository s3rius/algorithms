import time
from math import ceil
from typing import List, Any

from prettytable import PrettyTable


class Sort(object):
    mas: List

    def __init__(self, name, sort_function):
        self.sort_name = name
        self.sort_function = sort_function
        self.n = len(self.mas)

    def row(self, show: bool) -> List[Any]:
        """
        Method to test sort function and create table row.
        :param show: if True - sort results will be printed before result table.
        :return: table row.
        """

        def check_sort(array):
            status = "Passed"
            for i in range(1, len(array)):
                if array[i] < array[i - 1]:
                    status = "Failed"
            return status

        t = time.process_time()
        mas = self.sort_function(self.mas)
        elapsed_time = time.process_time() - t
        if show:
            print("{name}: {array}".format(name=self.sort_name, array=mas))

        return [self.sort_name, self.n, elapsed_time, check_sort(mas)]


def insertion_sort(massive: List):
    array = massive.copy()
    for j in range(1, len(array)):
        element = array[j]
        i = j - 1
        while i >= 0 and array[i] > element:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = element
    return array


def merge_sort(massive: List):
    def merge(part1, part2):
        res = []
        while len(part1) > 0 and len(part2) > 0:
            if part1[0] <= part2[0]:
                res.append(part1[0])
                part1.pop(0)
            else:
                res.append(part2[0])
                part2.pop(0)
        if len(part1) > 0:
            res.extend(part1)
        else:
            res.extend(part2)
        return res

    if len(massive) > 1:
        half_index = ceil(len(massive) / 2)
        part1 = merge_sort(massive[0:half_index])
        part2 = merge_sort(massive[half_index:])
        return merge(part1, part2)
    else:
        return massive


def run_sorts(sort_by: str, mas: List[int], reverse=False, show=False):
    """
    Prints all sorts results.
    :param show: if True - sort results will be printed before result table.
    :param reverse: reverse sort
    :param mas: array of int elements to sort.
    :param sort_by: parameter to sort printed tables. Possible values:
        - time
        - name
        - other value will be ignored.
    """

    if show:
        print("source: {0}".format(mas))

    Sort.n = len(mas)
    Sort.mas = mas
    sorts = []
    table = PrettyTable()

    table.title = 'Sorts results'
    table.field_names = ['Sort name', 'n', 'time (seconds)', 'status']

    sorts.append(Sort("insertion sort", insertion_sort))
    sorts.append(Sort("Merge sort", merge_sort))

    for sort in sorts:
        table.add_row(sort.row(show))

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
