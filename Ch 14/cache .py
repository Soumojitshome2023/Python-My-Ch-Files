
import time
from functools import lru_cache

@lru_cache(maxsize=32)     # work  k cache a save kore rakhe, tai next bar same kaj korte time kom lageee
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    print("Done... Calling again")
    some_work(3)
    print("Called again")

