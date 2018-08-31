from .generateprime import genprime
from .mulplicativeinverse import mulinv
import numpy as np
def genkeys(e, bit):

    """
    Generates keys for rsa.
    Parameters:
    e (int): public key
    bit (int): bit length of primes
    Outputs:
    n (int): modulus
    e (int): public key
    d (int): private key
    """

    lam=0
    while np.gcd(e, lam) != 1:
        p=genprime(bit)
        q=genprime(bit)
        lam=np.lcm(p-1, q-1)
    n=p*q
    d=mulinv(e,int(lam))
    return(n, e, d)
