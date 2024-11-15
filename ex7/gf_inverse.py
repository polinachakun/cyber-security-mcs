def gf_degree(a):
    """
    Returns the degree of the polynomial represented by integer 'a'.
    """
    if a == 0:
        return -1
    return a.bit_length() - 1

def gf_poly_mul(a, b):
    """
    Multiplies two polynomials a and b over GF(2).
    """
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        b >>= 1
    return result

def gf_poly_divmod(a, b):
    """
    Performs polynomial division of a by b over GF(2), returning the quotient and remainder.
    """
    deg_b = gf_degree(b)
    q = 0
    r = a
    while gf_degree(r) >= deg_b and r != 0:
        shift = gf_degree(r) - deg_b
        q ^= 1 << shift
        r ^= b << shift
    return q, r

def gf_poly_egcd(a, b):
    """
    Extended Euclidean Algorithm for polynomials over GF(2).
    Returns gcd, x, y such that gcd = x*a + y*b
    """
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    while b != 0:
        q, _ = gf_poly_divmod(a, b)
        a, b = b, a ^ gf_poly_mul(q, b)
        x0, x1 = x1, x0 ^ gf_poly_mul(q, x1)
        y0, y1 = y1, y0 ^ gf_poly_mul(q, y1)
    return a, x0, y0

def gf_inv(a):
    """
    Finds the multiplicative inverse of a in GF(2^8) using the Extended Euclidean Algorithm.
    """
    if a == 0:
        raise ValueError("Zero has no multiplicative inverse in GF(2^8).")
    modulus = 0x11b  # Irreducible polynomial x^8 + x^4 + x^3 + x + 1
    gcd, x, _ = gf_poly_egcd(a, modulus)
    if gcd != 1:
        raise ValueError("No multiplicative inverse exists.")
    inverse = x & 0xFF
    return inverse

def gf_mul(a, b):
    """
    Multiplies two elements in GF(2^8) modulo the AES irreducible polynomial.
    """
    result = 0
    for _ in range(8):
        if b & 1:
            result ^= a
        carry = a & 0x80
        a <<= 1
        if carry:
            a ^= 0x11b
        a &= 0xFF
        b >>= 1
    return result

def main():
    while True:
        try:
            input_str = input("Enter a byte value (or 'exit' to quit): ").strip()
            if input_str.lower() == 'exit':
                print("Exiting the program.")
                break
            input_byte = int(input_str, 0)
            if not (0 < input_byte < 256):
                print("Input byte must be in range 1..255")
                continue
            inverse_byte = gf_inv(input_byte)
            print(f"The multiplicative inverse of {hex(input_byte)} in GF(2^8) is {hex(inverse_byte)}")
            product = gf_mul(input_byte, inverse_byte)
            print(f"Verification: {hex(input_byte)} * {hex(inverse_byte)} = {hex(product)}\n")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid integer between 1 and 255.\n")

if __name__ == "__main__":
    main()
