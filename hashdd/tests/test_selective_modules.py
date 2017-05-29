"""
test_selective_modules.py
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
    """Unittests for defining selective modules and overrides
    """
    overrides = { 'hashdd_file_absolute_path': 'test/', 'hashdd_size': 0 }
    h = hashdd(filename='sample.exe', features=['hashdd_file_name', 'hashdd_file_absolute_path'],
            feature_overrides=overrides, algorithms=['hashdd_md5w', 'hashdd_crc16'] )
    result = h.safedict()

    def test_includes_removal(self):
        """When a list of features is provided, no other modules
        should be preset"""
        self.assertFalse('hashdd_known_level' in self.result)

    def test_includes(self):
        """When a list of features is provided, only those
        features should be present"""
        self.assertTrue('hashdd_file_name' in self.result)

        # Just double checking output
        self.assertEqual(self.result['hashdd_file_name'][0], 'sample.exe')

    def test_overrides(self):
        """Overrides should be in result"""
        self.assertEqual(self.result['hashdd_file_absolute_path'], 'test/')
        
        # Overrides not explicitedly defined in feature includes should not be in output
        self.assertFalse('hashdd_size' in self.result)

    def test_includes_algorithms(self):
        self.assertTrue('hashdd_md5w' in self.result)
        self.assertTrue('hashdd_crc16' in self.result)


if __name__ == '__main__':
    unittest.main()
