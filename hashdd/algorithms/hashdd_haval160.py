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

from mhashlib import haval160 as mhaval160

from .algorithm import algorithm

class hashdd_haval160(algorithm):
    name = 'hashdd_haval160'
    validation_regex = re.compile(r'^[a-f0-9]{40}$', re.IGNORECASE)
    sample = '8E324AFD3ADA3441AF539E589705E70394CDB508'

    def setup(self, arg):
        self.h = mhaval160()

    def digest(self):
        return self.h.digest()

    def hexdigest(self):
        return self.h.hexdigest().upper().decode()

    def update(self, arg):
        self.h.update(arg)

hashlib.hashdd_haval160 = hashdd_haval160
