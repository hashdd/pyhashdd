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
import os
import os.path

from requests.exceptions import HTTPError, ConnectionError
from urllib.parse import urlparse
from tempfile import NamedTemporaryFile
from os.path import basename, dirname
from hashlib import md5 

from .hashdd import hashdd
from .constants import Features, MAX_SIZE
from .decompressor import Decompressor, TempDirectory

def filename_candidate(candidate):
    if '.' in candidate:
        if len(candidate.split('.')[-1]) < 5:
            return True
    return False

def download(url, f):
    print('Downloading: {}'.format(url))
    try:
        r = requests.get(url, stream=True)
        r.raise_for_status()

        filename = basename(urlparse(r.url).path)

        if not filename_candidate(filename):
            if 'content-disposition' in r.headers:
                filename = re.findall("filename=(.+)", r.headers['content-disposition'])
            else:
                filename = 'unknown'

        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    except (HTTPError, ConnectionError) as e:
        print('Exception raised while downloading file: {}'.format(e))
        return None 

    f.seek(0)
    return filename 

def is_max(filename):
    statinfo = os.stat(filename)
    return statinfo.st_size >= MAX_SIZE

def hashdd_helper(filename, store_plaintext, feature_overrides):
        sp = store_plaintext if not is_max(filename) else False
        return hashdd(filename=filename, 
                store_plaintext=sp,
                feature_overrides=feature_overrides)


def extract_and_hash(f, url, parent, store_plaintext):
    d = Decompressor(f)
    fmt = d.get_fmt()
    if fmt is not None:
        with TempDirectory() as tmp_dir:
            extracted = d.extract(fmt, tmp_dir)
            for filename in extracted:
                yield hashdd_helper(filename, store_plaintext, { 
                    Features.FILE_NAME.value: [ basename(filename) ], 
                    Features.PARENTS.value: [ parent ], 
                    Features.FILE_ABSOLUTE_PATH.value: [ dirname(filename[len(tmp_dir)+1:]) ],
                    Features.SOURCE_URLS.value: [ url ] 
                    })

def download_and_hash(url, store_plaintext=False, decompress=False):
    with NamedTemporaryFile() as f:
        filename = download(url, f)
        if filename is not None:
            
            h = hashdd_helper(f.name, store_plaintext, { 
                Features.FILE_NAME.value: [ filename ], 
                Features.FILE_ABSOLUTE_PATH.value: [ None ],
                Features.SOURCE_URLS.value: [ url ] 
                })
            yield h
    
            if decompress:
                for result in extract_and_hash(f, url, h.sha256, store_plaintext=store_plaintext):
                    yield result
           
def get_dir_recursive(directory):
    """Recursively grabs the SHA1 sum of 
    all files starting at directory. For status checks. 
    """
    batch = []

    def hashfile(filename):
        with open(filename, 'rb') as f:
            return (filename, md5(f.read()).hexdigest().upper())

    for root, _, files in os.walk(directory):
        for f in files:
            batch.append(hashfile(os.path.join(root, f)))

    return list(set(batch))

if __name__ == '__main__':
    print('Cannot run this file directly!')
