import hashlib

# Hash functions expect bytes as input: the encode() method turns strings into bytes
input_bytes = b"BACKPACK"
output = hashlib.sha256(input_bytes)

# We use hexdigest() to convert bytes to hex because it's easier to read
print(output.hexdigest())