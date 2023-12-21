from drafter import *
from dataclasses import dataclass

@dataclass
class State:
    pass

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
        HorizontalRule()
    ])

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

start_server(State())