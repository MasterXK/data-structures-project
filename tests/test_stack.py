"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Stack
import unittest


class TestStack(unittest.TestCase):
    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        data = stack.pop()

        self.assertEqual(data, 'data2')

        data = stack.pop()

        self.assertIs(stack.top, None)

        self.assertEqual(data, 'data1')

    def test_str(self):
        stack = Stack()

        self.assertEqual(str(stack), '')

        stack.push('data1')
        stack.push('data2')

        self.assertEqual(str(stack), 'data2\ndata1')
