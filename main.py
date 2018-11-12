import random

from arrays_algos.runs import run_sorts, run_searches

if __name__ == "__main__":
    mas = random.sample(range(1, 100000), 8000)
    run_sorts("Name", mas, show=False)
    search_element = mas[2]
    run_searches("Name", mas)
