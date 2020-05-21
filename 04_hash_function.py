# MD5 128bit
# SHA-0/SHA-1 160bit
# SHA-256/SHA-224 256bit/224bit
# SHA-512/SHA-384 512bit/384bit
import hashlib

m = hashlib.md5('Hello world!'.encode("utf-8"))

print(m.hexdigest())
