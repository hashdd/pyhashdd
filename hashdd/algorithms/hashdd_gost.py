"""
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

import re

from .algorithm import algorithm

from mhashlib import gost as mgost

class hashdd_gost(algorithm):
    name = 'hashdd_gost'
    validation_regex = re.compile(r'^[a-f0-9]{64}$', re.IGNORECASE)
    sample = '68F5124FB7B3EAF3470B43582B83670338583B328023B23BDAF97ACD10D76787'

    def setup(self, arg):
        self.h = mgost()

    def hexdigest(self):
        return self.h.hexdigest().upper().decode()

    def update(self, arg):
        self.h.update(arg)

import hashlib
hashlib.hashdd_gost = hashdd_gost 
