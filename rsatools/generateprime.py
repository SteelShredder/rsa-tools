import secrets
def genprime(bitlen):
    """
    Generates prime numbers.
    Parameters:
    bitlen (int): length of prime
    Output:
    Prime number
    """

    seed = secrets.randbits(bitlen)
    seed += seed % 2+1
    while 1==1:
        if  pow(2, seed-1, seed) == 1:
            return seed
        seed+=2
