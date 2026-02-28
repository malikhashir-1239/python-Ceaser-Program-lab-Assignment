# Caesar Cipher Program

# Encryption Function
def caesar_encrypt(text, shift):
    result = ""

    for ch in text:
        if ch.isalpha():  # check if letter
            if ch.isupper():
                base = ord('A')
            else:
                base = ord('a')

            new_char = chr((ord(ch) - base + shift) % 26 + base)
            result += new_char
        else:
            result += ch  # space or special character same

    return result


# Decryption Function
def caesar_decrypt(text, shift):
    result = ""

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                base = ord('A')
            else:
                base = ord('a')

            new_char = chr((ord(ch) - base - shift) % 26 + base)
            result += new_char
        else:
            result += ch

    return result


# Main Program
print(" Caesar Cipher Program ")

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted = caesar_encrypt(message, shift)
print("Encrypted Message:", encrypted)

decrypted = caesar_decrypt(encrypted, shift)
print("Decrypted Message:", decrypted)