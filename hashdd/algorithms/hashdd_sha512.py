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

class hashdd_sha512(algorithm):
    name = 'hashdd_sha512'
    validation_regex = re.compile(r'^[a-f0-9]{128}$', re.IGNORECASE)
    sample = '60E218973D5493564C617CF76A0C82DA258095E4576ED51A498F90159A174AF69C3AD328ECC8DDBFE7BCAD2AA61E9889CE96D8BB7755A33C71146F311D653865'

    def setup(self, arg):
        self.h = hashlib.sha512()

    def hexdigest(self):
        return self.h.hexdigest().upper()

    def update(self, arg):
        self.h.update(arg)

import hashlib
hashlib.hashdd_sha512 = hashdd_sha512
