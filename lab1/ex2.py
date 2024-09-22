def caesar_cipher_decrypt(text, shift):
    result = []
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            base = ord('A') if char.isupper() else ord('a')  # Check if uppercase or lowercase
            # Shift character back by the specified shift (13 in this case)
            shifted_char = chr((ord(char) - base - shift) % 26 + base)
            result.append(shifted_char)
        else:
            result.append(char)  # Keep punctuation and spaces unchanged
    return ''.join(result)

if __name__ == "__main__":
    encrypted_message = "Gur dhvpx oebja sbk whzcf bire gur ynml qbt"
    shift = 13
    print(caesar_cipher_decrypt(encrypted_message, shift))