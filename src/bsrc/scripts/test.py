import random
import hashlib
import os

letters = "ABCEFGHIKLKMNOPQRSTUVWXYZ"
letters2 = "abcdefghijklmnopqrstuvwxyz"
numbers = "123456890"
speical_char = ""

# needs actual random generation that can derrive to itself

def ed25519_keypair():
    # return a 32 byte random
    seed = os.urandom(32) # os.urandom instead of randint for cryptographic security
    h = hashlib.sha512(seed).digest() # hash the seed using SHA-512 (64 bytes)
    h_low = bytearray(h[:32]) # take the lower 32 bytes

    # clamp the scalar bits (per RFC 8032) 
    h_low[0] &= 248
    h_low[31] &= 127
    h_low[31] |= 64

    a = int.from_bytes(h_low, "little") # the scalar 'a' is little-endian integer

    print("ED KEYPAIR:")
    print("Seed:         ", seed.hex())
    print("Hashed:       ", h.hex())
    print("Clamped low:  ", h_low.hex())
    print("Scalar (int): ", a)

    return seed, a

ed25519_keypair()

def return_random():
    return random.randint(0, 90000000)

public_key_a = hashlib.sha256(str(return_random()).encode('utf-8')).hexdigest()
public_key_b = hashlib.sha256(str(return_random()).encode('utf-8')).hexdigest()

private_key_a = hashlib.sha256(str(return_random()).encode('utf-8')).hexdigest()
private_key_b = hashlib.sha256(str(return_random()).encode('utf-8')).hexdigest()

print("\n")
print("Public key A:", public_key_a)
print("Private key A: ", private_key_a)
print("\n")
print("Public key B:", public_key_b)
print("Private key B: ", private_key_b)