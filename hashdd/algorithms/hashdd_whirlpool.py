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

from mhashlib import whirlpool as mwhirlpool

class hashdd_whirlpool(algorithm):
    name = 'hashdd_whirlpool'
    validation_regex = re.compile(r'^[a-f0-9]{128}$', re.IGNORECASE)
    sample = 'E503B69D61F038F526DB42A09BA60B1231DCA9ED685C5FCF9CD1CDDF63940A03F27F34DA0A6952DBE3B8B3E9D0B56A2E26F003685D1E56590325D348C5248D04'

    def setup(self, arg):
        self.h = mwhirlpool()

    def digest(self):
        return self.h.digest()

    def hexdigest(self):
        return self.h.hexdigest().upper()

    def update(self, arg):
        self.h.update(arg)

import hashlib
hashlib.hashdd_whirlpool = hashdd_whirlpool
