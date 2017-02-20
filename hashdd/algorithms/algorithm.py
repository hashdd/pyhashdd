"""
algorithm.py
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
class algorithm(object):
    name = None
    digest_size = None
    block_size = 1
    alphabet = None

    def __init__(self, arg):
        self.setup(arg)
        self.update(arg)
    
    def setup(self, arg):
        # Override
        pass

    def hexdigest(self):
        # Override
        pass

    def update(self, arg):
        # Override
        pass

    def digest(self):
        # Override
        pass

    def copy(self):
        copy = super(self.__class__, self).__new__(self.__class__)
        return copy

    @classmethod
    def validate(self, string):
        """Checks an input string if its length is
        digest_size and characters are all within
        alphabet.
        """
        if self.digest_size is None or self.alphabet is None:
                raise Exception("Cannot validate string for \
                    algorithm {}, no alphabet and/or digest_size \
                    defined".format(name))

        digest_length = self.digest_size * 2

        return ( len(string) == digest_length and
                all(c in self.alphabet for c in string))


