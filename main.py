import random

import sorts

if __name__ == "__main__":
    mas = random.sample(range(1, 100), 12)
    sorts.run_sorts("time", mas, show=True)
