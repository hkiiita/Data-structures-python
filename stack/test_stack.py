import unittest
from stack_implementation import Stack


class TestStack(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertTrue(self.stack.is_empty())

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1)
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_peek(self):
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)

    # Tests for an empty stack
    def test_empty_stack_pop(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.peek()


if __name__ == '__main__':
    unittest.main()
