#!/usr/bin/env python
"""
hashddcli.py
@brad_anton

Command line interface to pyhashdd and the hashdd.com API. 

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
import logging
import argparse
import os 

from os.path import join, isfile, isdir
from pybloomfilter import BloomFilter
from termcolor import colored
from json import dumps
from sys import exit, stderr

from hashdd import hashdd
from hashdd.constants import Algorithms, Features 

class hashddcli(object):
    """hashdd cli offers a couple main features:
        1. Scan files and create hashes
        2. Create a bloom filter from a list of files
        3. Scan files, compute hashes, and compare those hashes to a bloom filter
        4. Show a list of available 
    """
    def __init__(self, bloom=None, compute=None, show=None, filename=None, directory=None, algorithms=[ Algorithms.SHA256.value ],
            nomatch=None, plaintext=None, include_extensions=None, exclude_extensions=None, ignore_errors=False,             
            compute_all=None):
        self.logger = logging.getLogger(name=self.__class__.__name__)

        self.bloom = bloom
        self.compute = compute
        self.show = show
       
        if not show:
            # If we specify show, then we ignore filename, directory
            self._check_filename_directory(filename, directory)

        self.filename = filename
        self.directory = directory
        
        self.algorithms = self._check_algorithms(algorithms)

        self.nomatch = nomatch
        self.exclude_extensions = exclude_extensions
        self.ignore_errors = ignore_errors
        self.include_extensions = include_extensions
        self.compute_all = compute_all

        self.features = [ Features.FILE_ABSOLUTE_PATH.value ]
        if plaintext is not None:
            self.features.append(Features.PLAINTEXT.value)
        self.plaintext = plaintext

        if compute_all == True:
            self.algorithms = None
            self.features = None

    def _check_filename_directory(self, filename, directory):
        if filename is not None:
            if not isfile(filename):
                raise Exception('Invalid filename')

        if directory is not None:
            if not isdir(directory):
                raise Exception('Invalid directory')

        if filename is None and directory is None:
            raise Exception('Must specify filename or directory')


    def _check_algorithms(self, algorithms, default=['sha256']):
        if algorithms is None:
            # hashddcli treats None as undefined but hashdd treats it as 'all'
            return default

        if not isinstance(algorithms, list):
            try:
                if algorithms.lower() == 'all':
                    return None
            except:
                pass

            return default

        result = []
        for a in algorithms:
            algo = a.lower()
            if algo == 'all':
                return None

            if algo.startswith('hashdd_'):
                candidate = algo
            else:
                candidate = 'hashdd_{}'.format(algo)

            if Algorithms(candidate):
                result.append(candidate)

        return result

    def _show(self):
        for i in hashdd.algorithms_available():
            print('{}'.format(i))
        return hashdd.algorithms_available() 

    def _compute_result(self):
        if self.filename is not None:
            h = hashdd(filename=self.filename, 
                    store_plaintext=self.plaintext, 
                    algorithms=self.algorithms, 
                    features=self.features)
            return [ h.safedict() ]
       
       # No filename set, so it must be a directory
        return self._recurse()

    def _compute(self):
        result = self._compute_result()
        self.print_entry(result)
        return result 

    def _bloom(self, results, bloomfilter_filename='hashdd.bloom'):
        if not isfile(bloomfilter_filename):
            # If the bloom filter doesn't exist, "bloom" creates it
            return self._create_bloom(results)

        else:
            # If the bloom filter already exists, we compare it
            matches = self._check_bloom(results, self.algorithms)
            if self.nomatch:
                self.print_results_unmatched(matches)
            else:
                self.print_results(matches)
            return matches 
    
    def run(self):
        self.logger.info(self.bloom, self.compute, self.show)
        if self.show:
            return self._show()
        
        # After this point, we expect the file/dir options to be set.
        if self.compute:
            return self._compute()

        if self.bloom:
            results = self._compute()
            return self._bloom(results)

        return None

    @staticmethod
    def print_entry(result):
        try:
            print(dumps(result))
        except:
            print(result)

    def _recurse(self):
        """Recusively walks a directory starting at 'starting' and creates hashdd
        objects from each file encountered. 

        Keyword Arguments:
        starting -- Directory to start recursing.
        store_plaintext -- Boolean value defining whether or not we should store the plaintext
            of the discovered file. 
        algorithms -- a list of hashdd.constants.Algorithms to include in the result
        features -- a list of hashdd.constants.Features to include in the result
        """
        results = []
        visited = set()

        for root, dirs, files in os.walk(self.directory):
            for f in files:
                fp = join(root, f)
                if fp in visited:
                    continue
                visited.add(fp)

                extension = f.split('.')[-1]
                if self.exclude_extensions and extension in self.exclude_extensions:
                    continue

                if self.include_extensions and extension not in self.include_extensions:
                    continue

                try:    
                    h = hashdd(filename=join(root, f), 
                            store_plaintext=self.plaintext, 
                            algorithms=self.algorithms, 
                            features=self.features)
                    results.append(h.safedict())
                except:
                    if not self.ignore_errors:
                        raise
                    else:
                        results.append({ Features.FILE_ABSOLUTE_PATH.value: [fp, ]})
        return results

    def _create_or_return_bloom(self, elements=None, filename='hashdd.bloom'):
        """Creates and/or returns a bloom filter. If the filter
        does not exist, it will be created using the items in elements. 
        If it does exist, it will be returned. 

        Keyword Arguments:
        elements -- A list of strings to add to the bloom filter
        filename -- The filename where the bloom filter should be stored
        """
        if os.path.isfile(filename):
            bf = BloomFilter.open(filename)
        else:
            print('[+] Creating Bloom filter with {} elements'.format(len(elements)))
            if not elements:
                raise Exception('Attempting to build a bloom filter, but have no items to add')

            limit = len(elements)
            bf = BloomFilter(limit, 0.0001, '{}'.format(filename))
            for element in elements:
                bf.add(element)

        return bf

    def _create_bloom(self, results):
        elements = []
        for result in results:
            # There shouldn't be multiple algorithms for a bloom, but if there are, we'll use the first
            algo = self.algorithms[0] 
            elements.append(result[algo])
                
        return self._create_or_return_bloom(elements)

    def _check_bloom(self, results, algorithms):
        bf = self._create_or_return_bloom()
        for result in results:
            for algo in algorithms:
                if result[algo] in bf:
                    if 'match_count' not in result:
                        result['match_count'] = 0
                    result['match_count'] += 1

                    if 'matches' not in result:
                        result['matches'] = []
                    result['matches'].append(algo)
        return results

    def print_results(self, results):
        for result in results:
            if 'match_count' in result:
                print(colored(result['hashdd_file_absolute_path'], 'green'))
            else:
                print(colored(result['hashdd_file_absolute_path'], 'red'))

    @staticmethod
    def print_results_unmatched(results):
        for result in results:
            if 'match_count' not in result:
                print(colored(result['hashdd_file_absolute_path'], 'red'))

    @staticmethod
    def build_hash_list(results, algorithm):
        return [ result[algorithm] for result in results ]

    @staticmethod
    def parse_args(args):
        parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
            description=( 'pyhashdd - your hashing bff'),
            epilog=None)

        # This parent parser is for all of the
        parent_parser = argparse.ArgumentParser(add_help=False)
        parent_parser.add_argument('-i', '--ext-include', nargs='*', default=[],
                help='A space-separated list of file extensions to include. (Default: All)')
        parent_parser.add_argument('-e', '--ext-exclude', nargs='*', default=[],
                help='A space-separated list of file extensions to exclude. (Default: None)')
        parent_parser.add_argument('-q', '--ignore_errors', dest='ignore_errors',
                default=False, action="store_true",
                help='Ignore errors and keep processing filed')
        parent_parser.add_argument('--all', dest='compute_all', action='store_true',
                help='Compute all features and hashes (Default: No)')


        file_parent_group = parent_parser.add_mutually_exclusive_group(required=True)
        file_parent_group.add_argument('-f', '--file', dest='filename', type=str, nargs='?',
                help='Single file to process')
        file_parent_group.add_argument('-d', '--directory', dest='directory', type=str, nargs='?',
                help='Directory to recursively process')

        subparsers = parser.add_subparsers(help='Action to perform', dest='command')
        show_parser = subparsers.add_parser("show",
                help='Show the list of algorithms available to hashdd on this system.')

        compute_parser = subparsers.add_parser("compute",
                help='Compute features/algorithms and print to screen.',
                parents=[parent_parser])
        compute_parser.add_argument('-a', '--algorithms', nargs='*', default=[ 'sha256' ],
                help='A list of algorithms to include. (Default: sha256)')
        compute_parser.add_argument('-p', '--plaintext', action='store_true',
                help='Stored plaintext of files profiled (Default: false)')

        bloom_parser = subparsers.add_parser("bloom",
                help='Create a Bloom filter with algorithm results or, if it exists, compare the output to the bloom.',
                parents=[parent_parser])
        bloom_parser.add_argument('-n', '--nomatch', action='store_true',
                help='When comparing, only print files not included within the Bloom filter')

        ns = parser.parse_args()
        if ns.command is None:
            parser.print_help()
            return None

        return ns

