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

        try:
            res = requests.post(ep, data=data, files=files, verify=self.verify_ssl)
            res.raise_for_status()
        except (requests.exceptions.Timeout, requests.exceptions.HTTPError) as e:
            raise Exception('[!] Unable to query hashdd: {}'.format(e))

        return res.json()

    def upload(self, filename, absolute_path=None, product_code=None, opsystem_code=None):
        """Upload a new file to hashdd.

        Keyword Arguments:
        filename -- Full path of file to upload. 
        absolute_path -- Value to define where on the file system this file is present.
        product_code -- NSRL RDS Product Code.
        opsystem_code -- NSRL RDS Operating System Code.
        """
        files = { 'file': open(filename, 'rb') }

        data = {} 
        if absolute_path is not None:
            data['absolute_path'] = absolute_path

        if product_code is not None:
            data['product_code'] = product_code 

        if opsystem_code is not None:
            data['opsystem_code'] = opsystem_code 

        return self._post('upload', files=files, params=data)

    def status(self, hash_value):
        """Check the status of a hash in hashdd.

        Keyword Arguments:
        hash_value -- Some hash to check, usually good to only use md5, sha1, sha256 
        """
        if isinstance(hash_value, list):
            # Deduplicate
            hash_value = list(set(hash_value)) 
            if len(hash_value) > 500:
                # TODO: write simple function to chunk up requests
                raise Exception('hashdd api only supports 500 hashes per query, please split your list up across multiple requests')

        params = { 'hash': hash_value }

        return self._post('', params=params)


