"""
Given the string representations of two integers, return the string representation of the sum of those integers.

For example:

sumStrings('1','2') // => '3'
A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

I have removed the use of BigInteger and BigDecimal in java

Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.

"""

import gmpy2
def sum_strings(x,y):
    return"{}".format((gmpy2.mpz(x) if x else 0) + (gmpy2.mpz(y) if y else 0))
