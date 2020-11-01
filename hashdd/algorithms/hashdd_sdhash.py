"""
hashdd/algorithms/hashdd_sdhash.py
@brad_anton 

_sdbf_class.so is from compiling the official SDHash 
release. If you're getting errors using this module, 
you may need to compile it yourself. To do so, instructions
can be found here:

https://gist.github.com/brad-anton/a5a12eff6b5675c47da07aaffa727985



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

from hashdd.algorithms import sdbf_class 
from hashdd.algorithms.algorithm import algorithm
from hashdd.constants import MAX_SIZE

class hashdd_sdhash(algorithm):
    name = 'hashdd_sdhash'
    validation_regex = re.compile(r'^sdbf:\d+:\d+:.*:\d+:.*:\d+:\d+:.*:\d+:\d+:\d+:[a-z0-9=/+]{2,}$', re.IGNORECASE)
    sample = 'sdbf:03:7:unknown:8192:sha1:256:5:7ff:160:1:102:4QAIjJHDBGBAEMECLJgsIEAgMCAAABQiqQKEAWkAmKEPZIBIQiIMggJACQIQjAAAIRaAaGCCwJbAAIAUVIRE4BAIREQQBAEAAMFCBqI7ACDBGkAywSLUoJTQCkgBJASECEIJgmBwrREAAysIggSUQEAAIBAAwCABIhCIBhhBEAAgBEFgwABAItABhAC8IEaCyDgAEZgGAE4AcOCiAAiiEtlBoEDACAAAhiIqAIhBQEACEAAAUCAsBmBCQQEAEARAipkwKKAEAGiAwiYMIBICYQOAAoAwCQEobABAElgBEcAAIpEoEgoogLFAISCUBLCoBMLAQAEQgBIQAEYBqVgFQw=='
    implements_readfile = True

    @staticmethod
    def prefilter(arg):
        length = len(arg)
        return True if length >= 512 and length <= MAX_SIZE else False
    
    def readfile(self, filename):
        self.filename = filename
        self.h = sdbf_class.sdbf(filename, 0)

    def setup(self, arg):
        self.h = None
        self.update(arg)

    def hexdigest(self):
        # sdhashes have a trailing newline
        res = self.h.to_string().replace('\n', '')

        # This is gnarly, sdbf includes filename and length in the hash output, but not when we read from a buffer
        # so we're going to strip that out if we used hashdd_sdhash.readfile()
        used_readfile = getattr(self, 'filename', None)
        if used_readfile:
            parts = res.split(':')
            res = ':'.join(parts[0:2]) + ':7:unknown:' + ':'.join(parts[4:])

        return res

    def update(self, arg):
        if arg:
            self.h = sdbf_class.sdbf("unknown", arg, 0, len(arg), None)


hashlib.hashdd_sdhash = hashdd_sdhash 
