# This module is licensed under CC BY-SA 3.0
# Human readable https://creativecommons.org/licenses/by-sa/3.0/
# Actual license https://creativecommons.org/licenses/by-sa/3.0/legalcode
# From https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def eea(b, a):
    """Performs extended euclidean algorithm"""
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0
