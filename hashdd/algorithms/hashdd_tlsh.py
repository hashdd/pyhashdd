"""
hashdd/algorithms/hashdd_sdhash.py
@brad_anton 

tlsh.so is from compiling the official SDHash 
release. If you're getting errors using this module, 
you may need to compile it yourself. To do so, instructions
can be found here:

https://gist.github.com/brad-anton/184e15fd46c4dab8a6dd6876439f0a0f


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
import tlsh 

from algorithm import algorithm

class hashdd_tlsh(algorithm):
    name = 'hashdd_tlsh'
    validation_regex = re.compile(r'[a-f0-9]{70}$', re.IGNORECASE)
    sample = '5DF1D70B7E9180E1C789CAB817B24789EA69647117D170FB77A35EA98E353C0D42F14E'

    @staticmethod
    def prefilter(arg):
        return True if len(arg) >= 256 else False

    def setup(self, arg):
        self.h = tlsh.Tlsh()

    def hexdigest(self):
        self.h.final()
        return self.h.hexdigest()

    def update(self, arg):
        self.h.update(arg)


import hashlib
hashlib.hashdd_tlsh = hashdd_tlsh 
