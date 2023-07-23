def secret1(msg):
    return "".join([chr(ord(letter) + 1) for letter in list(msg)])


def secret2(msg):
    return "".join([chr(ord(letter) * 2) for letter in list(msg)])


def secret3(msg):
    return "".join([chr(ord(letter) - 1) for letter in list(msg)])


print(secret1("PYTHON JEST SUPER"))
print(secret2("PYTHON JEST SUPER"))
print(secret3(secret1("PYTHON JEST SUPER")))
