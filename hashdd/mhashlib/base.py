# -*- coding: utf-8 -*-

from . import api
import binascii
import ctypes

class BaseHash(object):
    _hash_type = None
    _result = None

    def __init__(self, data=None):
        self.td = api.lib.mhash_init(self._hash_type)
        if self.td is None:
            raise RuntimeError("Unexpected error")

        if data is not None:
            if not isinstance(data, bytes):
                raise RuntimeError("data must be bytes instance")

            api.lib.mhash(self.td, data, len(data))

    def update(self, data):
        if self._result is not None:
            return

        if not isinstance(data, bytes):
            raise RuntimeError("data must be bytes instance")

        api.lib.mhash(self.td, data, len(data))

    def digest(self):
        if self._result is not None:
            return self._result

        size = api.lib.mhash_get_block_size(self._hash_type)
        cvp = api.lib.mhash_end(self.td)
        self._result = ctypes.cast(cvp, ctypes.POINTER(ctypes.c_char))[:size]
        api.c_lib.free(cvp)

        return self._result

    def hexdigest(self):
        return binascii.hexlify(self.digest())


class gost(BaseHash):
    _hash_type = api.MHASH_GOST

class tiger192(BaseHash):
    _hash_type = api.MHASH_TIGER192

class tiger128(BaseHash):
    _hash_type = api.MHASH_TIGER128

class tiger160(BaseHash):
    _hash_type = api.MHASH_TIGER160

class whirlpool(BaseHash):
    _hash_type = api.MHASH_WHIRLPOOL

class crc32(BaseHash):
    _hash_type = api.MHASH_CRC32

class md5(BaseHash):
    _hash_type = api.MHASH_MD5

class sha1(BaseHash):
    _hash_type = api.MHASH_SHA1

class haval256(BaseHash):
    _hash_type = api.MHASH_HAVAL256

class ripemd160(BaseHash):
    _hash_type = api.MHASH_RIPEMD160

class crc32b(BaseHash):
    _hash_type = api.MHASH_CRC32B

class haval224(BaseHash):
    _hash_type = api.MHASH_HAVAL224

class haval192(BaseHash):
    _hash_type = api.MHASH_HAVAL192

class haval160(BaseHash):
    _hash_type = api.MHASH_HAVAL160

class haval128(BaseHash):
    _hash_type = api.MHASH_HAVAL128

class sha256(BaseHash):
    _hash_type = api.MHASH_SHA256

class adler32(BaseHash):
    _hash_type = api.MHASH_ADLER32

class sha224(BaseHash):
    _hash_type = api.MHASH_SHA224

class sha512(BaseHash):
    _hash_type = api.MHASH_SHA512

class sha384(BaseHash):
    _hash_type = api.MHASH_SHA384

class ripemd128(BaseHash):
    _hash_type = api.MHASH_RIPEMD128

class ripemd256(BaseHash):
    _hash_type = api.MHASH_RIPEMD256

class ripemd320(BaseHash):
    _hash_type = api.MHASH_RIPEMD320

class snefru128(BaseHash):
    _hash_type = api.MHASH_SNEFRU128

class snefru256(BaseHash):
    _hash_type = api.MHASH_SNEFRU256


tiger = tiger192
haval = haval256
ripemd = ripemd160
