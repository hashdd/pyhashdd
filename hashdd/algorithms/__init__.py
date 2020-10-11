"""
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
import os
import glob
from warnings import warn

# Detect all modules
for fullname in glob.glob(os.path.dirname(__file__) + "/*.py"):
    name = os.path.basename(fullname)
    if name[:-3] == "__init__" or name[:-3] == "algorithm" or not name.startswith('hashdd_'):
        pass
    else:
        try:
            __import__("hashdd.algorithms." + name[:-3])
        except (Exception) as e:
            msg = ("{} import aborted due to ImportError. Certain modules"
                    " can only be run on specific operating systems, or require compilation."
                    " It is safe to ignore this message unless you'd like to use this specific"
                    " Algorithm.".format(name[:-3]))
            warn(msg)
            warn(e)
            pass

