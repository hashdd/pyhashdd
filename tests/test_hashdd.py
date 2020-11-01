import unittest 
import hashlib

from hashdd import hashdd
from hashdd.features import feature


class TestHashdd(unittest.TestCase):
    TEST_FILENAME="tests/data/sample.exe"
    TEST_FILENAME_ZERO="tests/data/file_size_zero.txt"

    
    def check_hashdd(self, todict, safedict):
        """Checks a hashdd result against the "sample.exe" sample
        """
        # get a list of algorithms so we can check .todict() and .safedict() results
        available = hashdd.algorithms_available()

        # Check hashes match the sample hash
        for a in available:
            # Check to ensure the key is available in .todict()
            self.assertIn(a[7:], todict)
            # Remove the "hashdd_" prefix to check the key in .safedict()
            self.assertIn(a, safedict)
            
            # Extract the sample of the hash which should be for TEST_FILENAME
            m = getattr(hashlib, a)

            # Check that the sample hash matches that calculated
            self.assertEqual(todict[a[7:]], m.sample)
            self.assertEqual(safedict[a], m.sample)

        # Check profile information
        # TODO

    def test_hashdd_filename(self):
        h = hashdd(filename=self.TEST_FILENAME)
        self.assertIsNotNone(h)

        d = h.todict()
        self.assertIsInstance(d, dict)

        sd = h.safedict()
        self.assertIsInstance(sd, dict)
        
        self.check_hashdd(d, sd)

        # Check zero-sized file
        h = hashdd(filename=self.TEST_FILENAME_ZERO)
        self.assertIsNotNone(h)

        d = h.todict()
        self.assertIsInstance(d, dict)

        sd = h.safedict()
        self.assertIsInstance(sd, dict)
        
        # Dont check algorithms, just check features
        # self.check_hashdd(d, sd)

    def test_hashdd_buffer(self):
        with open(self.TEST_FILENAME, 'rb') as f:
            buf = f.read()

        h = hashdd(buf=buf)
        self.assertIsNotNone(h)

        d = h.todict()
        self.assertIsInstance(d, dict)

        sd = h.safedict()
        self.assertIsInstance(sd, dict)
        
        self.check_hashdd(d, sd)

