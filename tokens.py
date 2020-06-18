#tokens using enums

from enum import Enum
from dataclasses import dataclass

#using enums to distinguish the various token types
class TokenType(Enum):
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    LEFT_PARENTHESIS = 5
    RIGHT_PARENTHESIS = 6

@dataclass
class Token:
    type: TokenType
    value: any = None

    #Representation method
    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value != None else "")

 