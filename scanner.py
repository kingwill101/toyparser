from ptoken import Tag, Location, Token, BuiltIn
import io


class Scanner(object):
    current = -1
    source_lengh = 0
    tokens = []
    start =0

    def __init__(self, source: bytes) -> None:
        self.source = source
        self.source_lengh = len(self.source)

    def peek(self):
        if self.isAtEnd() or (self.current +1) >= self.len():
            return '\n'

        return self.charAt(self.current + 1)

    def peekNext(self):
        if self.isAtEnd() or (self.current +1 >= self.len()):
            return '\n'
        return self.charAt(self.current + 2)

    def len(self):
        return self.source_lengh

    def __addToken(self, tag:Tag):
        self.__addTokenWithValue(tag, None)

    def __addTokenWithValue(self, tag: Tag, value: str):
        self.tokens.append(Token(tag, Location(self.start, self.current), value))

    def isAtEnd(self):
        if self.current == self.len() -1:
            return True
        return False
        
    def scanTokens(self):
        while not self.isAtEnd():
            self.start = self.current
            self.__scanToken()
        self.__addToken(Tag.EOF)
        return
    
    def __scanToken(self):
        char = self.advance()
        if char == "(":
            self.__addToken(Tag.LEFT_PAREN)

        elif char == ")":
            self.__addToken(Tag.RIGHT_PAREN)

        elif char == "{":
            self.__addToken(Tag.LEFT_BRACE)

        elif char == "}":
            self.__addToken(Tag.RIGHT_BRACE)

        elif char == ',':
            self.__addToken(Tag.COMMA)

        elif char == '.':
            self.__addToken(Tag.DOT)

        elif char == '-':
            self.__addToken(Tag.MINUS)

        elif char == '+':
            self.__addToken(Tag.PLUS)

        elif char == ';':
            self.__addToken(Tag.SEMICOLON)

        elif char == '*':
            self.__addToken(Tag.STAR)

        elif char == '=':
            if self.match("="):
              self.__addToken(Tag.EQUAL_EQUAL)
              return

            self.__addToken(Tag.EQUAL)

        elif char == '<':
            if self.match("="):
              self.__addToken(Tag.LESS_EQUAL)
              return

            self.__addToken(Tag.LESS_THAN)

        elif char == '>':
            if self.match("="):
              self.__addToken(Tag.GREATER_EQUAL)
              return

            self.__addToken(Tag.GREATER_THAN)

        elif char == "/":
            self.__addToken(Tag.SLASH)

        elif char == "'":
            self.string()
            return
        elif char in [' ', '\r', '\t']:
            return
        
        elif char == "!":
            if self.match("="):
                self.__addToken(Tag.BANG_EQUAL)
                return 

            self.__addToken(Tag.BANG)

        elif self.isAlpha(char):
            self.identifier()
        
        elif self.isDigit(char):
            self.number()
    
    def charAt(self, index):
        return chr(self.source[index])
        
    def identifier(self):
        word = self.charAt(self.current)

        while not self.isAtEnd() and self.peek() != " ":
            word += self.advance()
            if self.peek() == '\n':
                break

        if BuiltIn.get(word) != Tag.KW_UNSUPPORTED:
            self.__addToken(BuiltIn.get(word))
        else:
            self.__addTokenWithValue(Tag.IDENTIFIER, word)

    def number(self):
        num = self.charAt(self.current)

        while self.isDigit(self.peek()):
            num += self.advance()

        #decimal numbers
        if(self.peek() == "." and self.isDigit(self.peekNext())):
            num += self.advance()
            while self.isDigit(self.peek()):
                num += self.advance()
                
        self.__addTokenWithValue(Tag.NUMBER, num)
        return

    def string(self):
        string = ""
        while not self.isAtEnd():
            if self.peek() == '\n' or self.peek() == "'":
                break
            string += self.advance()
        if self.isAtEnd():
            print("Unterminated string literal found")
            return 
        self.consume()
        self.__addTokenWithValue(Tag.STRING, string)
        return
       
    def consume(self, steps:int =1):
        self.current +=steps

    def isAlphaNumeric(self, val):
       return self.isAlpha(val) or self.isDigit(val)

    def isAlpha(self, val):
        ascii_num = ord(val)

        if ascii_num >= 65  and ascii_num <=90:
            return True
        
        if ascii_num >= 97  and ascii_num <=122:
            return True

    def isDigit(self, val):
        
        ascii_num = ord(val)
        if(ascii_num >= 48  and ascii_num <=57):
            return True
        
        return False
        
    def advance(self):
        self.current += 1
        byte_char = self.source[self.current]
        return chr(byte_char)

    def match(self, val):
        if self.isAtEnd():
            return False
        if self.peek() != val:
            return False
        
        self.consume()
        return True
