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

from .algorithm import algorithm

class hashdd_sha1(algorithm):
    name = 'hashdd_sha1'
    validation_regex = re.compile(r'^[a-f0-9]{40}$', re.IGNORECASE)
    sample = '8C2429DB2B3E0550C0E4964E7AE605ACD8FF5AB3'

    def setup(self, arg):
        self.h = hashlib.sha1()

    def hexdigest(self):
        return self.h.hexdigest().upper()

    def update(self, arg):
        self.h.update(arg)

import hashlib
hashlib.hashdd_sha1 = hashdd_sha1
