"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Stack


def test_pop():
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    data = stack.pop()

    assert data == 'data2'

    data = stack.pop()

    assert stack.top is None

    assert data == 'data1'
