# Sean

# unit = 1 second
# length of dot is one unit
# dash is three units
# the space between letters is three units
# the space between words is seven units

s = "Hello this is Sean"


def morse(text):
    encrypt = {'A': '.-', 'B': '-...', 'C': '-.-.',
               'D': '-..', 'E': '.', 'F': '..-.',
               'G': '--.', 'H': '....', 'I': '..',
               'J': '.---', 'K': '-.-', 'L': '.-..',
               'M': '--', 'N': '-.', 'O': '---',
               'P': '.--.', 'Q': '--.-', 'R': '.-.',
               'S': '...', 'T': '-', 'U': '..-',
               'V': '...-', 'W': '.--', 'X': '-..-',
               'Y': '-.--', 'Z': '--..', ' ': '.....'}
    decrypt = {value: key for key, value in encrypt.items()}

    if '-' in text:
        return '' .join(decrypt[i] for i in text.split())
    return ' ' .join(encrypt[i] for i in text.upper())


print(morse(s))
