"""
test_algorithms.py
@brad_anton

License:
 
Copyright 2015 hashdd.com

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import unittest
import hashlib

from hashdd import hashdd
from hashdd.algorithms.algorithm import algorithm

class TestAlgorithms(unittest.TestCase):
    TEST_FILENAME='tests/data/sample.exe'
    def test_available(self):
        """Simple test to check all available algorithms

            We have all algorithms in individual tests to call out those not supported on this system
        """
        h = hashdd(filename=self.TEST_FILENAME)
        result = h.safedict()
        algos = [ a.__name__ for a in algorithm.__subclasses__() ]
        for module in algos:
            if module.startswith('hashdd_'):
                m = getattr(hashlib, module)
                self.assertIsNotNone(m.sample)
                self.assertEqual(result[module], m.sample)

    def check_algo(self, algo):
        h = hashdd(filename=self.TEST_FILENAME, algorithms=[algo])
        m = getattr(hashlib, algo)

        result_safe = h.safedict()
        self.assertEqual(result_safe[algo], m.sample)
        
        result = h.todict()
        self.assertEqual(result[algo[7:]], m.sample)

    def test_hashdd_adler32(self):
        self.check_algo("hashdd_adler32")
    
    def test_hashdd_content_hash(self):
        self.check_algo("hashdd_content_hash")

    def test_hashdd_crc32(self):
        self.check_algo("hashdd_crc32")
    
    def test_hashdd_crc32b(self):
        self.check_algo("hashdd_crc32b")
    
    def test_hashdd_haval128(self):
        self.check_algo("hashdd_haval128")
    
    def test_hashdd_haval160(self):
        self.check_algo("hashdd_haval160")
    
    def test_hashdd_haval192(self):
        self.check_algo("hashdd_haval192")

    def test_hashdd_haval224(self):
        self.check_algo("hashdd_haval224")

    def test_hashdd_haval256(self):
        self.check_algo("hashdd_haval256")

    def test_hashdd_md5(self):
        self.check_algo("hashdd_md5")
    
    def test_hashdd_md5w(self):
        self.check_algo("hashdd_md5w")

    def test_hashdd_ripemd128(self):
        self.check_algo("hashdd_ripemd128")

    def test_hashdd_ripemd256(self):
        self.check_algo("hashdd_ripemd256")

    def test_hashdd_ripemd320(self):
        self.check_algo("hashdd_ripemd320")

    def test_hashdd_sdhash(self):
        self.check_algo("hashdd_sdhash")

    def test_hashdd_sha1(self):
        self.check_algo("hashdd_sha1")
    
    def test_hashdd_sha224(self):
        self.check_algo("hashdd_sha224")

    def test_hashdd_sha256(self):
        self.check_algo("hashdd_sha256")

    def test_hashdd_sha3_224(self):
        self.check_algo("hashdd_sha3_224")
    
    def test_hashdd_sha3_256(self):
        self.check_algo("hashdd_sha3_256")

    def test_hashdd_sha3_384(self):
        self.check_algo("hashdd_sha3_384")

    def test_hashdd_sha3_512(self):
        self.check_algo("hashdd_sha3_512")

    def test_hashdd_sha384(self):
        self.check_algo("hashdd_sha384")
    
    def test_hashdd_sha512(self):
        self.check_algo("hashdd_sha512")

    def test_hashdd_snefru128(self):
        self.check_algo("hashdd_snefru128")

    def test_hashdd_snefru256(self):
        self.check_algo("hashdd_snefru256")

    def test_hashdd_ssdeep(self):
        self.check_algo("hashdd_ssdeep")

    def test_hashdd_tiger128(self):
        self.check_algo("hashdd_tiger128")

    def test_hashdd_tiger160(self):
        self.check_algo("hashdd_tiger160")

    def test_hashdd_tiger192(self):
        self.check_algo("hashdd_tiger192")

    def test_hashdd_tlsh(self):
        self.check_algo("hashdd_tlsh")

    def test_hashdd_whirlpool(self):
        self.check_algo("hashdd_whirlpool")


if __name__ == '__main__':
    unittest.main()
