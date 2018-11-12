from math import ceil
from typing import List

from utils import FunType
from utils.tables import Manager

man = Manager()


@man.register("Insertion sort", FunType.sort)
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


@man.register("Insertion sort (Binary)", FunType.sort)
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


@man.register('Merge sort', FunType.sort)
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


@man.register('Insertion sort (Merge modified)', FunType.sort)
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
