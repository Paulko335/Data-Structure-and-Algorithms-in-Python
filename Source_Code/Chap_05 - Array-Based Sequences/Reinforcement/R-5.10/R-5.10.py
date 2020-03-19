# R-5.10
# The constructor for the CaesarCipher class in Code Fragment 5.11 can
# be implemented with a two-line body by building the forward and backward
# strings using a combination of the join method and an appropriate
# comprehension syntax. Give such an implementation.


# Original constructor
def __init__(self, shift):
    """Construct Caesar cipher using given integer shift for rotation."""
    encoder = [None] * 26  # temp array for encryption
    decoder = [None] * 26  # temp array for decryption
    for k in range(26):
        encoder[k] = chr((k + shift) % 26 + ord('A'))
        decoder[k] = chr((k - shift) % 26 + ord('A'))
    self._forward = ''.join(encoder)  # will store as string
    self._backward = ''.join(decoder)  # since fixed


# Equivalent constructor
def __init__(self, shift):
    self._forward = "".join([chr((k + shift) % 26 + ord("A")) for k in range(26)])
    self._backward = "".join([chr((k - shift) % 26 + ord("A")) for k in range(26)])
