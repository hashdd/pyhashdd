# hashdd

pyhashdd is a library for building and using hash databases. It also serves as the client library for interacting with the [hashdd.com](https://www.hashdd.com) [API](https://github.com/hashdd/api_documentation), an online hash database. 

# Installation

With all prerequisites installed, you can install pyhashdd with `pip`:

```
pip install hashdd

```

## Prerequisites 

### Ubuntu
```
sudo apt-get install libfuzzy-dev libmhash-dev libffi-dev libssl-dev

```

### OSX/Darwin Prerequisites
```
brew install ssdeep

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

# Library Examples

To hash a file using all algorithms and features, then store the results in Mongo:

```
>>> from hashdd import hashdd
>>> h = hashdd(filename='sample.exe')
>>> from pymongo import MongoClient
>>> db = MongoClient().hashdd
>>> db.hashes.insert_one(h.result)

```

# API Client Examples

To query the hashdd.com API for a basic status:

```
>>> from hashdd.api import client
>>> c = client(None) # Basic status does not require an api_key, thus the None argument
>>> c.status('39E1D81353B1002E5043317CE75FA966FDD8DB215E57BC6F72681673CDDA561C')
{u'39E1D81353B1002E5043317CE75FA966FDD8DB215E57BC6F72681673CDDA561C': {u'known_level': 1, u'result': u'SUCCESS'}, u'result': u'SUCCESS'}

```

