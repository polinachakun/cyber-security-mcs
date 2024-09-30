import numpy as np
from collections import Counter

# Function to convert a binary string to an array of numbers
def binary_str_to_array(binary_str):
    return np.array([int(bit) for bit in binary_str])

# XOR function for two arrays
def xor_binary_arrays(arr1, arr2):
    return np.bitwise_xor(arr1, arr2)

# Function to decrypt a ciphertext using XOR and the found key
def decrypt_ciphertext(ciphertext, keystream):
    return xor_binary_arrays(ciphertext, keystream)

def main():
    # Ciphertexts (as binary strings)
    ciphertexts = [
        "00010111011000110010010110100011",
        "11001101001111101100100011000110",
        "10100111111110110000100100001101",
        "01100100001110111001000101101000",
        "00110101010011010001100010011001",
        "10110101100100101001111111101110",
        "00111011101111110001011100011001",
        "11011011101101101111100111101111",
        "00110101101100101110011110011001"
    ]

    # Possible plaintext messages (as binary strings)
    messages = [
        "11111111000000001111111100000000",
        "01010101010101010101010101010101",
        "11011101001011101100001000111010",
        "01101101101101101110111010010100",
        "11110001111100101111000010000000",
        "00001111000011110000111100001111",
        "11111111111111110000000000000000",
        "00010001111110110001111001110110",
        "10101110011101100111011011110001",
        "01111111110111110111100001110111"
    ]

    # Convert binary strings to arrays of numbers
    ciphertexts_array = [binary_str_to_array(c) for c in ciphertexts]
    messages_array = [binary_str_to_array(m) for m in messages]

    # Find possible keys by XORing each ciphertext with each possible message
    possible_keys = {}

    # Iterate through all ciphertexts
    for i, ciphertext in enumerate(ciphertexts_array):
        # For each ciphertext, iterate through all possible messages
        for j, message in enumerate(messages_array):
            # Apply XOR between ciphertext and possible message to find the key
            key = xor_binary_arrays(ciphertext, message)
            # Store the key as a binary string for each combination
            key_str = ''.join(map(str, key))
            possible_keys[f"Key for c{i} and m{j}"] = key_str

    # Count the occurrences of each key to find repeating ones
    key_counter = Counter(possible_keys.values())

    # Identify the most frequent key
    most_common_key, most_common_key_count = key_counter.most_common(1)[0]

    # Now try to decrypt as many messages as possible using the most common key
    decrypted_messages_with_common_key = {}
    common_key_array = binary_str_to_array(most_common_key)

    # Decrypt all ciphertexts using the most common key
    for i, ciphertext in enumerate(ciphertexts_array):
        decrypted_message = decrypt_ciphertext(ciphertext, common_key_array)
        decrypted_messages_with_common_key[f"Decrypted c{i}"] = ''.join(map(str, decrypted_message))

    # Output the results
    print("All possible keys:")
    for key, value in possible_keys.items():
        print(f"{key}: {value}")

    print("\nRepeating keys:")
    for key, count in key_counter.items():
        if count > 1:
            print(f"Key: {key} - Count: {count}")

    print(f"\nMost common key: {most_common_key} - Occurrences: {most_common_key_count}")

    print("\nDecrypted messages using the most common key:")
    for msg, value in decrypted_messages_with_common_key.items():
        print(f"{msg}: {value}")

# Call the main function
if __name__ == "__main__":
    main()
