PRINTABLES_OFFSET = 32
PRINTABLES_LENGTH = 94

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