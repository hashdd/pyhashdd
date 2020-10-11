import zipfile

from .compressed_file import CompressedFile 

class ZIPFile (CompressedFile):
    magic = '\x50\x4b\x03\x04'
    file_type = 'zip'
    mime_type = 'compressed/zip'

    def open(self):
        return zipfile.ZipFile(self.f)

    def extract(self, tmp_dir=None):
        z = self.open()
        return [ z.extract(item, path=tmp_dir) for item in z.namelist()[:self.MAX_FILES] ]

