"""
hashdd_opsystem_code.py
@brad_anton

This is really just a placeholder module. It's purpose is to define
a NSRL RDS-friendly operating system code, and should be used by
providing a 'hashdd_opsystem_code' override called through profile()


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

class hashdd_opsystem_code(feature):
    def process(self):
        return [ None ]

