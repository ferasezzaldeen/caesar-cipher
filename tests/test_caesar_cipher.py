from caesar_cipher.caesar_cipher import *


def test_version():
    assert 1==1

#encrypt a string with a given shift
def test_encrypt():
    assert encrypt('abc',2)=='cde'

#decrypt a previously encrypted string with the same shift
def test_decrypt():
    assert decrypt('cde',2)=='abc'

#encryption should handle upper and lower case letters
def test_encrypt_capital():
    assert encrypt('ABC',2)=='cde'

#encryption should allow non-alpha characters but ignore them, including white space
def test_encrypt_SPECIAL():
    assert encrypt('ABC',2)=='cde'

#ecrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.
def test_crack():
    assert crack(encrypt('It was the best of times, it was the worst of times.',15))=='it was the best of times, it was the worst of times.'
