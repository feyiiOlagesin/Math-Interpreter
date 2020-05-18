import unittest
from tokens import Token, TokenType
from parser_ import Parser
from nodes import *

class TestParser(unittest.TestCase):
    
    def test_emptyString(self):
        tokens = []
        node = Parser(tokens).parse()
        self.assertEqual(node, None)

    def test_Numbers(self):
        tokens = [Token(TokenType.NUMBER, 51.2)]
        node = Parser(tokens).parse()
        self.assertEqual(node, NumberNode(51.2))

    def test_individual_operations(self):
        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 14)
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, AddNode(NumberNode(27), NumberNode(14)))



        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 14),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, SubtractNode(NumberNode(27), NumberNode(14)))


        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 14),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, MultiplyNode(NumberNode(27), NumberNode(14)))


        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 14),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, DivideNode(NumberNode(27), NumberNode(14)))

    def test_full_expression(self):
        # 27 + (10 - 2) / 3 * 1
        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 8)
            # Token(TokenType.NUMBER, 27),
            # Token(TokenType.PLUS),
            # Token(TokenType.LEFT_PARENTHESIS),
            # Token(TokenType.NUMBER, 10),
            # Token(TokenType.MINUS),
            # Token(TokenType.NUMBER, 2),
            # Token(TokenType.RIGHT_PARENTHESIS),
            # Token(TokenType.DIVIDE),
            # Token(TokenType.NUMBER, 3),
            # Token(TokenType.MULTIPLY),
            # Token(TokenType.NUMBER, 1),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, SubtractNode(
            NumberNode(27),
            NumberNode(8)
        ))
        # self.assertEqual(node, AddNode(
        #     NumberNode(27),
        #     MultiplyNode(
        #         DivideNode(
        #             SubtractNode(
        #                 NumberNode(10),
        #                 NumberNode(2)
        #             ),
        #             NumberNode(3)
        #         ),
        #         NumberNode(1)
        #     )
        # )
        # )
        # self.assertEqual(node, AddNode(
        #     NumberNode(27),
        #     DivideNode(
        #         SubtractNode(
        #             NumberNode(10),
        #             NumberNode(2)
        #         ),
        #         MultiplyNode(
        #             NumberNode(3),
        #             NumberNode(1)
        #         )
        #     )  
        # )
        # )