from .eea import eea
# This module is licensed under CC BY-SA 3.0
# Human readable https://creativecommons.org/licenses/by-sa/3.0/
# Actual license https://creativecommons.org/licenses/by-sa/3.0/legalcode
# From https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def mulinv(b, n):
    """ performs mulplicative inverse """
    
    g, x, _ = eea(b, n)
    if g == 1:
        return x % n
