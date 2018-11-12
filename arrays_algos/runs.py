from typing import List

from arrays_algos import Sort, Search, sorts
from arrays_algos.searches import linear_search, binary_search_recursive, binary_search_iterative
from arrays_algos.sorts import insertion_sort, binary_insertion_sort, merge_sort, merge_insertion_sort
from utils.tables import create_table, fill_table, print_table


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

    Sort.mas = mas
    sort = []

    sort_table = create_table("Sorts results", ['Name', 'N', 'Time (seconds)', 'Status'])

    sort.append(Sort("Insertion sort", insertion_sort))
    sort.append(Sort("Insertion sort with binary search", binary_insertion_sort))
    sort.append(Sort("Merge sort", merge_sort))
    sort.append(Sort("Merge sort with insertion", merge_insertion_sort))

    fill_table(sort_table, sort, show)

    print_table(sort_table, sort_by, reverse)


def run_searches(sort_by: str, search_list: List[int], reverse=False, show=False):
    """
    Prints all searches results.
    :param show: if True - search results will be printed before result table.
    :param reverse: reversed sort in table.
    :param search_list: array of int elements where need search.
    :param sort_by: parameter to search printed tables.
    """

    # print(linear_search(mas, 1))

    if show:
        print("source: {0}".format(search_list))

    Search.set_mas(sorts.merge_insertion_sort(search_list))
    search = []

    search_table = create_table("Searches results", ['Name', 'N', 'Time (seconds)', 'Status'])

    search.append(Search("Linear search", linear_search))
    search.append(Search("Binary search (Recursive)", binary_search_recursive))
    search.append(Search("Binary search (Iterative)", binary_search_iterative))

    fill_table(search_table, search, show)

    print_table(search_table, sort_by, reverse)
