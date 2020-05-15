from lexer import Lexer

while True:
    text = input("Math Interpreter> ")
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    print(list(tokens))