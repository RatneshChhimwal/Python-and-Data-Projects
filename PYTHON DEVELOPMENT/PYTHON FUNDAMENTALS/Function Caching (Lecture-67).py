"""

Function caching is a technique for improving the performance of a program by storing the results of a function call
so that you can reuse the results instead of recomputing them every time the function is called.
This can be particularly useful when a function is computationally expensive, or when the inputs to the function are unlikely to change frequently.

In Python, function caching can be achieved using the functools.lru_cache decorator.
The functools.lru_cache decorator is used to cache the results of a function so that you can reuse the results
instead of recomputing them every time the function is called. Here's an example:

"""

import functools
import time

@functools.lru_cache(maxsize=None)
def number(n):
    time.sleep(5)
    return n * 5


print(number(2))
print("Done for 2")
print(number(4))
print("Done for 4")
print(number(6))
print("Done for 6")
print(number(8))
print("Done for 8")
print(number(2))
print("Done for 2")
print(number(4))
print("Done for 4")
print(number(10))
print("Done for 10")
