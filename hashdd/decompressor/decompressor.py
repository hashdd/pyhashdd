from os.path import isfile

from .formats.zip_file import ZIPFile
from .formats.compressed_file import TempDirectory

class Decompressor(object):
    def __init__(self, f):
        self.f = f

    def get_fmt(self):
        magic = self.f.read(8)
        self.f.seek(0)
        for fmt in [ ZIPFile ]:
            if fmt.is_magic(magic):
                return fmt 
        return None

    def extract(self, fmt, tmp_dir):
        compressed = fmt(self.f)
        return [ f for f in compressed.extract(tmp_dir) if isfile(f) ]
