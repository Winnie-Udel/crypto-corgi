from drafter import *
from dataclasses import dataclass
from helpers import *

BASE = 31
HASH_SIZE = 1000000000

@dataclass
class State:
    rotation_amount: int
    user_message: str
    encrypted_message: str
    hash_value: str
    decrypted_message: str

@route
def index(state: State) -> Page:
    """
    Displays the front page, which consists of the website's banner, links that
    redirect the user to the encryption or decryption page, and a button that
    directs the user to the settings page.

    Args:
        state (State): New values of the page that is hidden from the user.

    Returns:
        Page: Composed of the required information needed for a viewable webpage.
    """
    # Reset the value of all fields except for the rotation amount to default
    state.user_message = ""
    state.encrypted_message = ""
    state.hash_value = ""
    state.decrypted_message = ""
    return Page(state, [
        Image("http://tinyurl.com/3ct5zznh", 600, 120),
        LineBreak(),
        """
        Welcome! Need to encrypt or decrypt a message? Well, you came to the 
        right place!
        """,
        HorizontalRule(),
        Link("Encryption", encryption),
        "Encrypt messages based on the rotation amount.",
        BulletedList(["Input: Message",
                      "Output: Encrypted Message and Hash Value"]),
        HorizontalRule(),
        Link("Decryption", decryption),
        "Decrypt encrypted messages based on the rotation amount.",
        BulletedList(["Input: Encrypted Message and Hash Value",
                      "Output: Decrypted Message"]),
        HorizontalRule(),
        Button("Setting", setting)
    ])

@route
def encryption(state: State) -> Page:
    """
    Displays the encryption page, which consists of a header, instructions, textbox,
    table, and buttons. After the user enters a message, and presses the "Submit"
    button, the encrypted message and hash value are outputted to the table.

    Args:
        state (State): New values of the page that is hidden from the user.

    Returns:
        Page: Composed of the required information needed for a viewable webpage.
    """
    return Page(state, [
        Header("Encryption", 3),
        "Rotation Amount: " + str(state.rotation_amount),
        HorizontalRule(),
        "Please enter your desired message to be encrypted!",
        TextBox("user_message", state.user_message),
        HorizontalRule(),
        Table([["Encrypted Message", "Hash Value"],
               [state.encrypted_message, state.hash_value]]),
        HorizontalRule(),
        Button("Submit", update_encryption),
        Button("Return Home", index, float="right")
    ])

@route
def update_encryption(state: State, user_message: str) -> Page:
    """
    Update the information on the encryption page.

    Args:
        state (State): New values of the page that is hidden from the user.
        user_message (str): User message that needed to be encrypted.

    Returns:
        Page: Composed of the required information needed for a viewable webpage.
    """
    state.user_message = user_message
    state.encrypted_message = encrypt_text(user_message, state.rotation_amount)
    hash_value = hash_text(user_message, BASE, HASH_SIZE)
    state.hash_value = str(hash_value)
    return encryption(state)

@route
def decryption(state: State) -> Page:
    """
    Displays the decryption page, which consists of a header, instructions, textboxes,
    table, and buttons. When the user enters the encrypted message and hash value, and
    then presses the "Submit" button, the decrypted message is outputted if the
    user-inputted hash value matches the computed hash value.

    Args:
        state (State): New values of the page that is hidden from the user.

    Returns:
        Page: Composed of the required information needed for a viewable webpage.
    """
    return Page(state, [
        Header("Decryption", 3),
        "Rotation Amount: " + str(state.rotation_amount),
        HorizontalRule(),
        "Please enter your encrypted message to be decrypted!",
        TextBox("encrypted_message", state.encrypted_message),
        "Please enter the hash value to your encrypted message!",
        TextBox("hash_value", state.hash_value),
        HorizontalRule(),
        Table([["Decrypted Message"],
               [state.decrypted_message]]),
        HorizontalRule(),
        Button("Submit", update_decryption),
        Button("Return Home", index, float="right")
    ])

@route
def update_decryption(state: State, encrypted_message: str, hash_value: str) -> Page:
    """
    Update the information on the decryption page. If the user-inputted hash value
    matches the computed hash value, we return to the decryption page. Else, the
    user is directed to an error page.

    Args:
        state (State): New values of the page that is hidden from the user.
        encrypted_message (str): User-inputted encrypted message that needed to
        be decrypted.
        hash_value (str): User-inputted hash value in a string format.

    Returns:
        Page: Composed of the required information needed for a viewable webpage.
    """
    state.encrypted_message = encrypted_message
    state.hash_value = hash_value
    decrypted_message = decrypt_text(encrypted_message, state.rotation_amount)
    computed_hash_value = str(hash_text(decrypted_message, BASE, HASH_SIZE))
    if hash_value == computed_hash_value:
        state.decrypted_message = decrypted_message
        return decryption(state)
    else:
        return error(state)

@route
def error(state: State) -> Page:
    return Page(state, [
        "There's been an error. Please try again."
    ])

@route
def setting(state: State) -> Page:
    """
    Displays the setting page, which consists of a header, a select box, and a
    "Return Home" button. On this page, the user can adjust the rotation amount
    (1-10) using the select box.

    Args:
        state (State): New values of the page that is hidden from the user.

    Returns:
        Page: Composed of the required information needed for a viewable webpage.
    """
    rotation_amount = str(state.rotation_amount)
    return Page(state, [
        Header("Setting", 3),
        HorizontalRule(),
        "Set the rotation amount.",
        SelectBox("rotation_amount",
                  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
                  rotation_amount),
        HorizontalRule(),
        Button("Return Home", update_setting, float="right")
    ])

@route
def update_setting(state: State, rotation_amount: str) -> Page:
    """
    Update the value of the rotation_amount of the State dataclass. Returns back to
    the front page (index page).

    Args:
        state (State): New values of the page that is hidden from the user.
        rotation_amount (str): Selected rotation amount.

    Returns:
        Page: Composed of the required information needed for a viewable webpage.
    """
    state.rotation_amount = int(rotation_amount)
    return index(state)

start_server(State(2, "", "", "", ""))