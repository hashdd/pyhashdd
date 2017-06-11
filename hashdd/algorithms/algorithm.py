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
import re

class algorithm(object):
    name = None
    validation_regex = None
    sample = None # The result of hashing sample.exe

    def __init__(self, arg):
        self.setup(arg)
        self.update(arg)

    @staticmethod
    def prefilter(arg):
        """
        Override, use to inspect the input buffer
        to determine if it meets algorithm requirements
        (e.g. length). Return True to continue processing 
        otherwise return False to abort
        """
        return True 
    
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
        """Checks an input string to determine if it matches the characteristics
        of the hash
        """
        if self.validation_regex is None:
            raise Exception("Cannot validate string for \
                    algorithm {}, no alphabet and/or digest_size \
                    defined".format(self.name))

        return bool(self.validation_regex.match(string))


