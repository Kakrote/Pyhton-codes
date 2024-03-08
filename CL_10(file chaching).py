import time as t
from functools import lru_cache
@lru_cache(maxsize=None)
def file_chaching(x):
    # print(" the program is running")
    t.sleep(x)
    return x
if __name__=="__main__":
    print("now the task is runing .....")
    file_chaching(3) # will hold the program for 3 sec.
    print("done....")
    file_chaching(3) # this time it wont hold the program as its already been stored into the chaching memory.
    print("called again..")

