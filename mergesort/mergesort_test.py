import unittest
import mergesort


class MergeSortTestCase(unittest.TestCase):

    def test_sort(self):
        unsorted = [1, 9, 4, 3, 8, 7, 2, 5, 0, 6]
        mergesorted = mergesort.sort(unsorted)

        self.assertEqual(mergesorted, sorted(unsorted))

    def test_merge(self):
        left = [1, 2, 3, 9]
        right = [4, 5, 6, 7, 8]

        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9],
                         mergesort.merge(left, right))


if __name__ == '__main__':
    unittest.main()
