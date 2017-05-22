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

from mhashlib import ripemd320 as mripemd320

class hashdd_ripemd320(algorithm):
    name = 'hashdd_ripemd320'
    validation_regex = re.compile(r'^[a-f0-9]{80}$', re.IGNORECASE) 
    sample = '202D0DDAA594F2191BFD98602EBAD1FC85DFFE23DBAA1F2129BB335C7CB8E3BC38C477F3A40D8ECB'

    def setup(self, arg):
        self.h = mripemd320()

    def digest(self):
        return self.h.digest()

    def hexdigest(self):
        return self.h.hexdigest().upper()

    def update(self, arg):
        self.h.update(arg)

import hashlib
hashlib.hashdd_ripemd320 = hashdd_ripemd320
