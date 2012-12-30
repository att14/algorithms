import unittest
import mergesort


class MergeSortTestCase(unittest.TestCase):

    def test_merge_sort(self):
        unsorted = [1, 9, 4, 3, 8, 7, 2, 5, 0, 6]
        mergesorted = mergesort.sort(unsorted)

        self.assertEqual(mergesorted, sorted(unsorted))


if __name__ == '__main__':
    unittest.main()
