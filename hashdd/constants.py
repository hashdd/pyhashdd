"""
hashdd/constants.py
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
from enum import Enum

class HashLengths(Enum):
    SHA1 = 40
    MD5 = 32
    SHA256 = 64
    SHA512 = 128
    CRC32 = 8

class Algorithms(Enum):
    # Hashes
    MD2 = 'hashdd_md2'
    MD4 = 'hashdd_md4'
    MD5 = 'hashdd_md5' 
    MD5W = 'hashdd_md5w' 
    SHA1 = 'hashdd_sha1' 
    SHA256 = 'hashdd_sha256'
    SHA384 = 'hashdd_sha384'
    SHA512 = 'hashdd_sha512' 
    SHA3 = 'hashdd_sha3_224' 
    SHA3_224 = 'hashdd_sha3_224' 
    SHA3_256 = 'hashdd_sha3_256'
    SHA3_384 = 'hashdd_sha3_384'
    SHA3_512 = 'hashdd_sha3_512' 
    CRC16 = 'hashdd_crc16'
    CRC16_CCITT = 'hashdd_crc16_ccitt'
    CRC32 = 'hashdd_crc32'
    FCS16 = 'hashdd_fcs16'
    FCS32 = 'hashdd_fcs32'
    SSDEEP = 'hashdd_ssdeep'
    RIPEMD128 = 'hashdd_ripemd128'
    RIPEMD160 = 'hashdd_ripemd160'
    HAVAL5_256 = 'hashdd_haval5_256'
    GHASH32_3 = 'hashdd_ghash32_3'
    GHASH32_5 = 'hashdd_ghash32_5'
    GOST = 'hashdd_gost'
    TIGER = 'hashdd_tiger'
    CONTENT_HASH = 'hashdd_content_hash'
    SDHASH = 'hashdd_sdhash'
    TLSH = 'hashdd_tlsh'

    # Supported hashes to search on hashdd.com, supporting more is easy.. just do it already! TODO
    SUPPORTED_HASHES = [ SHA1, MD5, SHA256, SHA512, CRC32 ]


class Features(Enum):
    UUID = 'hashdd_uuid4'
    KNOWN_LEVEL = 'hashdd_known_level'
    IMPORT_DATE = 'hashdd_import_date'
    SIZE = 'hashdd_size'
    DATA_SOURCE = 'hashdd_data_source'
    VOTES = 'hashdd_votes'  
    REQUESTED = 'hashdd_requested'
    USER = 'hashdd_user'
    PLAINTEXT = 'hashdd_plaintext'

    # File-specific
    FILE_NAME = 'hashdd_file_name'
    FILE_CREATION_DATE = 'hashdd_file_creation_date'
    FILE_ABSOLUTE_PATH = 'hashdd_file_absolute_path'
    FILE_FULL_PATH = 'hashdd_file_full_path'
    FILE_MAGIC = 'hashdd_filemagic' # TODO: Fix this to be hashdd_file_magic
    FILE_MIME = 'hashdd_mime' # TODO: fix this to be hashdd_file_mime
    FILE_PRODUCT_NAME = 'hashdd_product_name'
    FILE_PRODUCT_VERSION = 'hashdd_product_version'
    FILE_PRODUCT_MANUFACTURER = 'hashdd_product_manufacturer'
    FILE_PRODUCT_CODE= 'hashdd_product_code'
    FILE_OPSYSTEM_CODE = 'hashdd_opsystem_code'
    FILE_ARCHITECTURE = 'hashdd_architecture'

class Profile(Enum):
    ALL = [ a for a in Algorithms if a is not Algorithms.SUPPORTED_HASHES ] + [ f for f in Features ]

class Status(Enum):
    KNOWN_LEVEL_GOOD = 'Good'
    KNOWN_LEVEL_BAD = 'Bad'
    KNOWN_LEVEL_UNKNOWN = 'Unknown'
    NOT_FOUND = 'NOT_FOUND'
    INVALID = 'INVALID_HASH'
    SUCCESS = 'SUCCESS'
    EXISTS = 'EXISTS'
    FAILURE = 'FAILURE'
    UNAUTHORIZED = 'UNAUTHORIZED'

