from .eea import eea
def mulinv(b, n):
    """ performs mulplicative inverse """
    
    g, x, _ = eea(b, n)
    if g == 1:
        return x % n
