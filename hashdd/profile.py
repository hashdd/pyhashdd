"""
profile.py
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

from features.feature import feature 
from os.path import join

class profile(object):
    def __init__(self, buffer=None, filename=None, overrides=None, modules=None, 
            store_plaintext=False):
        """
        Keyword Arguments:
        buffer -- String to apply features to
        overrides -- Dictionary with hashdd_ feature module 
            names use to override the module output with
        store_plaintext -- Boolean defining whether or not 
            the string value itself should be stored
        modules -- A list of module names to include in the output. 
            If None, all modules will be included. If an empty list, 
            no modules will be included
        """

        self.profile = {} 

        if filename is None and buffer is None:
            raise Exception('No file or buffer supplied, nothing to profile!')

        if buffer is None:
            with open(filename, 'rb') as f:
                buffer = f.read()

        for f in feature.__subclasses__():
            if ( f.__name__ == 'hashdd_plaintext'
                    and not store_plaintext ):
                continue

            if modules is not None and f.__name__ not in modules:
                # Skip modules that are not expressly enabled
                continue

            if overrides is not None and f.__name__ in overrides:
                # Override any defined values
                self.profile[f.__name__] = overrides[f.__name__]
                continue

            self.profile[f.__name__] = f(buffer=buffer, filename=filename).result 

if __name__ == '__main__':
    raise Exception('Cannot run this module directory')
