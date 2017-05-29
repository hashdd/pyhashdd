"""
test_features.py
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

from hashdd import hashdd

class TestFeatures(unittest.TestCase):
    h = hashdd(filename='sample.exe')
    result = h.safedict()

    def test_known_level(self):
        self.assertEqual(self.result['hashdd_known_level'], 'Unknown')

    def test_file_name(self):
        self.assertEqual(self.result['hashdd_file_name'][0], 'sample.exe')

    def test_file_absolute_path(self):
        self.assertTrue(self.result['hashdd_file_absolute_path'][0].endswith('sample.exe'))

    def test_size(self):
        self.assertEqual(self.result['hashdd_size'], 8192)

    def test_mime(self):
        self.assertEqual(self.result['hashdd_mime'], 'application/x-dosexec')

    def test_filemagic(self):
        self.assertEqual(self.result['hashdd_filemagic'], 'PE32 executable (console) Intel 80386, for MS Windows')

if __name__ == '__main__':
    unittest.main()
