import Stack as st
hexVal = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}

decVal = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

stack = st.Stack()
def complementoA(value):
    compA = ""
    for i in range (len(value)):
        if int(value[i]) == 1:
            compA += "0"
        else:
            compA +="1"
    return compA

def complementoA2(value): 
    compA2 = complementoA(value)
    res = int(compA2, 2)+1
    compA2 = format(res, "08b")
    return str(compA2)


def hexToDec(value):
    reference = list(hexVal)
    value = value[::-1]
    for i in range (len(value)):
        if value[i] in reference:
            stack.push(int((16**i) * hexVal[value[i]]))
        else: 
            stack.push(int(value[i]) * (16**i))
    hexvalue = 0
    for i in range(len(stack.modules)):
        hexvalue += stack.pop()
    stack.modules.clear()
    return str(hexvalue)


def decToHex(value):
    condition = True
    divisor = int(value)//16
    stack.push(int(value)%16)
    while condition:
        cociente = divisor//16
        stack.push(divisor%16)
        divisor = cociente
        if (cociente < 16):
            stack.push(cociente)
            condition = False

    decValue = ""
    for i in range(len(stack.modules)):
       if stack.modules[i] > 9:
           stack.modules[i] = decVal[stack.modules[i]]

    for i in range(len(stack.modules)):
        decValue += str(stack.pop())
    stack.modules.clear()
    return(str(decValue))
