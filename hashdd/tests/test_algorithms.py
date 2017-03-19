"""
test_algorithms.py
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

import unittest

from hashdd import hashdd

from uuid import UUID


class TestAlgorithms(unittest.TestCase):
    h = hashdd(filename='sample.exe')

    def test_md2(self):
        self.assertEqual(self.h.result['hashdd_md2'], '67F5641272E1C37A3198D497E0268F1B')

    def test_md4(self):
        self.assertEqual(self.h.result['hashdd_md4'], '7875BEB6F3F889FE3013D6E8181D48BE')

    def test_md5(self):
        self.assertEqual(self.h.result['hashdd_md5'], '6C93F080B3CC1D15955AF589FE5D021A')

    def test_md5w(self):
        self.assertEqual(self.h.result['hashdd_md5w'], '670054AF1AD8A8DE128F9F8C0E94836C')

    def test_sha1(self):
        self.assertEqual(self.h.result['hashdd_sha1'], '8C2429DB2B3E0550C0E4964E7AE605ACD8FF5AB3')

    def test_sha224(self):
        self.assertEqual(self.h.result['hashdd_sha224'], '01FBFE4143EB82E58569CCC9308048F499A595B1A13EEED90C60D2B6')

    def test_sha256(self):
        self.assertEqual(self.h.result['hashdd_sha256'], '39E1D81353B1002E5043317CE75FA966FDD8DB215E57BC6F72681673CDDA561C')

    def test_sha384(self):
        self.assertEqual(self.h.result['hashdd_sha384'], 'FFDAB803259DF5C1A76D9DA51CDD30644A8206FF306A80C35D03E48A9D391E616370F8B2896085966E5CEB33D5ACBA39')

    def test_sha512(self):
        self.assertEqual(self.h.result['hashdd_sha512'], '60E218973D5493564C617CF76A0C82DA258095E4576ED51A498F90159A174AF69C3AD328ECC8DDBFE7BCAD2AA61E9889CE96D8BB7755A33C71146F311D653865')

    def test_tiger128(self):
        self.assertEqual(self.h.result['hashdd_tiger128'], 'F9A5C8809291B3BB85F7217F29810AA0')

    def test_tiger160(self):
        self.assertEqual(self.h.result['hashdd_tiger160'], 'F9A5C8809291B3BB85F7217F29810AA0A074BCB1')

    def test_tiger192(self):
        self.assertEqual(self.h.result['hashdd_tiger192'], 'F9A5C8809291B3BB85F7217F29810AA0A074BCB1B49ACE41')

    def test_ripemd128(self):
        self.assertEqual(self.h.result['hashdd_ripemd128'], 'F32A0D98929C70792E94E9656FD54E82')

    def test_ripemd160(self):
        self.assertEqual(self.h.result['hashdd_ripemd160'], 'B60D032AC971D19D0F05C6FAD8C90FCCBE25AD6A')

    def test_ripemd256(self):
        self.assertEqual(self.h.result['hashdd_ripemd256'], 'FD1E6FD68CAE1DD51146FD78BE3883555812A45FBD64548E9DB7533C6D30821B')

    def test_ripemd320(self):
        self.assertEqual(self.h.result['hashdd_ripemd320'], '202D0DDAA594F2191BFD98602EBAD1FC85DFFE23DBAA1F2129BB335C7CB8E3BC38C477F3A40D8ECB')

    def test_haval128(self):
        self.assertEqual(self.h.result['hashdd_haval128'], '0201C2C2F2FD3A38036FE5D566C34974')

    def test_haval160(self):
        self.assertEqual(self.h.result['hashdd_haval160'], '8E324AFD3ADA3441AF539E589705E70394CDB508')

    def test_haval192(self):
        self.assertEqual(self.h.result['hashdd_haval192'], '084C9727950ABD6629BC43594FAFB2474DDFEAC9E3790A2D')

    def test_haval224(self):
        self.assertEqual(self.h.result['hashdd_haval224'], 'A36CBEF0F3A26F0EBDC7F169B2B97AF84B27A1AD5AABC146F50AC131')

    def test_haval256(self):
        self.assertEqual(self.h.result['hashdd_haval256'], '8A120CE2C67582EC5B6360B283F46F9BEC75735558420287F5EE41A249798B57')

    def test_snefru128(self):
        self.assertEqual(self.h.result['hashdd_snefru128'], '1918A341C2C04C56C75FD3DA0B1A6F06')

    def test_snefru256(self):
        self.assertEqual(self.h.result['hashdd_snefru256'], '10119ED9CCA39C7D3F14471B9C29BFFA9F560145D96542CD73E5FD721F625B20')

    def test_gost(self):
        self.assertEqual(self.h.result['hashdd_gost'], '68F5124FB7B3EAF3470B43582B83670338583B328023B23BDAF97ACD10D76787')

    def test_whirlpool(self):
        self.assertEqual(self.h.result['hashdd_whirlpool'], 'E503B69D61F038F526DB42A09BA60B1231DCA9ED685C5FCF9CD1CDDF63940A03F27F34DA0A6952DBE3B8B3E9D0B56A2E26F003685D1E56590325D348C5248D04')

    def test_alder32(self):
        self.assertEqual(self.h.result['hashdd_adler32'], '77B3C08A')

    def test_ssdeep(self):
        self.assertEqual(self.h.result['hashdd_ssdeep'], '96:hFIe+kdd/6A6Kdt4DmITQi5/0HcsQXLCWSzrSVAB1JMxCtoL6:/IexCAwMi5MHLiCWSzrSVQ1JMYo')

    def test_crc16(self):
        self.assertEqual(self.h.result['hashdd_crc16'], 'EAE8')

    def test_crc16_ccitt(self):
        self.assertEqual(self.h.result['hashdd_crc16_ccitt'], 'F07A')

    def test_crc32b(self):
        self.assertEqual(self.h.result['hashdd_crc32b'], 'BC5E1E30')

    def test_content_hash(self):
        self.assertEqual(self.h.result['hashdd_content_hash'], '1A2E7229BA84BC8A23794B75A7457B5FA449D4D2998B32B52FD30417E7929164')

    def test_uuid4(self):
        self.assertTrue(UUID(self.h.result['hashdd_uuid4']))



if __name__ == '__main__':
    unittest.main()
