def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using modulo 26
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted_char)
        else:
            # Non-alphabetical characters (like punctuation) remain unchanged
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    text = "Veni, vidi, vici."
    shift = 14
    print(caesar_cipher(text, shift))

