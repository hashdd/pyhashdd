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

from mhashlib import ripemd256 as mripemd256

from .algorithm import algorithm

class hashdd_ripemd256(algorithm):
    name = 'hashdd_ripemd256'
    validation_regex = re.compile(r'^[a-f0-9]{64}$', re.IGNORECASE)
    sample = 'FD1E6FD68CAE1DD51146FD78BE3883555812A45FBD64548E9DB7533C6D30821B'

    def setup(self, arg):
        self.h = mripemd256()

    def digest(self):
        return self.h.digest()

    def hexdigest(self):
        return self.h.hexdigest().upper().decode()

    def update(self, arg):
        self.h.update(arg)

hashlib.hashdd_ripemd256 = hashdd_ripemd256
