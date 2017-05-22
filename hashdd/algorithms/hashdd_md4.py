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

from algorithm import algorithm

from Crypto.Hash import MD4

class hashdd_md4(algorithm):
    name = 'hashdd_md4'
    validation_regex = re.compile(r'^[a-f0-9]{32}$', re.IGNORECASE)
    sample = '7875BEB6F3F889FE3013D6E8181D48BE'

    def setup(self, arg):
        self.h = MD4.new()

    def hexdigest(self):
        return self.h.hexdigest().upper()

    def update(self, arg):
        self.h.update(arg)

import hashlib
hashlib.hashdd_md4 = hashdd_md4 
