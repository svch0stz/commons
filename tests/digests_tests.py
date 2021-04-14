import unittest

from digital_thought_commons import digests


class TestDigests(unittest.TestCase):

    def test_string_digests(self):
        digest = digests.calc_string_digests("This is a test string", process_extended=True)
        self.assertEqual(digest.md5(), 'c639efc1e98762233743a75e7798dd9c')
        self.assertEqual(digest.sha256(), '717AC506950DA0CCB6404CDD5E7591F72018A20CBCA27C8A423E9C9E5626AC61'.lower())
        self.assertEqual(digest.sha1(), 'E2F67C772368ACDEEE6A2242C535C6CC28D8E0ED'.lower())
        self.assertEqual(digest.sha512(), 'B8EE69B29956B0B56E26D0A25C6A80713C858CF2902A12962AAD08D682345646B2D5F193BBE03997543A9285E5932F34BAF2C85C89459F25BA1CF43C4410793C'.lower())

    def test_bytes_digest(self):
        digest = digests.calc_bytes_digests("This is a test string".encode('utf-8'), process_extended=True)
        self.assertEqual(digest.md5(), 'c639efc1e98762233743a75e7798dd9c')
        self.assertEqual(digest.sha256(), '717AC506950DA0CCB6404CDD5E7591F72018A20CBCA27C8A423E9C9E5626AC61'.lower())
        self.assertEqual(digest.sha1(), 'E2F67C772368ACDEEE6A2242C535C6CC28D8E0ED'.lower())
        self.assertEqual(digest.sha512(),
                         'B8EE69B29956B0B56E26D0A25C6A80713C858CF2902A12962AAD08D682345646B2D5F193BBE03997543A9285E5932F34BAF2C85C89459F25BA1CF43C4410793C'.lower())

    def test_digests_to_dict(self):
        digest = digests.calc_string_digests("This is a test string", process_extended=True)
        json = digest.as_dict()
        self.assertEqual(json['md5'], 'c639efc1e98762233743a75e7798dd9c')
        self.assertEqual(json['sha256'], '717AC506950DA0CCB6404CDD5E7591F72018A20CBCA27C8A423E9C9E5626AC61'.lower())
        self.assertEqual(json['sha1'], 'E2F67C772368ACDEEE6A2242C535C6CC28D8E0ED'.lower())
        self.assertEqual(json['sha512'], 'B8EE69B29956B0B56E26D0A25C6A80713C858CF2902A12962AAD08D682345646B2D5F193BBE03997543A9285E5932F34BAF2C85C89459F25BA1CF43C4410793C'.lower())

    def test_update_digests(self):
        digest = digests.calc_string_digests("This is a test string", process_extended=True)
        digest.update_from_string("and another")
        self.assertEqual(digest.md5(), '9cc715fc7ee868e69464b85af305bf47')
        self.assertEqual(digest.sha256(), 'c42d312cc3f1e09e56109791e81be10953055b06b8fa729e760a4a04892ec0f4')
        self.assertEqual(digest.sha1(), '3cb90dea5074849a0da1c734c7738fe7db6523a6')
        self.assertEqual(digest.sha512(), '4227b48563622f64b4e9c7afcef8564b829ca18691cf332f5b97b22ac8e0f1aca03c0370132932e1105b1cec5662e57de679fde56aa0a211c88904bb41a2409c')

