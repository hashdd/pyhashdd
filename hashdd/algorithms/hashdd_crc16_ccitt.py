"""
hashdd_crc16_ccitt.py
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
from PyCRC.CRCCCITT import CRCCCITT

class hashdd_crc16_ccitt(algorithm):
    name = 'hashdd_crc16_ccitt'
    validation_regex = re.compile(r'^[a-f0-9]{4}$', re.IGNORECASE)
    sample = 'F07A'

    def setup(self, arg):
        self.__digest = 0

    def digest(self):
        return self.__digest

    def hexdigest(self):
        return '{:04X}'.format(self.__digest)

    def update(self, arg):
        self.__digest += CRCCCITT().calculate(arg)

import hashlib
hashlib.hashdd_crc16_ccitt = hashdd_crc16_ccitt
