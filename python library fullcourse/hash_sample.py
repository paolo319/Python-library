import hashlib

name = "Paolo"
print("Name:", name)
print("MD5: ", hashlib.md5(name.encode()).hexdigest())
print("SHA-1: ", hashlib.sha1(name.encode()).hexdigest())