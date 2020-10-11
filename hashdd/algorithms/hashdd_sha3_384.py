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

class hashdd_sha3_384(algorithm):
    name = 'hashdd_sha3_384'
    validation_regex = re.compile(r'^[a-f0-9]{96}$', re.IGNORECASE)
    sample = 'e9effde89c5b4731fe05480ada5f5f69a1d8bd4371f1013ff8f86fb0e1475712c00f735ae44c481686219fc4453b74b2'.upper()

    def setup(self, arg):
        self.h = hashlib.sha3_384()

    def hexdigest(self):
        return self.h.hexdigest().upper()

    def update(self, arg):
        self.h.update(arg)

import hashlib
hashlib.hashdd_sha3_384 = hashdd_sha3_384
