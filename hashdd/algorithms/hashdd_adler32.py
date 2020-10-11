"""
hashdd_alder32.py
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
import hashlib

from .algorithm import algorithm

from mhashlib import adler32 as madler32

class hashdd_adler32(algorithm):
    name = 'hashdd_adler32'
    validation_regex = re.compile(r'^[a-f0-9]{8}$', re.IGNORECASE)
    sample = '77B3C08A'

    def setup(self, arg):
        self.h = madler32()

    def digest(self):
        return self.h.digest()

    def hexdigest(self):
        return self.h.hexdigest().upper().decode()

    def update(self, arg):
        self.h.update(arg)

hashlib.hashdd_adler32 = hashdd_adler32
