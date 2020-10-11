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

from hashdd.algorithms.algorithm import algorithm

class TestValidation(unittest.TestCase):
    def test_all(self):
        algos = [ a.__name__ for a in algorithm.__subclasses__() ]

        for module in algos:
            if module.startswith('hashdd_'):
                m = getattr(hashlib, module)
                if m.sample is not None:
                    print('Testing {}'.format(module))
                    self.assertTrue(m.validate(m.sample))

if __name__ == '__main__':
    unittest.main()
