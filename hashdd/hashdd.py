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
import logging

from os.path import join
from functools import partial

from hashdd.algorithms.algorithm import algorithm
from hashdd.features.feature import feature
from hashdd.constants import MAX_SIZE

class hashdd(object):
    CHUNK_SIZE=8192
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
        self._logger = logging.getLogger('hashdd')
        self._filename = filename
        self._buffer = buf
        self._store_plaintext = store_plaintext
        self._features = features
        self._feature_overrides = feature_overrides
        self._algorithms = algorithms
        self._filename_size = None
            

        if not self._filename and not self._buffer:
            raise Exception('Neither buf or filename is defined')

        if self._filename and self._buffer:
            raise Exception('Must define either buf or filename, both cannot be set')

        if self._filename:
            statinfo = os.stat(self._filename)
            if statinfo is None:
                raise Exception(f'Cannot stat filename {self._filename}')
            
            self._filename_size = statinfo.st_size
            if self._filename_size is None:
                raise Exception(f'Cannot read file size of {self._filename}')

            if self._filename_size >= MAX_SIZE:
                self._store_plaintext = False
        
        elif self._buffer:
            # No special handling for buffers
            pass

        self._generate_hashes()
        self._generate_profile()
    
    @staticmethod
    def algorithms_available():
        """Return a list of hashdd algorithms currently available"""
        available = []

        algos = list(hashlib.algorithms_available)
        for a in algorithm.__subclasses__():
            algos.append(a.__name__)

        for module in algos:
            if module.startswith('hashdd_'):
                available.append(module)

        return available

    def _runmod_algo(self, algorithmname):
        if not self._buffer and self._filename_size == 0:
            return None

        module = getattr(hashlib, algorithmname)

        hexdigest = None
        if self._buffer:
            # For buffers we use prefilter, for chunked files, we don't
            if module.prefilter(self._buffer):
                hexdigest = module(self._buffer).hexdigest()
        elif self._filename:
            m = module(b'')

            if m.implements_readfile:
                m.readfile(self._filename)
            else:
                with open(self._filename, 'rb') as f:
                    for chunk in iter(partial(f.read, self.CHUNK_SIZE), b''):
                        m.update(chunk)

            hexdigest = m.hexdigest()

        return hexdigest

    def _runmod_feature(self, modfeature):
        return modfeature(buffer=self._buffer, filename=self._filename).result

    def _generate_hashes(self):
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
                hexdigest = None
                try:
                    hexdigest = self._runmod_algo(module)
                except (Exception) as e:
                    self._logger.warning(f'Exception raised when calculating {module}, setting to None: {e}')
                    pass 
                    
                setattr(self, module[7:], hexdigest)

    def _generate_profile(self):
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

            result = None
            try:
                result = self._runmod_feature(f)
            except (Exception) as e:
                self._logger.warning(f'Exception raised when calculating {f.__name__}, setting to None: {e}')
                pass 

            setattr(self, f.__name__[7:], result) 


    def todict(self):
        result = {}
        for key, value in self.__dict__.items():
            if not key.startswith('_'):
                result[key] = value

        return result

    def safedict(self):
        """Return a dictionary that can be safely merged with another that may have 
        keys named after hashing algorithms (e.g. md5, sha256). It's considered safe 
        because the keys of the dictionary are prefixed with "hashdd_".
        """
        result = {}
        for key, value in self.__dict__.items():
            if not key.startswith('_'):
                result['hashdd_{}'.format(key)] = value
        return result

    def __str__(self):
        return str(self.todict())


if __name__ == '__main__':
    raise Exception('Cannot run this module directly.')
