from pkg_resources import non_empty_lines
from typing import Optional


def arctan_i(x : int) -> Optional[tuple[float,int, float]]:

    if x < 0 or x > 1:
        print("error!")
        return None

    i = 0
    error = 1.0
    a = 0.0

    while error >= 0.0001:

        a += (((-1) ** i) * (x ** (2 * i + 1))) / ( 2 * i + 1)
        error = (x ** ((2 * (i + 1)) + 1)) / ((2 * i) + 1)

        i += 1

    return a , i + 2, error

print(arctan_i(0))