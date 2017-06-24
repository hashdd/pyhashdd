"""
hashdd/utils.py
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

import requests
import re


from requests.exceptions import HTTPError, ConnectionError
from urlparse import urlparse
from tempfile import NamedTemporaryFile
from os.path import basename

from hashdd import hashdd
from constants import Features

def filename_candidate(candidate):
    if '.' in candidate:
        if len(candidate.split('.')[-1]) < 5:
            return True
    return False

def download_and_hash(url, store_plaintext=False):
    with NamedTemporaryFile() as f:
        print 'Downloading: {}'.format(url)
        print 'Writing to temporary file: {}'.format(f.name)

        filename = basename(urlparse(url).path)

        try:
            r = requests.get(url, stream=True)

            r.raise_for_status()

            if not filename_candidate(filename):
                if 'content-disposition' in r.headers:
                    filename = re.findall("filename=(.+)", r.headers['content-disposition'])
                else:
                    filename = 'unknown'

            for chunk in r.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
        except (HTTPError, ConnectionError) as e:
            print 'Exception raised while downloading file: {}'.format(e)
            return None

        print 'Downloaded file! Using filename: {}'.format(filename)
        feature_overrides = { Features.FILE_NAME.value: [ filename ], 
            Features.FILE_ABSOLUTE_PATH.value: [ None ],
            Features.SOURCE_URLS.value: [ url ]}


        h = hashdd(filename=f.name, store_plaintext=store_plaintext, feature_overrides=feature_overrides)
        return h


if __name__ == '__main__':
    print 'Cannot run this file directly!'
