import unittest
from thechronic.strange import Strange


class StrangeTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_basic(self):
        srange = Strange(1, 10)
        self.assertEqual(len(list(srange)), 9)

        srange = list(Strange(1, 10))
        ran = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        self.assertTrue(isinstance(srange[0], str))
        self.assertCountEqual(srange, ran)

        srange = list(Strange(1, 10, 2))
        ran = ['1', '3', '5', '7', '9']

        self.assertTrue(isinstance(srange[0], str))
        self.assertCountEqual(srange, ran)

    def test_no_start(self):
        srange = list(Strange(3))
        xres = ['0', '1', '2']
        self.assertCountEqual(srange, xres)

    def test_srange_reiterable(self):
        srange = Strange(1, 3)
        xres = ['1', '2']

        lst1 = list(srange)
        lst2 = list(srange)

        self.assertCountEqual(lst1, lst2)
        self.assertCountEqual(lst1, xres)
