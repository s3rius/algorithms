import random
import time
from typing import List, Any

from utils.TableItem import TableItem


class Sort(TableItem):
    mas: List

    def __init__(self, name, sort_function):
        self.sort_name = name
        self.sort_function = sort_function

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

        return [self.sort_name, len(self.mas), elapsed_time, check_sort(mas)]


class Search(TableItem):
    _mas: List
    _element: int

    def __init__(self, name: str, search_function):
        self.search_name = name
        self.search_function = search_function

    @staticmethod
    def set_mas(act_arr: List):
        Search._mas = act_arr
        Search._element = random.choice(act_arr)

    def row(self, show: bool):
        def check_correctness(i: int):
            status = "Passed"
            if i is not None:
                if len(self._mas) <= i or i < 0:
                    status = "Failed (index out of range: index = {index})".format(index=i)
                elif self._mas[i] != self._element:
                    status = "Failed (Wrong element. Expected: {el}, Actual: {act})".format(el=self._element,
                                                                                            act=self._mas[i])
            return status

        t = time.process_time()
        index = self.search_function(self._mas, self._element)
        elapsed_time = time.process_time() - t
        if show:
            print("name:{name}, index:{index}, el: {el}".format(name=self.search_name, index=index, el=self._element))

        return [self.search_name, len(self._mas), elapsed_time, check_correctness(index)]
