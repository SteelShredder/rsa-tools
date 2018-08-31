def decrypt(m,d,n):
    """
    Returns decrypted message.
    Parameters:
    m (int): encrypted message
    d (int): private key
    n (int): modulus
    Output:
    decrypted message in numeral form
    """
    return(pow(m,d,n))
