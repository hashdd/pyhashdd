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
from algorithm import algorithm

from mhashlib import ripemd128 as mripemd128

class hashdd_ripemd128(algorithm):
    name = 'hashdd_ripemd128'

    def setup(self, arg):
        self.h = mripemd128()

    def digest(self):
        return self.h.digest()

    def hexdigest(self):
        return self.h.hexdigest().upper()

    def update(self, arg):
        self.h.update(arg)

import hashlib
hashlib.hashdd_ripemd128 = hashdd_ripemd128
