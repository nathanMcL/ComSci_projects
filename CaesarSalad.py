# python project Cesar Cipher program
import offset as offset

from Encryption import plain_text, cipher_text

#offset plus or minus determine cipher

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# let user choose offset
def get_offset():
    offset = int(input("Enter offset: "))
    return offset

def get_plain_text():
 # example: plain_text = "DRINK WATER TO BEAT THE HEAT!"
    plain_text = input("Enter your plain-text for encryption: ")
    return plain_text


def caesar_cipher(plain_text, offset):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_text = []
    return cipher_text


if offset < 0:
    shifted_letters = letters[abs(offset):] + letters[: abs(offset)]
elif offset> 0:
    shifted_letters = letters[-offset:] + letters[:-offset]
else:
    shifted_letters = letters

letters = letters + letters.lower()
shifted_letters = shifted_letters + shifted_letters.lower()

for text in plain_text:
    if text.isalpha():
        for i in range(52):
            if text == letters[i]:
             cipher_text.append(shifted_letters[i])
    else:
        cipher_text.append(text)

for item in cipher_text:
    print(item, end="")


pt = get_plain_text()
offset = get_offset()
ct = caesar_cipher(pt, offset)

