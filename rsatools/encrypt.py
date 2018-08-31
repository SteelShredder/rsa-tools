def encrypt(m,e,n):
    """
    Returns decrypted message.
    Parameters:
    m (int): numeral message 
    e (int): public key
    n (int): modulus
    Output:
    encrypted message
    """
    return(pow(m,e,n))
