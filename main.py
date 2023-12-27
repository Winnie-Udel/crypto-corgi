from drafter import *
from dataclasses import dataclass
from helpers import *

@dataclass
class State:
    user_message: str
    encrypted_message: str

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
        Button("Submit", update_page)
    ])

@route
def update_page(state: State, user_message: str):
    state.encrypted_message = encrypt_text(user_message, ROTATION_AMOUNT)
    return encryption(state)

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

start_server(State("", ""))