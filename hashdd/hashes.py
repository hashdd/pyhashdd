"""
hashes.py
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

import hashlib
import os

from algorithms.algorithm import algorithm

class hashes(object):
    def __init__(self, buffer=None, modules=None):
        """
        Keyword Arguments:
        buffer -- A string containing the content to hash.
        modules -- A list of module names to include in the output. None
            means all modules will be included, empty list means None will be included
        """
        if buffer is None:
            raise Exception('No buffer provided, nothing to do')

        algos = list(hashlib.algorithms)
        for a in algorithm.__subclasses__():
            algos.append(a.__name__)
   
        for module in algos:
            """To support validation within each algorithm's
            module, we wrap an existing implementation 
            and name it with the 'hashdd_' prefix to avoid conflicts. 
            We're not going to strip this prefix until the very last moment
            as common hashes like md5 may be used in a variety of places
            """
            if modules is not None and module not in modules:
                # Skip modules that are not expressly enabled
                continue

            if module.startswith('hashdd_'):
                m = getattr(hashlib, module)
                # Do not strip prefix
                # setattr(self, module[7:], m(buffer).hexdigest())
                setattr(self, module, m(buffer).hexdigest())


if __name__ == '__main__':
    h = hashes('../simpleStackandHeap.exe')
    print h.__dict__

