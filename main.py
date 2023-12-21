from drafter import *
from dataclasses import dataclass

@dataclass
class State:
    pass

@route
def index(state: State) -> Page:
    return Page(state, [
        Header("Crypto Corgi"),
        HorizontalRule()
    ])

start_server(State())