import binascii

def number2string(i):
    """Convert a number to a string

    Input: long or integer
    Output: string (big-endian)
    """
    assert isinstance(i, int), "expected i to be <class 'int'>, got: %s" % type(i)
    s=hex(i)[2:].rstrip('L')
    if len(s) % 2:
        s = '0' + s
    return str(binascii.unhexlify(s), "ascii")

def number2string_N(i, N):
    """Convert a number to a string of fixed size

    i: long or integer
    N: length of string
    Output: string (big-endian)
    """
    assert isinstance(i, int), "expected i to be <class 'int'>, got: %s" % type(i)
    assert isinstance(N, int), "expected N to be <class 'int'>, got: %s" % type(i)
    s = '%0*x' % (N*2, i)
    return str(binascii.unhexlify(s), "ascii")

def string2number(i):
    """ Convert a string to a number

    Input: string (big-endian)
    Output: long or integer
    """
    assert isinstance(i, str), "expected i to be <class 'str'>, got: %s" % type(i)
    return int(binascii.hexlify(i.encode("utf-8")),16)

def xorstring(a,b):
    """XOR two strings of same length

    For more complex cases, see CryptoPlus.Cipher.XOR"""
    assert isinstance(a, str), "expected a to be <class 'str'>, got: %s" % type(i)
    assert isinstance(b, str), "expected b to be <class 'str'>, got: %s" % type(i)
    assert len(a) == len(b)
    return number2string_N(string2number(a)^string2number(b), len(a))

class Counter(str):
    #found here: http://www.lag.net/pipermail/paramiko/2008-February.txt
    """Necessary for CTR chaining mode

    Initializing a counter object (ctr = Counter('xxx'), gives a value to the counter object.
    Everytime the object is called ( ctr() ) it returns the current value and increments it by 1.
    Input/output is a raw string.

    Counter value is big endian"""
    def __init__(self, initial_ctr):
        if not isinstance(initial_ctr, str):
            raise TypeError("nonce must be str")
        self.c = int(binascii.hexlify(initial_ctr.encode("utf-8")),16)
    def __call__(self):
        # This might be slow, but it works as a demonstration
        ctr = ("%032x" % (self.c,))
        ctr = str(binascii.unhexlify(ctr), "ascii")
        self.c += 1
        return ctr
