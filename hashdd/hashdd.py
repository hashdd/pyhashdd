"""
hashdd.py
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

from hashes import hashes
from profile import profile 

import os

MAX_SIZE = 4096 * 1024 * 1024

class hashdd:
    def __init__(self,  filename=None, buffer=None, store_plaintext=False, absolute_path=None,
            features=None, algorithms=None, opsystem_code=None, product_code=None):
        """Primary class for all hashing and profiling modules.

        Keyword Arguments:
        filename --
        buffer --
        store_plaintext --
        features --
        feature_overrides --
        algorithms --
        """
        self.buffer = buffer

        if filename and self.buffer is None:
            statinfo = os.stat(filename)
            size = statinfo.st_size

            with open(filename, 'rb') as f:
                self.buffer = f.read()

            if size >= MAX_SIZE:
                self.store_plaintext = False

        p = profile(filename=filename, buffer=self.buffer, store_plaintext=store_plaintext,
                opsystem_code=opsystem_code, product_code=product_code, absolute_path=absolute_path,
                modules=features)
                

        self.result = p.profile.copy()

        h = hashes(buffer=self.buffer, modules=algorithms)
        self.result.update(h.__dict__)

if __name__ == '__main__':
    h = hashdd(filename='../simpleStackandHeap.exe', directory='/home/e/pyhashdd')
    print h.result
