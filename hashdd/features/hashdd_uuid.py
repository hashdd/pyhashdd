"""
hashdd_uuid.py
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
from .feature import feature
from uuid import uuid4

class hashdd_uuid4(feature):
    """Generates a UUID4 uuid for use within a resulting
    hash. 

    Note: This is a random value every time its called, so
    don't expect to get a constant value over multiple runs
    of the same file. 
    """
    def process(self):
        return str(uuid4()).upper()

