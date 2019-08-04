from pythonds.basic import Stack

def baseConvertter(decNumber, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConvertter(139, 2))
print(baseConvertter(139, 8))
print(baseConvertter(139, 16))
