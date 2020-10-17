# -*- coding: utf-8 -*-

import ctypes
import ctypes.util

def load_library():
    libpath = ctypes.util.find_library('mhash')
    return ctypes.CDLL(libpath), ctypes.CDLL(None)

MHASH_CRC32     = 0
MHASH_MD5       = 1
MHASH_SHA1      = 2
MHASH_HAVAL256  = 3
MHASH_RIPEMD160 = 5
MHASH_TIGER192  = 7
MHASH_GOST      = 8
MHASH_CRC32B    = 9
MHASH_HAVAL224  = 10
MHASH_HAVAL192  = 11
MHASH_HAVAL160  = 12
MHASH_HAVAL128  = 13
MHASH_TIGER128  = 14
MHASH_TIGER160  = 15
MHASH_SHA256    = 17
MHASH_ADLER32   = 18
MHASH_SHA224    = 19
MHASH_SHA512    = 20
MHASH_SHA384    = 21
MHASH_WHIRLPOOL = 22
MHASH_RIPEMD128 = 23
MHASH_RIPEMD256 = 24
MHASH_RIPEMD320 = 25
MHASH_SNEFRU128 = 26
MHASH_SNEFRU256 = 27


try:
    lib, c_lib = load_library()
    lib.mhash_init.argtypes = [ctypes.c_int]
    lib.mhash_init.restype = ctypes.c_void_p

    lib.mhash.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
    lib.mhash_end.argtypes = [ctypes.c_void_p]
    lib.mhash_end.restype = ctypes.c_void_p

    lib.mhash_get_block_size.argtypes = [ctypes.c_int]
    lib.mhash_get_block_size.restype = ctypes.c_int

    c_lib.free.argtypes = [ctypes.c_void_p]
except AttributeError:
    raise ImportError('mhash shared library not found or incompatible')
except (OSError, IOError):
    raise ImportError('mhash shared library not found.\n'
                      'you probably had not installed mhash library.\n')
