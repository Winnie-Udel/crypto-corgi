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
    return Page(state, [
        Header("Crypto Corgi"),
        """
        Welcome to Crypto Corgi! Need to encrypt or decrypt a message? Well, you 
        came to the right place! All you need to do is press the buttons below! 
        """,
        HorizontalRule(),
        Button("Encryption", encryption),
        Button("Decryption", decryption),
        Button("Setting", setting)
    ])

@route
def encryption(state: State) -> Page:
    return Page(state, [
        Header("Encryption"),
        "Please enter your desired message to be encrypted!",
        HorizontalRule(),
        TextBox("user_message", state.user_message),
        "Encrypted message: " + state.encrypted_message,
        "Hash value: " + state.hash_value,
        Button("Submit", encryption_updating),
        Button("Return Home", default_index)
    ])

@route
def encryption_updating(state: State, user_message: str):
    state.user_message = user_message
    state.encrypted_message = encrypt_text(user_message, state.rotation_amount)
    hash_value = hash_text(user_message, BASE, HASH_SIZE)
    state.hash_value = str(hash_value)
    return encryption(state)

@route
def default_index(state: State):
    state.user_message = ""
    state.encrypted_message = ""
    state.hash_value = ""
    return index(state)

@route
def decryption(state: State) -> Page:
    return Page(state, [
        Header("Decryption"),
        "Please enter your encrypted message to be decrypted!",
        HorizontalRule()
    ])

@route
def setting(state: State) -> Page:
    return Page(state, [
        Header("Setting"),
        HorizontalRule()
    ])

start_server(State(2, "", "", ""))