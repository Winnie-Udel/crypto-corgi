from bakery import assert_equal

ENTER_HASH = "Please enter the hashed value to your encrypted message."
ERROR = "There's been an error. Please try again."
PRINTABLES_OFFSET = 32
PRINTABLES_LENGTH = 94
ROTATION_AMOUNT = 2
BASE = 31
HASH_SIZE = 1000000000

def convert_to_ascii(message: str) -> list[int]:
    """
    This function converts each character in a message to
    its corresponding ASCII code. The resulting ASCII code
    is then appended to a list.

    Args:
        message (str): Plaintext message needed to be converted
        to a list of ASCII codes.

    Returns:
        list[int]: List of ASCII codes.
    """
    codes = []
    for character in message:
        codes.append(ord(character))
    return codes


def rotation(codes: list[int], rotation_amount: int) -> list[int]:
    """
    This function rotates each ASCII code in a list of ASCII codes
    by the specified amount.

    Args:
        codes (list[int]): List of ASCII codes.
        rotation_amount (int): Amount of rotation, moving forward
        or backward, corresponding to the ASCII code.

    Returns:
        list[int]: List of ASCII codes after rotation.
    """
    rotated_codes = []
    for code in codes:
        rotated = (code + rotation_amount - PRINTABLES_OFFSET) % PRINTABLES_LENGTH + PRINTABLES_OFFSET
        rotated_codes.append(rotated)
    return rotated_codes


def insert_tilde(codes: list[int]) -> list[int]:
    """
    This function inserts tilde ASCCI code (126,
    translated to "~") after every ASCII code less than 48
    in a list of ASCII codes.

    Args:
        code (list[int]): List of ASCII codes.

    Returns:
        list[int]: List of ASCII codes with inserted tilde.
    """
    new_codes = []
    for code in codes:
        if code >= 48:
            new_codes.append(code)
        elif code < 48:
            new_codes.append(code)
            new_codes.append(126)
    return new_codes


def remove_tilde(codes: list[int]) -> list[int]:
    """
    This function removes tilde ASCCI code (126) in a list of
    ASCII codes.

    Args:
        codes (list[int]): List of ASCII codes.

    Returns:
        list[int]: List of ASCII codes with removed tilde.
    """
    new_codes = []
    for code in codes:
        if code != 126:
            new_codes.append(code)
    return new_codes


def encrypt_text(message: str, rotation_amount: int) -> str:
    """
    This function encrypts a message based on the given rotation
    amount.

    Args:
        message (str): Plaintext message needed to be encrypted.
        rotation_amount (int): Amount of rotation, moving forward
        or backward, corresponding to the ASCII code.

    Returns:
        str: Encrypted message.
    """
    encrypted_text = ""
    encrypted_codes = insert_tilde(rotation(convert_to_ascii(message), rotation_amount))
    for code in encrypted_codes:
        encrypted_text += chr(code)
    return encrypted_text


def decrypt_text(message: str, rotation_amount: int) -> str:
    """
    This function decrypts an encrypted message based on the
    given rotation amount.

    Args:
        message (str): Encrypted message needed to be decrypted.

    Returns:
        str: Decrypted message.
    """
    decrypted_text = ""
    decrypted_codes = rotation(remove_tilde(convert_to_ascii(message)), -rotation_amount)
    for code in decrypted_codes:
        decrypted_text += chr(code)
    return decrypted_text


def transform_ascii(codes: list[int], base: int) -> list[int]:
    """
    This function transforms each ASCII code in a list of ASCII codes
    into a list of new values by applying the following formula:
    new value = (index + base) ** (old value).

    Args:
        codes (list[int]): List of ASCII codes.
        base (int): Chosen base to apply to our formula to create a
        new value.

    Returns:
        list[int]: List of new values after applying our formula.
    """
    new_values = []
    for index, code in enumerate(codes):
        new_value = (index + base) ** (code)
        new_values.append(new_value)
    return new_values


def sum_values(values: list[int]) -> int:
    """
    This function sums all the values in a list.

    Args:
        values (list[int]): A list of values needed to be summed.

    Returns:
        int: Sum of the values.
    """
    summated = 0
    for value in values:
        summated += value
    return summated


def hash_text(message: str, base: int, hash_size: int) -> int:
    """
    This function consumes a message, base, and hash size and produces
    a unique hash value that represents the message.

    Args:
        message (str): Plaintext message needed to be hashed.
        base (int): Chosen base to apply to our formula to create a
        new value.
        hash_size (int): A number that we based our hashing on.

    Returns:
        int: Hash of the message.
    """
    hashed_value = sum_values(transform_ascii(convert_to_ascii(message), base)) % hash_size
    return hashed_value


# 4) Define main
def main():
    """
    This function permits the user to input their desired action, either
    encrypt or decrypt. The function prints out the encrypted message and
    hash value it to the user after the user inputs their desired message.
    If the user enters 'decrypt', the user is prompted to input their
    encrypted message and the hash value. If the user hash value and the
    computed hash value match, the function prints out the decrypted message.
    """
    user_action = input("INSTRUCTION")
    if user_action == "encrypt":
        user_message = input("ENCRYPTING_MESSAGE")
        encrypted_text = encrypt_text(user_message, ROTATION_AMOUNT)
        hashed_value = hash_text(user_message, BASE, HASH_SIZE)
        print("Encrypted message:", encrypted_text)
        print("Hash value:", hashed_value)
    elif user_action == "decrypt":
        user_message = input("DECRYPTING_MESSAGE")
        user_hash = input(ENTER_HASH)
        decrypted_text = decrypt_text(user_message, ROTATION_AMOUNT)
        actual_hash = str(hash_text(decrypted_text, BASE, HASH_SIZE))
        if user_hash == actual_hash:
            print("Decrypted message:", decrypted_text)
        else:
            print(ERROR)
    else:
        print(ERROR)


#main()
"""
assert_equal(convert_to_ascii("Hi!"), [72, 105, 33])
assert_equal(rotation(convert_to_ascii("Hi!"), 1), [73, 106, 34])
assert_equal(insert_tilde(convert_to_ascii("Hi!")), [72, 105, 33, 126])
assert_equal(encrypt_text("Dragons!", 10), "N|kqyx}+~")
assert_equal(remove_tilde([72, 105, 33, 126]), [72, 105, 33])
assert_equal(decrypt_text("N|kqyx}+~", 10), "Dragons!")
assert_equal(transform_ascii([33, 34], 1), [1, 17179869184])
assert_equal(sum_values([33, 34]), 67)
assert_equal(hash_text("Hello", 31, 1000000000), 590934605)
"""