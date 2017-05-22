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

from Crypto.Hash import MD2

class hashdd_md2(algorithm):
    name = 'hashdd_md2'
    validation_regex = re.compile(r'^[a-f0-9]{32}$', re.IGNORECASE)
    sample = '67F5641272E1C37A3198D497E0268F1B'

    def setup(self, arg):
        self.h = MD2.new()

    def hexdigest(self):
        return self.h.hexdigest().upper()

    def update(self, arg):
        self.h.update(arg)

import hashlib
hashlib.hashdd_md2 = hashdd_md2 
