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
import hashlib
import sha3

from .algorithm import algorithm

class hashdd_sha3_224(algorithm):
    name = 'hashdd_sha3_224'
    validation_regex = re.compile(r'^[a-f0-9]{56}$', re.IGNORECASE)
    sample = 'fc4843572ea040841021236a7f102322a20b8dd941f689fb444be4c3'.upper()

    def setup(self, arg):
        self.h = hashlib.sha3_224()

    def hexdigest(self):
        return self.h.hexdigest().upper()

    def update(self, arg):
        self.h.update(arg)

import hashlib
hashlib.hashdd_sha3_224 = hashdd_sha3_224
