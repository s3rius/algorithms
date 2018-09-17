import time
from typing import List, Any

import sorts
from utils import TableItem, create_table, fill_table, print_table


class Search(TableItem):
    mas: List

    def __init__(self, name: str, search_function, element: Any):
        self.element = element
        self.search_name = name
        self.search_function = search_function
        self.n = len(self.mas)

    def row(self, show: bool):
        def check_correctness(i: int):
            status = "Passed"
            if i is not None:
                if self.n <= i or i < 0:
                    status = "Failed (index out of range: index = {index})".format(index=i)
                elif self.mas[i] != self.element:
                    status = "Failed (Wrong element. Expected: {el}, Actual: {act})".format(el=self.element,
                                                                                            act=self.mas[i])
            return status

        t = time.process_time()
        index = self.search_function(self.mas, self.element)
        elapsed_time = time.process_time() - t
        if show:
            print("name:{name}, index:{index}, el: {el}".format(name=self.search_name, index=index, el=self.element))

        return [self.search_name, self.n, elapsed_time, check_correctness(index)]


def linear_search(array: List[Any], element: Any) -> Any:
    """
    Function returns requested element index if such element exists.
    :param array: where element can be found.
    :param element: element that needs to be found.
    :return: element index or None.
    """
    for index, el in enumerate(array):
        if el == element:
            return index
    return None


def binary_search_recursive(array: List[Any], element: Any) -> int:
    def search(left_b: int, right_b: int):

        mid = left_b + (right_b - left_b) // 2

        if array[mid] == element:
            return mid
        elif array[mid] > element:
            return search(left_b, mid)
        else:
            return search(mid, right_b)

    left = 0
    right = len(array)
    return search(left, right)


def binary_search_iterative(array: List[Any], element: Any) -> int:
    left = 0
    right = len(array)
    while True:
        mid = left + (right - left) // 2
        if element == array[mid]:
            return mid
        elif element <= array[mid]:
            right = mid
        else:
            left = mid


def run_searches(sort_by: str, mas: List[int], element: int, reverse=False, show=False):
    """
    Prints all searches results.
    :param element: element to find.
    :param show: if True - search results will be printed before result table.
    :param reverse: reversed sort in table.
    :param mas: array of int elements where need search.
    :param sort_by: parameter to search printed tables.
    """

    # print(linear_search(mas, 1))

    if show:
        print("source: {0}".format(mas))

    Search.mas = sorts.merge_sort(mas)
    search = []

    search_table = create_table("Searches results", ['Name', 'N', 'Time (seconds)', 'Status'])

    search.append(Search("Linear search", linear_search, element))
    search.append(Search("Binary search (Recursive)", binary_search_recursive, element))
    search.append(Search("Binary search (Iterative)", binary_search_iterative, element))

    fill_table(search_table, search, show)

    print_table(search_table, sort_by, reverse)
