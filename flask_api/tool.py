import hashlib


def Md5Encrypt(plain):
    return hashlib.md5(plain).hexdigest()