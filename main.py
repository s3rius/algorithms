import random

import searches
import sorts

if __name__ == "__main__":
    mas = random.sample(range(1, 100000), 5000)
    sorts.run_sorts("Name", mas, show=False)
    search_element = mas[1]
    searches.run_searches("Name", mas, search_element)
