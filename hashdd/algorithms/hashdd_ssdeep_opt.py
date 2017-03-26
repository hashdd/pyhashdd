"""
hashdd_ssdeep_opt.py
@brad_anton 


Implements the following:
    https://www.virusbulletin.com/virusbulletin/2015/11/optimizing-ssdeep-use-scale/
    https://github.com/bwall/ssdc

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

from base64 import b64decode
from struct import unpack
import ssdeep

class hashdd_ssdeep_opt(algorithm):
    name = 'hashdd_ssdeep_opt'

    @staticmethod
    def preprocess_hash(h):
        def get_all_7_char_chunks(h):
            return list(set((unpack("<Q", b64decode(h[i:i+7] + "=") + "\x00\x00\x00")[0] for i in xrange(len(h) - 6))))
        block_size, h = h.split(":", 1)
        block_size = int(block_size)

        # Reduce any sequence of the same char greater than 3 to 3
        for c in set(list(h)):
            while c * 4 in h:
                h = h.replace(c * 4, c * 3)

        block_data, double_block_data = h.split(":")

        return block_size, get_all_7_char_chunks(block_data), get_all_7_char_chunks(double_block_data)

    def setup(self, arg):
        self.h = ssdeep.Hash()

    def hexdigest(self):
        block_size, chunk_ints, double_chunk_ints = self.preprocess_hash(self.h.digest())
        return { 'block_size': block_size, 'chunk_ints': chunk_ints, 'double_chunk_ints': double_chunk_ints }

    def update(self, arg):
        self.h.update(arg)

import hashlib
hashlib.hashdd_ssdeep_opt = hashdd_ssdeep_opt
