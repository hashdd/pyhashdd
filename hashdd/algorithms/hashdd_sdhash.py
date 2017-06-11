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
import sdbf_class 

from algorithm import algorithm

class hashdd_sdhash(algorithm):
    name = 'hashdd_sdhash'
    validation_regex = re.compile(r'^sdbf:\d+:\d+:.*:\d+:.*:\d+:\d+:.*:\d+:\d+:\d+:[a-z0-9=/+]{2,}$', re.IGNORECASE)
    sample = 'sdbf:03:7:unknown:8192:sha1:256:5:7ff:160:1:102:4QAIjJHDBGBAEMECLJgsIEAgMCAAABQiqQKEAWkAmKEPZIBIQiIMggJACQIQjAAAIRaAaGCCwJbAAIAUVIRE4BAIREQQBAEAAMFCBqI7ACDBGkAywSLUoJTQCkgBJASECEIJgmBwrREAAysIggSUQEAAIBAAwCABIhCIBhhBEAAgBEFgwABAItABhAC8IEaCyDgAEZgGAE4AcOCiAAiiEtlBoEDACAAAhiIqAIhBQEACEAAAUCAsBmBCQQEAEARAipkwKKAEAGiAwiYMIBICYQOAAoAwCQEobABAElgBEcAAIpEoEgoogLFAISCUBLCoBMLAQAEQgBIQAEYBqVgFQw=='

    @staticmethod
    def prefilter(arg):
        return True if len(arg) >= 512 else False

    def setup(self, arg):
        self.update(arg)

    def hexdigest(self):
        return self.h.to_string().replace('\n', '')

    def update(self, arg):
        self.h = sdbf_class.sdbf('unknown', arg, 0, len(arg), None)


import hashlib
hashlib.hashdd_sdhash = hashdd_sdhash 
