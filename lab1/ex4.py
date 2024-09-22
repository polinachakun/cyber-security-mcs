# Step 1: Function to generate the key matching the length of the plaintext
def generate_key(plaintext, key):
    key = list(key)
    if len(plaintext) == len(key):
        return key
    else:
        # If the key is shorter, repeat it to match the length of the plaintext
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


# Step 2: Function to encrypt the plaintext using Vigenère cipher
def vigenere_encrypt(plaintext, key):
    encrypted_text = []
    key = generate_key(plaintext, key)  # Match key length to plaintext
    for i in range(len(plaintext)):
        # Convert both the plaintext and key characters to numbers (A = 0, B = 1, etc.)
        p = ord(plaintext[i]) - ord('A')
        k = ord(key[i]) - ord('A')

        # Apply the Vigenère cipher shift
        encrypted_char = (p + k) % 26  # Ensure the result wraps around using mod 26

        # Convert back to character and append to the encrypted text list
        encrypted_text.append(chr(encrypted_char + ord('A')))

    return "".join(encrypted_text)  # Join the list into a final string


# Step 3: Define the plaintext and key based on your student number
plaintext = "MAYTHEFORCEBEWITHYOU"  # Given plaintext
key = "AAFBC"  # The key derived from the last 5 digits of your student number (00512 -> AAFBC)

# Step 4: Encrypt the plaintext using the Vigenère cipher
encrypted_message = vigenere_encrypt(plaintext, key)

# Step 5: Output the result
if __name__ == "__main__":
    print(f"Encrypted Message: {encrypted_message}")