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
    # Copying array.
    array = massive[:]
    # loop over elements except first.
    # Cause we don't need to move first element.
    for j in range(1, len(array)):
        # Current picked element.
        element = array[j]
        # index of elements to move. from 0 to i.
        i = j - 1
        # Loop over moving elements and move them if necessary.
        while i >= 0 and array[i] > element:
            # moving element forward.
            array[i + 1] = array[i]
            # Picking next element.
            i = i - 1
        # Insert inspected element.
        array[i + 1] = element
    return array


def binary_insertion_sort(massive: List):
    def search(el, left_b: int, right_b: int):
        """
        Modified binary search function.
        :param el: element to find.
        :param left_b: search area left border.
        :param right_b: search area right border.
        :return: index of element if element exists in array, or
                index where element need to be placed if element wasn't found.
        """
        # Divide list by half.
        mid = left_b + (right_b - left_b) // 2
        # if search areas intersected -> nothing was found.
        # return index where the element need to be placed.
        if left_b >= right_b:
            if array[left_b] > el:
                return left_b
            else:
                return left_b + 1
        # if element found -> return index.
        if array[mid] == el:
            return mid
        # Because we have already sorted array
        # We can suggest where is the element
        # And search in suggested part.
        elif array[mid] > el:
            return search(el, left_b, mid - 1)
        else:
            return search(el, mid + 1, right_b)

    # Copying array.
    array = massive[:]
    for j in range(1, len(array)):
        element = array[j]
        # Search index where element need to be placed.
        i = search(element, 0, j - 1)
        # Creates new array.
        array = array[:i] + [element] + array[i:j] + array[(j + 1):]
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


def merge_insertion_sort(mas: List):
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

    # Quantity of elements, when insertion sort will be faster then merge.
    k = 40
    # getting middle of array.
    mid = len(mas) // 2
    # Dividing array by half.
    part1 = mas[:mid]
    part2 = mas[mid:]
    # If every part of array has more than k elements:
    # Faster to divide that parts using merge sort.
    if len(mas) > 2 * k:
        part1 = merge_insertion_sort(part1)
        part2 = merge_insertion_sort(part2)
    # If every part of array k or less elements
    # Insertion sort will be faster.
    else:
        part1 = insertion_sort(part1)
        part2 = insertion_sort(part1)
    # Merge parts together.
    return merge(part1, part2)


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

    sort.append(Sort("Insertion sort", insertion_sort))
    sort.append(Sort("Insertion sort with binary search", binary_insertion_sort))
    sort.append(Sort("Merge sort", merge_sort))
    sort.append(Sort("Merge sort with insertion", merge_insertion_sort))

    fill_table(sort_table, sort, show)

    print_table(sort_table, sort_by, reverse)
    # for sort in sorts:
    #     table.add_row(sort.row(show))
    #
    # print_table(reverse, sort_by, table)
