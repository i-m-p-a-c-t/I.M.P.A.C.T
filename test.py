import hashlib
password = 'pa$$w0rd'
h = hashlib.md5(password.encode())
h = h.hexdigest()
print(len(h))
