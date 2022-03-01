def vowel_to_code(vowel):
    vowcode = {
        "A": "&",
        "a": "&",
        "E": "$",
        "e": "$",
        "I": "!",
        "i": "!",
        "O": "@",
        "o": "@",
        "U": "^",
        "u": "^",
    }

    return vowcode.get(vowel)
    
def con_to_code(const):
    concode = {
        "B": "8",
        "b": "8",
        "C": "%",
        "c": "%",
        "D": ")",
        "d": ")",
        "F": "#",
        "f": "#",
        "G": "?",
        "g": "?",
        "H": "=",
        "h": "=",
        "J": "-",
        "j": "-",
        "K": "<",
        "k": "<",
        "L": "_",
        "l": "_",
        "M": "n",
        "m": "n",
        "N": "M",
        "n": "M",
        "P": "R",
        "p": "R",
        "Q": "]",
        "q": "]",
        "R": "P",
        "r": "P",
        "S": "{",
        "s": "{",
        "T": "*",
        "t": "*",
        "V": "W",
        "v": "W",
        "W": "V",
        "w": "V",
        "X": "+",
        "x": "+",
        "Y": "/",
        "y": "/",
        "Z": "~",
        "z": "~",
    }

    return concode.get(const)

def special_code(specChar):
    speCode = {
        " ": "s",
        "-": "t",
        ".": "i",
        ",": "p",
        "!": "l",
        "@": "Q",
        "*": "e",
        "$": "w",
        "?": "y",
        "&": "g",
        "%": "q",
    }

    return speCode.get(specChar)
        




message = str(input("Enter a message to be encoded: "))
code = ""

for letter in message:
    if letter in "AEIOUaeiou":
        code += (vowel_to_code(letter))
    elif letter in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
        code += (con_to_code(letter))
    elif letter in "-.,!@*$?&% ":
        code += (special_code(letter))
    else:
        print("Im sorry cant code this character: " + letter)

print(code)
