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

import hashlib
import os

from os.path import join

from .algorithms.algorithm import algorithm
from .features.feature import feature
from .constants import MAX_SIZE

class hashdd(object):
    def __init__(self,  filename=None, buf=None, store_plaintext=False,
            features=None, feature_overrides=None, algorithms=None):
        """Primary class for all hashing and profiling modules.

        Keyword Arguments:
        filename -- Filename to evaluate. If buffer is not defined, this will open the file,
            otherwise it will use this value when building the profile
        buffer -- Contents to evaluate.
        store_plaintext -- Whether or not the plaintext should be included in the resulting output,
            this is useful for storing the content in a database.
        features -- List of features to use, None for all.
        feature_overrides -- Dictionary containing features and values to override the output of the module
        algorithms -- List of algorithms to use, None for all.
        """
        self._filename = filename
        self._buffer = buf
        self._store_plaintext = store_plaintext
        self._features = features
        self._feature_overrides = feature_overrides
        self._algorithms = algorithms

        statinfo = None
        if self._filename is not None and self._buffer is None:
            
            try:
                statinfo = os.stat(self._filename)
                size = statinfo.st_size

                if size > 0:
                    with open(self._filename, 'rb') as f:
                        self._buffer = f.read()

                    if size >= MAX_SIZE:
                        self._store_plaintext = False
                else:
                    self._buffer = ""
            except:
                pass

        if self._buffer is not None:
            self._generate_hashes()
            self._generate_profile()
        elif statinfo is not None:
            raise Exception("Unable to read file to a buffer")
        elif statinfo is None:
            raise Exception("Unable to read file information")
        else:
            raise Exception("Unknown file error")

    def _generate_hashes(self):
        if self._buffer is None:
            raise Exception('No buffer provided, nothing to do')

        algos = list(hashlib.algorithms_available)
        for a in algorithm.__subclasses__():
            algos.append(a.__name__)

        for module in algos:
            """To support validation within each algorithm's
            module, we wrap an existing implementation
            and name it with the 'hashdd_' prefix to avoid conflicts.
            We're not going to strip this prefix until the very last moment
            as common hashes like md5 may be used in a variety of places
            """
            if self._algorithms is not None and module not in self._algorithms:
                # Skip modules that are not expressly enabled
                continue

            if module.startswith('hashdd_'):
                m = getattr(hashlib, module)
                if m.prefilter(self._buffer):
                    setattr(self, module[7:], m(self._buffer).hexdigest())

    def _generate_profile(self):
        if self._buffer is None:
            raise Exception('No buffer provided, nothing to do')

        for f in feature.__subclasses__():
            if ( f.__name__ == 'hashdd_plaintext'
                    and not self._store_plaintext ):
                continue

            if self._features is not None and f.__name__ not in self._features:
                # Skip modules that are not expressly enabled
                continue

            if self._feature_overrides is not None and f.__name__ in self._feature_overrides:
                # Override any defined values
                setattr(self, f.__name__[7:], self._feature_overrides[f.__name__])
                continue

            setattr(self, f.__name__[7:], f(buffer=self._buffer, filename=self._filename).result )


    def todict(self):
        result = {}
        for key, value in self.__dict__.items():
            if not key.startswith('_'):
                result[key] = value

        return result

    def safedict(self):
        result = {}
        for key, value in self.__dict__.items():
            if not key.startswith('_'):
                result['hashdd_{}'.format(key)] = value
        return result

    def __str__(self):
        return str(self.todict())


if __name__ == '__main__':
    raise Exception('Cannot run this module directly.')
