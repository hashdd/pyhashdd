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

import zlib
import re

class hashdd_crc32(algorithm):
    name = 'crc32'
    validation_regex = re.compile(r'^[a-f0-9]{8}$', re.IGNORECASE)
    sample = '301E5EBC' 

    def setup(self, arg):
        self.__digest = 0

    def copy(self):
        copy = super(self.__class__, self).__new__(self.__class__)
        copy.__digest = self.__digest
        return copy

    def digest(self):
        return self.__digest

    def hexdigest(self):
        return '{:08X}'.format(self.__digest)

    def update(self, arg):
        self.__digest = zlib.crc32(arg, self.__digest) & 0xffffffff
        #self.__digest = binascii.crc32(arg, self.__digest) & 0xffffffff

import hashlib
hashlib.hashdd_crc32 = hashdd_crc32
