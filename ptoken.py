import enum

class Location(object):
    def __new__(cls, arg1, arg2):
        return super().__new__(cls)

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __str__(self):
        return f'start({self.start}) end({self.end})'

class Token(object):
    def __init__(self, tag: int, location: Location, data: str = None):
        self.pos = location
        self.tag = tag
        self.data = data

    def __str__(self):
        return f"TOKEN type({self.tag}) data({self.data}) pos({self.pos.start},{self.pos.end}))"

class Tag(enum.Enum):
    IDENTIFIER = enum.auto()
    
    LEFT_PAREN= enum.auto()
    LEFT_BRACE= enum.auto()
    RIGHT_BRACE= enum.auto()
    RIGHT_PAREN= enum.auto()
    WHITESPACE= enum.auto()
    SINGLE_QUOTE= enum.auto()
    DOUBLE_QUOTE= enum.auto()
    COMMA =  enum.auto()
    DOT =  enum.auto()
    MINUS = enum.auto()
    PLUS = enum.auto()
    SEMICOLON= enum.auto()
    SLASH= enum.auto()
    STAR= enum.auto()
    
    EQUAL= enum.auto()
    BANG= enum.auto()
    BANG_EQUAL= enum.auto()
    EQUAL_EQUAL= enum.auto()
    LESS_EQUAL= enum.auto()
    LESS_THAN= enum.auto()
    GREATER_THAN= enum.auto()
    GREATER_EQUAL= enum.auto()
    
    STRING= enum.auto()
    NUMBER =enum.auto()
        
    KW_LET =  enum.auto()
    KW_PRINT= enum.auto()
    
    
    EOF =  enum.auto()
    KW_UNSUPPORTED =  enum.auto()


class BuiltIn(object):
    @staticmethod
    def get(keyword):
        keywords = {
            "print": Tag.KW_PRINT,
            "let": Tag.KW_LET,
        }

        kw = keywords.get(keyword)

        if kw != None:
            return kw

        return Tag.KW_UNSUPPORTED

        