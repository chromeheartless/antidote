import os
import time
import random
import hashlib
from qrcode import generate_qr_ascii
from ed25519_pure import keygen

# key generation section

public_key_a, private_key_a, valid_status_a = keygen()
public_key_b, private_key_b, valid_status_b = keygen()

print("Public key A:", public_key_a)
print("Private key A:", private_key_a)
print("Keypair valid status: A", valid_status_a)

print("\n")

print("Public key B:", public_key_a)
print("Private key B:", private_key_a)
print("Keypair valid status: B", valid_status_a)

print("\n")

def get_ssn(message_sender_public_key):

    def strip_first_n(s, n):
        return s[:n]

    key_ssn = strip_first_n(message_sender_public_key, 12) #2 char for identifying user

    return key_ssn

# content encryption section

def encrypt(message_sender_public_key, message_receiver_public_key, message_content):

    degree_of_0f = (int.from_bytes(os.urandom(1), "big") % 9) + 1
    # os.urandom(1) gives a random byte from 0 to 255
    # int.from_bytes turns the byte into an integer
    # %9 reduces it to the range 0 to 8
    # and + 1 shifts it 1-9

    inaccuracy_identifyier = degree_of_0f

    binary = ''.join(format(ord(c), '08b') for c in message_content)
    content_length_binary = len(binary)
    
    return content_length_binary


def sign(message_sender_public_key, message_receiver_public_key, message):
    sender_public_key_cut_size = 8
    receiver_public_key_cut_size = 8
    
    part1_key_sig = ''
    part2_key_sig = ''

    for _ in range(sender_public_key_cut_size):
        # get a random byte, convert to an index in s
        index = ord(os.urandom(1)) % len(message_sender_public_key)
        part1_key_sig += message_sender_public_key[index]

    for _ in range(receiver_public_key_cut_size):
        # get a random byte, convert to an index in s
        index = ord(os.urandom(1)) % len(message_receiver_public_key)
        part2_key_sig += message_receiver_public_key[index]

    hashed_signature = hashlib.sha256((part1_key_sig + part2_key_sig).encode('utf-8')).hexdigest() # replace sha256 with non-brute forcabe algo
    content_signature = hashlib.sha256(message.encode('utf-8')).hexdigest() # replace sha256 with non-brute forcabe algo

    return hashed_signature, content_signature

def check_integrity(message):
    return True

# output section

message_content = """

"""

def shape(message_sender_public_key, message_receiver_public_key, message):
    
    top_marking = "========== BEGIN ANI MESSAGE ==========\n\n"
    bottom_marking = "\n\n  ==========  END MESSAGE  =========="

    encrypted_message = encrypt(message_sender_public_key, message_receiver_public_key, message)

    timestamp = time.strftime("%d:%m:%Y %H:%M:%S")
    message_timestamp = f"\n\nSender's clock timezone: {timestamp}"
    
    integrity_of_message = check_integrity(message)
    integrity = f"\nMessage integrity: {integrity_of_message}"

    message_sender = message_sender_public_key
    ssn = f"\nSender SSN: {get_ssn(message_sender_public_key)}"

    message_signature, content_signature = sign(message_sender_public_key, message_receiver_public_key, message)
    signature1 = f"\nMessage signature: {message_signature}"
    signature2 = f"\nContent signature: {content_signature}\n"

    signature2_qr = generate_qr_ascii(content_signature, return_string=True)
    output_message = f"{top_marking}{encrypted_message}{bottom_marking}{message_timestamp}{integrity}{ssn}{signature1}{signature2}{signature2_qr}"
    print(output_message)

shape(public_key_a, public_key_b, message_content) 



