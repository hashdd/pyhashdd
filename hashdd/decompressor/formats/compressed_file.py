"""
Originally from https://stackoverflow.com/questions/13044562/python-mechanism-to-identify-compressed-file-type-and-uncompress
"""

from tempfile import mkdtemp
from shutil import rmtree 

class TempDirectory(object):
    name = None
    def __enter__(self):
        self.name = mkdtemp()
        return self.name

    def __exit__(self, type, value, traceback):
        rmtree(self.name)

class CompressedFile (object):
    magic = None
    file_type = None
    mime_type = None
    proper_extension = None
    MAX_FILES = 1000

    def __init__(self, f):
        # f is an open file or file like object
        self.f = f
        self.accessor = self.open()

    @classmethod
    def is_magic(self, data):
        return data.startswith(self.magic)

    def open(self):
        return None

    def extract(self):
        return None

