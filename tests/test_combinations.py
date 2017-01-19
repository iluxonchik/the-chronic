"""
Test if comibnations of words are working as expected.
"""
import unittest
from tests.utils import get_words_generator
from itertools import product
from thechronic.thechronic import TheChronic


class CombinationsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.TESTS_PATH = 'tests/'
        cls.RES_PATH = cls.TESTS_PATH + 'res/'
        cls.WORDS1_PATH = cls.RES_PATH + 'words1.txt'
        cls.WORDS2_PATH = cls.RES_PATH + 'words2.txt'

    def setUp(self):
        self.words1 = ['cat', 'dog', 'rat']
        self.words2 = ['the', 'chronic', '1992']

    def tearDown(self):
        pass

    def test_combinations_one_word(self):
        thechronic = TheChronic(words=self.words1)

        # genreate combinations of one word only
        res = list(thechronic.combine(num_words=1))
        res = list(res)
        self.assertEqual(len(res), 3)
        self.assertCountEqual(res, self.words1)

        # make sure that num_words defaults to 1
        res = list(thechronic.combine())
        self.assertEqual(len(res), 3)

        self.assertCountEqual(res, self.words1)


    def test_combinations_multiple_words_single_source(self):
        thechronic = TheChronic(words=self.words1)

        expected_result = [
            'catcat', 'catdog', 'catrat',
            'dogcat', 'dogdog', 'dograt',
            'ratcat', 'ratdog', 'ratrat'
        ]
        res = list(thechronic.combine(num_words=2))
        self.assertEqual(len(res), 9)
        self.assertCountEqual(res, expected_result)

        expected_result = get_words_generator(product(self.words1, repeat=3))
        res = list(thechronic.combine(num_words=3))
        self.assertEqual(len(res), 27)
        self.assertCountEqual(res, expected_result)

    def test_combinations_multiple_words_multiple_sources(self):
        thechronic = TheChronic(words=[self.words1, self.words2])

        expected_result = ['catcat', 'catdog', 'catrat', 'catthe', 'catchronic',
        'cat1992',
        'dogcat', 'dogdog', 'dograt', 'dogthe', 'dogchronic', 'dog1992',
        'ratcat', 'ratdog', 'ratrat', 'ratthe', 'ratchronic', 'rat1992',
        'thecat', 'thedog', 'therat', 'thethe', 'thechronic', 'the1992',
        'chroniccat', 'chronicdog', 'chronicrat', 'chronicthe',
        'chronicchronic', 'chronic1992',
        '1992cat', '1992rat', '1992dog', '1992the', '1992chronic', '19921992',
        ]
        res = list(thechronic.combine(num_words=2))
        self.assertEqual(len(res), 36)
        self.assertCountEqual(res, expected_result)

        expected_result = get_words_generator(product(self.words1 + self.words2,
            repeat=3))
        res = list(thechronic.combine(num_words=3))
        self.assertEqual(len(res), 216)
        self.assertCountEqual(res, expected_result)


    def test_combinations_with_build_up(self):
        thechronic = TheChronic(words=self.words1)

        expected_result = [
            'cat', 'dog', 'rat',
            'catcat', 'catdog', 'catrat',
            'dogcat', 'dogdog', 'dograt',
            'ratcat', 'ratdog', 'ratrat'
        ]

        res = list(thechronic.combine(num_words=2, build_up=True))
        self.assertEqual(len(res), 12)
        self.assertCountEqual(res, expected_result)

        res = list(thechronic.combine(num_words=5, build_up=True))
        self.assertEqual(len(res), 363)

    def test_combinations_load_from_single_file(self):
        thechronic = TheChronic(files=self.WORDS1_PATH)

        expected_result = [
            'catcat', 'catdog', 'catrat',
            'dogcat', 'dogdog', 'dograt',
            'ratcat', 'ratdog', 'ratrat'
        ]

        res = list(thechronic.combine(num_words=2))
        self.assertEqual(len(res), 9)
        self.assertCountEqual(res, expected_result)

        expected_result = get_words_generator(product(self.words1, repeat=3))
        res = list(thechronic.combine(num_words=3))
        self.assertEqual(len(res), 27)
        self.assertCountEqual(res, expected_result)

    def test_combinations_load_from_multiple_file(self):
        thechronic = TheChronic(files=(self.WORDS1_PATH, self.WORDS2_PATH))

        expected_result = ['catcat', 'catdog', 'catrat', 'catthe', 'catchronic',
        'cat1992',
        'dogcat', 'dogdog', 'dograt', 'dogthe', 'dogchronic', 'dog1992',
        'ratcat', 'ratdog', 'ratrat', 'ratthe', 'ratchronic', 'rat1992',
        'thecat', 'thedog', 'therat', 'thethe', 'thechronic', 'the1992',
        'chroniccat', 'chronicdog', 'chronicrat', 'chronicthe',
        'chronicchronic', 'chronic1992',
        '1992cat', '1992rat', '1992dog', '1992the', '1992chronic', '19921992',
        ]

        res = list(thechronic.combine(num_words=2))
        self.assertEqual(len(res), 36)
        self.assertCountEqual(res, expected_result)

        expected_result = get_words_generator(product(self.words1 + self.words2,
            repeat=3))
        res = list(thechronic.combine(num_words=3))
        self.assertEqual(len(res), 216)
        self.assertCountEqual(res, expected_result)

    def test_combinaitons_load_from_words_and_file(self):
        thechronic = TheChronic(words=self.words1, files=self.WORDS2_PATH)

        expected_result = ['catcat', 'catdog', 'catrat', 'catthe', 'catchronic',
        'cat1992',
        'dogcat', 'dogdog', 'dograt', 'dogthe', 'dogchronic', 'dog1992',
        'ratcat', 'ratdog', 'ratrat', 'ratthe', 'ratchronic', 'rat1992',
        'thecat', 'thedog', 'therat', 'thethe', 'thechronic', 'the1992',
        'chroniccat', 'chronicdog', 'chronicrat', 'chronicthe',
        'chronicchronic', 'chronic1992',
        '1992cat', '1992rat', '1992dog', '1992the', '1992chronic', '19921992',
        ]

        res = list(thechronic.combine(num_words=2))
        self.assertEqual(len(res), 36)
        self.assertCountEqual(res, expected_result)

        expected_result = get_words_generator(product(self.words1 + self.words2,
            repeat=3))
        res = list(thechronic.combine(num_words=3))
        self.assertEqual(len(res), 216)
        self.assertCountEqual(res, expected_result)

    def test_min_length(self):
        thechronic = TheChronic(words=self.words1)

        expected_result = [
            'catcat', 'catdog', 'catrat',
            'dogcat', 'dogdog', 'dograt',
            'ratcat', 'ratdog', 'ratrat'
        ]

        res = list(thechronic.combine(num_words=2, build_up=True, min_length=4))
        self.assertEqual(len(res), 9)
        self.assertCountEqual(res, expected_result)

    def test_max_length(self):
        thechronic = TheChronic(words=self.words1)

        expected_result = [
            'cat', 'dog', 'rat',
        ]

        res = list(thechronic.combine(num_words=2, build_up=True, max_length=3))
        self.assertEqual(len(res), 3)
        self.assertCountEqual(res, expected_result)


        res = list(thechronic.combine(num_words=2, build_up=True, max_length=2))
        self.assertEqual(len(res), 0)
        self.assertCountEqual(res, [])

    def test_min_max_length(self):
        thechronic = TheChronic(words=['the', 'game', 'the documentary',
        'the doctor\'s advocate', 'l.a.x.', 'red', '1992'])

        expected_result = ['the', 'game', 'red', '1992']

        res = list(thechronic.combine(num_words=1, build_up=True,
                                                    min_length=2, max_length=4))
        self.assertEqual(len(res), 4)
        self.assertCountEqual(res, expected_result)

    def test_ending_numbers(self):
        thechronic = TheChronic(words=self.words1)
        expected_result = [
            'catcat201', 'catdog102', 'catrat001',
            'dogcat101', 'dogdog102', 'dograt122',
            'ratcat500', 'ratdog404', 'ratrat007'
        ]
        thechronic.add_numeric(digits=3, build_up=False)

        res = list(thechronic.combine(num_words=2, build_up=True))
        self.assertIn(res, expected_result)


    def test_ending_numbers_with_build_up(self):
        thechronic = TheChronic(words=self.words1)
        expected_result = [
            'catcat1', 'catdog00', 'catrat021',
            'dogcat22', 'dogdog99', 'dograt122',
            'ratcat500', 'ratdog404', 'ratrat007'
        ]
        thechronic.add_numeric(digits=3, build_up=True)

        res = list(thechronic.combine(num_words=2, build_up=True))
        self.assertIn(res, expected_result)
