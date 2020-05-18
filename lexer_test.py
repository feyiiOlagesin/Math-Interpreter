import unittest
from tokens import Token, TokenType
from lexer import Lexer

class TestLexer(unittest.TestCase):

    def test_emptyString(self):
        tokens = list(Lexer("").generate_tokens())
        self.assertEqual(tokens, [])

    def test_emptyString(self):
        tokens = list(Lexer(" \t\n \t\t\n\n").generate_tokens())
        self.assertEqual(tokens, [])

    def test_numbers(self):
        tokens = list(Lexer("123 123.456 123. .456 .").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 123.000),
            Token(TokenType.NUMBER, 123.456),
            Token(TokenType.NUMBER, 123.000),
            Token(TokenType.NUMBER, 000.456),
            Token(TokenType.NUMBER, 000.000),
        ])

    def test_operators(self):
        tokens = list(Lexer("+-*/").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.PLUS),
            Token(TokenType.MINUS),
            Token(TokenType.MULTIPLY),
            Token(TokenType.DIVIDE),
        ])

    def test_parenthesis(self):
        tokens = list(Lexer("()").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.LEFT_PARENTHESIS),
            Token(TokenType.RIGHT_PARENTHESIS),
        ])

    def test_all(self):
        tokens = list(Lexer("27 + (10 - 2) / 3 * 1").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.PLUS),
            Token(TokenType.LEFT_PARENTHESIS),
            Token(TokenType.NUMBER, 10),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 2),
            Token(TokenType.RIGHT_PARENTHESIS),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 3),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 1),
        ])