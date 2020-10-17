# -*- coding: utf-8 -*-

import unittest
from hashdd import mhashlib

class MHashlibTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample_data = b"hello\n\n"

    @classmethod
    def tearDownClass(cls):
        pass

    def test_gost_hash(self):
        hash = mhashlib.gost(self.sample_data)
        valid_digest = b'a2c0810ccbb997eb2e029e7e4186535ef4efae43fdcb49afb4933303f649f8db'
        self.assertEqual(valid_digest, hash.hexdigest())

    def test_tiger192_hash(self):
        hash = mhashlib.tiger192(self.sample_data)
        valid_digest = b'3655e96f537401e1c5ac4197ac22594e6d0a740c664e7263'
        self.assertEqual(valid_digest, hash.hexdigest())

    def test_sha1_hash(self):
        hash = mhashlib.sha1(self.sample_data)
        valid_digest = b'4588019fd3d2567f303815db6adfe489b2ee5f92'
        self.assertEqual(valid_digest, hash.hexdigest())

    def test_sha256_hash(self):
        hash = mhashlib.sha256(self.sample_data)
        valid_digest = b'50adea61fa4e77ab111b814716097abfd05f83a207b47eb4529bbd4f54e111e0'
        self.assertEqual(valid_digest, hash.hexdigest())

    def test_md5_hash(self):
        hash = mhashlib.md5(self.sample_data)
        valid_digest = b'14e273e6f416c4b90a071f59ac01206a'
        self.assertEqual(valid_digest, hash.hexdigest())

    def test_whirlpool_hash(self):
        hash = mhashlib.whirlpool(self.sample_data)
        valid_digest = (b'adc277e898e7164962c1674c0c3984169534630428364dd43fc7e4e3e7222b6'
                        b'ccf7b7c4656f972f392d5580797b70125780ac860cb84de6f55ed043277d545d3')
        self.assertEqual(valid_digest, hash.hexdigest())

    def test_ripemd160_hash(self):
        hash = mhashlib.ripemd(self.sample_data)
        valid_digest = b'52985141506d19e443281ad5c6e058871bb2f765'
        self.assertEqual(valid_digest, hash.hexdigest())

    def test_haval256_hash(self):
        hash = mhashlib.haval(self.sample_data)
        valid_digest = b'1b3aa948d5d867964d72b9320a648050725e2daac5898c2d9f09512b99e5f72f'
        self.assertEqual(valid_digest, hash.hexdigest())

    def test_adler32_hash(self):
        hash = mhashlib.adler32(self.sample_data)
        valid_digest = b'2902740a'
        self.assertEqual(valid_digest, hash.hexdigest())

    def test_snefru256_hash(self):
        hash = mhashlib.snefru256(self.sample_data)
        valid_digest = b'f33eb2a3152af27e719474e8888da43c53b1ea7a629796eb7a67ecc539fc29a8'
        self.assertEqual(valid_digest, hash.hexdigest())

if __name__ == "__main__":
    unittest.main()

