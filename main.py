from drafter import *
from dataclasses import dataclass
from helpers import *

@dataclass
class State:
    rotation_amount: int
    user_message: str
    encrypted_message: str
    hash_value: str

@route
def index(state: State) -> Page:
    state.user_message = ""
    state.encrypted_message = ""
    state.hash_value = ""
    return Page(state, [
        Header("Crypto Corgi", 2),
        """
        Welcome to Crypto Corgi! Need to encrypt or decrypt a message? Well, you 
        came to the right place!
        """,
        HorizontalRule(),
        Link("Encryption", encryption),
        "Encrypt messages based on the rotation amount.",
        BulletedList(["Input: Message", "Output: Encrypted Message and Hash Value"]),
        HorizontalRule(),
        Link("Decryption", decryption),
        "Decrypt encrypted messages based on the rotation amount.",
        BulletedList(["Input: Encrypted Message and Hash Value", "Output: Decrypted Message"]),
        HorizontalRule(),
        Button("Setting", setting)
    ])

@route
def encryption(state: State) -> Page:
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
def update_encryption(state: State, user_message: str):
    state.user_message = user_message
    state.encrypted_message = encrypt_text(user_message, state.rotation_amount)
    hash_value = hash_text(user_message, BASE, HASH_SIZE)
    state.hash_value = str(hash_value)
    return encryption(state)

@route
def decryption(state: State) -> Page:
    return Page(state, [
        Header("Decryption", 3),
        "Please enter your encrypted message to be decrypted!",
        HorizontalRule()
    ])

@route
def setting(state: State) -> Page:
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
def update_setting(state: State, rotation_amount: str):
    state.rotation_amount = int(rotation_amount)
    return index(state)

start_server(State(2, "", "", ""))