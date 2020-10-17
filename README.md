# hashdd

pyhashdd is a library for building and using hash databases.

# Installation

With all prerequisites installed, you can install pyhashdd with `pip`:

```
pip install hashdd

```

# Docker

Build the container from the git root:
```
docker build -t hashdd .
```

Create a directory to scan, and copy our `sample.exe` into it.
```
mkdir files_to_scan/
cp tests/data/sample.exe files_to_scan/
```

Mount `files_to_scan/` and scan away!
```
docker run --rm -v "$PWD"/files_to_scan:/files_to_scan hashdd hashdd compute -d /files_to_scan
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

To recusively (`-d goodfiles/`) calculate the SHA256 hashes of files in the `goodfiles/` directory and add those hashes to a new bloom filter (the bloom filter is stored in `hashdd.bloom`): 

```
hashdd bloom -d goodfiles/

```

With the bloom filter created, the `bloom` option now compares calculated hashes to the bloom. To calculate the SHA256 hash of `sample.exe` (`-f sample.exe`) and check if it is within the bloom filter (`bloom`):

```
hashdd bloom -f sample.exe

```

To calculate (`compute`) all hashes (`--all`) and output them to the screen:
```
hashdd compute -f sample.exe --all

```

To calculate a specific hash type:
```
hashdd compute -f sample.exe -a md5w

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

# Testing
```
python -m unittest discover -s tests/
```

# `py-mhash` and `mhashlib`

Back in 2017 [we fixed an issue in py-mhash](https://github.com/niwinz/py-mhash/pull/4) which was merged into the git repository, however this fix was not built as part of the distribution in PyPi. Rather then rely on the package maintainer any further, we've bundled in `py-mhash` with hashdd. Please see the [py-mash license](https://github.com/niwinz/py-mhash/blob/master/LICENSE) for copyright information. 
