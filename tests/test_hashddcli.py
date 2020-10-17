import unittest
import hashlib

from os.path import isfile
from os import remove

from hashdd.hashddcli import hashddcli
from hashdd import hashdd
from hashdd.constants import Features, Algorithms


class TestHashddCli(unittest.TestCase):
    TEST_FILENAME='tests/data/sample.exe'
    TEST_RECURSIVE_DIRECTORY='tests/data/recursive_directory_test'
    TEST_RECURSIVE_FILENAME='sample.exe'

    def tearDown(self):
        if isfile('hashdd.bloom'):
            remove('hashdd.bloom')

    def check_compute_result(self, results, algorithms, features):
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)

        for result in results:
            for feature, value in features:
                self.assertIn(feature, result)
                """This is a little hacky but we use .endswith to account for features like
                FILE_ABSOLUTE_PATH which may prepend other things to the result"""
                if isinstance(result[feature], list):
                    self.assertTrue(result[feature][0].endswith(value))
                else:
                    self.assertTrue(result[feature].endswith(value))

            for algo in algorithms:
                if algo.startswith('hashdd_'):
                    a = algo
                else:
                    a = 'hashdd_{}'.format(algo)

                self.assertIn(a, result)
                m = getattr(hashlib, a)
                self.assertEqual(result[a], m.sample)

    def test_show(self):
        h = hashddcli(show=True)
        self.assertIsNotNone(h)

        results = h.run()
        self.assertIsInstance(results, list)

        available = hashdd.algorithms_available()

        for algo in results:
            self.assertTrue(algo.startswith('hashdd_'))
            self.assertIn(algo, available)

    def test_compute_filename(self):
        algorithms = [ Algorithms.SHA256.value ] # Default
        features = [ [ Features.FILE_ABSOLUTE_PATH.value, self.TEST_FILENAME] ] # Default
        
        h = hashddcli(compute=True, filename=self.TEST_FILENAME)
        self.assertIsNotNone(h)

        results = h.run()
        self.check_compute_result(results, algorithms, features)
        
        # Test selected algorithms 
        algorithms = [ 'md5', 'md5w', 'sha256' ]
        features = [ [ Features.FILE_ABSOLUTE_PATH.value, self.TEST_FILENAME] ]
        
        h = hashddcli(compute=True, filename=self.TEST_FILENAME, algorithms=algorithms)
        self.assertIsNotNone(h)

        results = h.run()
        self.check_compute_result(results, algorithms, features)
        
    def test_compute_directory(self):
        algorithms = [ Algorithms.SHA256.value ] # Default
        features = [ [ Features.FILE_ABSOLUTE_PATH.value, self.TEST_RECURSIVE_FILENAME] ] # Default
        
        h = hashddcli(compute=True, directory=self.TEST_RECURSIVE_DIRECTORY)
        self.assertIsNotNone(h)

        results = h.run()
        self.check_compute_result(results, algorithms, features)

    def test_bloom_filename(self):
        h = hashddcli(bloom=True, filename=self.TEST_FILENAME)
        self.assertIsNotNone(h)

        results = h.run()
        self.assertTrue(isfile('hashdd.bloom'))
  
        # Check the bloom filter we just created
        algorithms = [ Algorithms.SHA256.value ] # Default
        features = [ [ Features.FILE_ABSOLUTE_PATH.value, self.TEST_FILENAME] ] # Default
        
        h = hashddcli(bloom=True, filename=self.TEST_FILENAME)
        self.assertIsNotNone(h)

        results = h.run()
        self.check_compute_result(results, algorithms, features)
        self.assertIn('match_count', results[0])
        self.assertIn('matches', results[0])
        self.assertEqual(results[0]['match_count'], 1)
        self.assertEqual(results[0]['matches'][0], 'hashdd_sha256')

        # Recheck with nomatch
        h = hashddcli(bloom=True, filename=self.TEST_FILENAME, nomatch=True)
        self.assertIsNotNone(h)

        results = h.run()
        self.check_compute_result(results, algorithms, features)
        self.assertIn('match_count', results[0])
        self.assertIn('matches', results[0])
        self.assertEqual(results[0]['match_count'], 1)
        self.assertEqual(results[0]['matches'][0], 'hashdd_sha256')

    def test_bloom_directory(self):
        h = hashddcli(bloom=True, directory=self.TEST_RECURSIVE_DIRECTORY)
        self.assertIsNotNone(h)

        results = h.run()
        self.assertTrue(isfile('hashdd.bloom'))

        # Check the bloom filter we just created
        algorithms = [ Algorithms.SHA256.value ] # Default
        features = [ [ Features.FILE_ABSOLUTE_PATH.value, self.TEST_RECURSIVE_FILENAME] ] # Default
        
        h = hashddcli(bloom=True, directory=self.TEST_RECURSIVE_DIRECTORY)
        self.assertIsNotNone(h)

        results = h.run()
        self.check_compute_result(results, algorithms, features)
        self.assertIn('match_count', results[0])
        self.assertIn('matches', results[0])
        self.assertEqual(results[0]['match_count'], 1)
        self.assertEqual(results[0]['matches'][0], 'hashdd_sha256')

