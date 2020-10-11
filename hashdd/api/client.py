"""
api/client.py
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
import os

from hashdd.constants import MAX_SIZE, Status

BATCH_SIZE = 100

class client:
    def __init__(self, api_key, host="api.hashdd.com", port=443, ssl=True, verify_ssl=True):
        """API Client for hashdd.com

        Keyword Arguments:
        api_key -- String containing your hashdd.com API key
        host -- String containing the hostname of the hashdd.com API server
        port -- Integer value containing the port to use when connecting to host
        ssl -- Boolean value defining whether or not SSL should be used. Non-SSL 
            connections over TCP 443 is not supported.
        verify_ssl -- Boolean value defining whether or not to validate SSL certificates.

        """
        self.api_key = api_key
        self.verify_ssl = verify_ssl

        self.server = 'https://{}:{}'.format(host, port)
        if not ssl:
            if port == 443:
                port = 80
            self.server = 'http://{}:{}'.format(host, port)

    def _post(self, endpoint, params=None, files=None):
        """Internal function to prep and make POST requests to the server.
        """
        ep = '{}/{}'.format(self.server, endpoint)

        data = { 'api_key': self.api_key }
        if params:
            data.update(params)

        headers = requests.utils.default_headers()
        headers.update({ 'User-Agent': 'pyhashdd/0.x.x'})

        try:
            res = requests.post(ep, data=data, headers=headers, 
                    files=files, verify=self.verify_ssl)
            res.raise_for_status()
        except (requests.exceptions.Timeout, requests.exceptions.HTTPError) as e:
            raise Exception('[!] Unable to query hashdd: {}'.format(e))

        return res.json()

    def upload(self, filename, absolute_path=None, product_code=None, opsystem_code=None, known_level=None):
        """Upload a new file to hashdd.

        Keyword Arguments:
        filename -- Full path of file to upload. 
        absolute_path -- Value to define where on the file system this file is present.
        product_code -- NSRL RDS Product Code.
        opsystem_code -- NSRL RDS Operating System Code.
        """

        statinfo = os.stat(filename)
        if statinfo.st_size >= MAX_SIZE:
            print('File is too large, skipping')
            return { 'result': Status.FAILURE.value, 'message': 'File is too large' }

        files = { 'file': open(filename, 'rb') }

        data = {} 
        if absolute_path is not None:
            data['absolute_path'] = absolute_path

        if product_code is not None:
            data['product_code'] = product_code 

        if opsystem_code is not None:
            data['opsystem_code'] = opsystem_code 

        # Doesn't do anything at the moment..
        if known_level is not None:
            data['known_level'] = known_level

        return self._post('upload', files=files, params=data)

    def chunker(self, l, n=BATCH_SIZE):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def _batch(self, action, hashes):
        """Chunks up large batches and sends them in groups of BATCH_SIZE.

        Keyword Arguments:
        action -- Callable to action (e.g. self.status)
        hashes -- A list of hashes to chunk up.
        """
        batch_results =  { 'chunk_results': [] }
        for chunk in self.chunker(hashes):
            r = action([ i[1] for i in chunk ])

            # Track the overall result of each chunk
            batch_results['chunk_results'].append( { 'result': r['result'] } )

            for i in chunk:
                filename, h = i
                if h in r:
                    batch_results[h] = r[h]
                    batch_results[h]['filename'] = filename
        return batch_results

    def status(self, hash_value):
        """Check the status of a hash in hashdd.

        Keyword Arguments:
        hash_value -- Some hash to check, usually good to only use md5, sha1, sha256 
        """
        if isinstance(hash_value, list):
            # Deduplicate
            hash_value = list(set(hash_value)) 
            if len(hash_value) > BATCH_SIZE:
                return self._batch(self.status, hash_value)

        params = { 'hash': hash_value }

        return self._post('', params=params)


