# hashdd

pyhashdd is a library for building hash databases and interacting with the [hashdd.com](https://www.hashdd.com) API. For detailed information about the API, see the [API documentation](https://github.com/hashdd/api_documentation). 

# Installation

With all prerequisites installed, you can install pyhashdd with `pip`:

```
pip install git+https://github.com/hashdd/pyhashdd.git
```

## Prerequisites 

### Ubuntu
```
sudo apt-get install libfuzzy-dev
sudo apt-get install libmhash-dev
```

### OSX/Darwin Prerequisites
```
brew install ssdeep
```

**Note: ** Due to a [bug in py-mhash](https://github.com/niwinz/py-mhash/pull/4), pyhashdd on OSX may cause a free error when generating certain hash types. As a workaround until the maintainer accepts the open pull request, please install from this repository:

```
pip install git+https://github.com/brad-anton/py-mhash.git
```

# Command Line Examples

To calculate the hash of a specific file (`-f sample`) and look it up (`-l`) in the hashdd.com database:
```
hashdd -l -f sample.exe
```

To recusively (`-r goodfiles/`) calculate the SHA256 hashes of files in the `goodfiles/` directory and add those hashes to a new bloom filter (the bloom filter is stored in `hashdd.bloom`): 

```
hashdd -b -r goodfiles/
```

With the bloom filter created, the `-b` option now compares calculated hashes to the bloom. To calculate the SHA256 hash of `sample.exe` (`-f sample.exe`) and check if it is within the bloom filter (`-b`):

```
hashdd -b -f sample.exe
```

To calculate all hashes (`--all`) and output them to the screen (`-s`):
```
hashdd -s -f sample.exe --all
```

To calculate a specific hash type:
```
hashdd -s -f sample.exe -a md5w
```

# API Client Examples

To query the hashdd.com API for a basic status:

```
>>> from hashdd.api import client
>>> c = client(None) # Basic status does not require an api_key, thus the None argument
>>> c.status('39E1D81353B1002E5043317CE75FA966FDD8DB215E57BC6F72681673CDDA561C')
{u'39E1D81353B1002E5043317CE75FA966FDD8DB215E57BC6F72681673CDDA561C': {u'known_level': 1, u'result': u'SUCCESS'}, u'result': u'SUCCESS'}
```

