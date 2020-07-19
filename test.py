import unittest
from command import FirstPrimesCommand, SortAndCombineCommand

class TestFirstPrimesCommand(unittest.TestCase):
    def test_zero_primes(self):
        command = FirstPrimesCommand(0)
        actual = command.execute()
        self.assertEqual(len(actual), 0)
    
    def test_invalid_input_throw_error(self):
        with self.assertRaises(ValueError):
            command = FirstPrimesCommand(-1)

    def test_first_primes(self):
        command = FirstPrimesCommand(10)
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        actual = command.execute()
        self.assertEqual(actual, expected)

class TestSortAndCombineCommand(unittest.TestCase):
    def test_sort_and_combine_first_longer(self):
        command = SortAndCombineCommand([4, 3, 6, 5, 1, 2], ['F', 'C', 'D', 'B', 'A'])
        expected = [['1:A'], ['2:B'], ['3:C'], ['4:D'], ['5:F'], ['6:NULL']]
        actual = command.execute()
        self.assertEqual(actual, expected)
    
    def test_sort_and_combine_second_longer(self):
        command = SortAndCombineCommand([4, 3, 5, 1, 2], ['F', 'C', 'D', 'B', 'A', 'E'])
        expected = [['1:A'], ['2:B'], ['3:C'], ['4:D'], ['5:E'], ['NULL:F']]
        actual = command.execute()
        self.assertEqual(actual, expected)

    def test_sort_and_combine_same_length(self):
        command = SortAndCombineCommand([4, 3, 5, 1, 2, 6], ['F', 'C', 'D', 'B', 'A', 'E'])
        expected = [['1:A'], ['2:B'], ['3:C'], ['4:D'], ['5:E'], ['6:F']]
        actual = command.execute()
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
