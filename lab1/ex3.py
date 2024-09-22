from math import gcd
from functools import reduce


# Function to calculate the least common multiple (LCM)
def lcm(a, b):
    return abs(a * b) // gcd(a, b)


# Function to find the LCM for a list of numbers
def lcm_multiple(numbers):
    return reduce(lcm, numbers)


# Given plain and cipher alphabets
plain_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher_alphabet = "SNPUJCMGOVLZWHKXFDABRITQEY"


# Function to find the cycles in the substitution cipher
def find_cycles(plain_alphabet, cipher_alphabet):
    visited = set()  # Set to track visited letters
    cycles = []  # List to store the length of each cycle

    # Iterate through all the letters in the alphabet
    for i in range(len(plain_alphabet)):
        if plain_alphabet[i] not in visited:
            cycle = []  # Start a new cycle
            current_letter = plain_alphabet[i]

            # Continue until we return to the original letter
            while current_letter not in visited:
                visited.add(current_letter)
                cycle.append(current_letter)
                # Find the next letter using the cipher
                next_letter = cipher_alphabet[plain_alphabet.index(current_letter)]
                current_letter = next_letter

            # Add the length of the cycle
            cycles.append(len(cycle))

    return cycles


# Find the cycles in the given cipher
cycles = find_cycles(plain_alphabet, cipher_alphabet)

# Calculate the LCM of the cycle lengths
cycle_length = lcm_multiple(cycles)

if __name__ == "__main__":
    print("Cycle lengths:", cycles)
    print("Number of distinct words before repetition:", cycle_length)
