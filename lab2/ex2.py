def KSA(key):
    key_length = len(key)
    S = list(range(256))  # Create the array "S"
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]  # Swap values
    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # Swap values
        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(key, plaintext):
    # Convert key and plaintext to their ASCII values
    key = [ord(c) for c in key]
    plaintext = [ord(c) for c in plaintext]

    S = KSA(key)
    keystream = PRGA(S)

    # XOR plaintext with keystream to get ciphertext
    ciphertext = []
    for char in plaintext:
        val = char ^ next(keystream)
        ciphertext.append(val)

    # Return ciphertext as hexadecimal string
    return ''.join([format(c, '02X') for c in ciphertext])


# Function to encrypt and decrypt using RC4
def encrypt_decrypt_rc4(key, word):
    encrypted = RC4(key, word)
    # To decrypt, simply run RC4 on the encrypted hex as ASCII values
    decrypted = ''.join([chr(int(encrypted[i:i + 2], 16)) for i in range(0, len(encrypted), 2)])
    decrypted_word = RC4(key, decrypted)
    return encrypted, decrypted_word


# Main function to run the RC4 algorithm
def main():
    key = "CRYPTO"
    plaintext = "ATLANTIS"

    print(f"Key: {key}")
    print(f"Plaintext: {plaintext}")

    encrypted, decrypted = encrypt_decrypt_rc4(key, plaintext)

    print(f"Encrypted (Hex): {encrypted}")
    print(f"Decrypted: {decrypted}")


if __name__ == "__main__":
    main()
