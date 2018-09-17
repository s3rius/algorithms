import time
from math import ceil
from typing import List, Any

from utils import create_table, fill_table, TableItem, print_table


class Sort(TableItem):
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
                    status = "Failed on position {pos}".format(pos=i)
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
    def merge(part1: List, part2: List) -> List:
        """
        Function to merge two sorted lists.
        :param part1: first sorted list.
        :param part2: second sorted list.
        :return: sorted combination of part1 and part2.
        """
        res = []  # result list.
        while len(part1) > 0 and len(part2) > 0:
            # Loop while both lists has at least one element.
            # Since lists already sorted we can check only first elements.
            # After comparing, we just delete lesser element from list.
            if part1[0] <= part2[0]:
                res.append(part1[0])
                part1.pop(0)
            else:
                res.append(part2[0])
                part2.pop(0)
        # In case if lists has different size.
        # We need to add all remaining elements.
        if len(part1) > 0:
            res.extend(part1)
        else:
            res.extend(part2)
        return res

    # Check length.
    if len(massive) > 1:
        # Array divided by half on tow arrays.
        half_index = ceil(len(massive) / 2)
        # Recursive calls on first and second parts.
        part1 = merge_sort(massive[0:half_index])
        part2 = merge_sort(massive[half_index:])
        return merge(part1, part2)
    else:
        # (Length <= 1) => reached recursion tail.
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

    # print(linear_search(mas, 1))

    if show:
        print("source: {0}".format(mas))

    Sort.mas = mas
    sort = []

    sort_table = create_table("Sorts results", ['Name', 'N', 'Time (seconds)', 'Status'])

    sort.append(Sort("insertion sort", insertion_sort))
    sort.append(Sort("Merge sort", merge_sort))

    fill_table(sort_table, sort, show)

    print_table(sort_table, sort_by, reverse)
    # for sort in sorts:
    #     table.add_row(sort.row(show))
    #
    # print_table(reverse, sort_by, table)
