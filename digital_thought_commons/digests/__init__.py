import hashlib


def calc_string_digests(string: str, process_extended: bool = False):
    return Digest(string.encode(encoding='utf-8'), process_extended=process_extended)


def calc_bytes_digests(data: bytes, process_extended: bool = False):
    return Digest(data, process_extended=process_extended)


class Digest:

    def __init__(self, val: bytes, process_extended: bool = False) -> None:
        self._process_extended = process_extended
        self._sha256 = hashlib.sha256(val).hexdigest()
        self._sha1 = hashlib.sha1(val).hexdigest()
        self._md5 = hashlib.md5(val).hexdigest()

        self._sha512 = 'NOT_CALCULATED'
        if self._process_extended:
            self._sha512 = hashlib.sha512(val).hexdigest()

    def sha256(self):
        return self._sha256

    def sha1(self):
        return self._sha1

    def md5(self):
        return self._md5

    def sha512(self):
        return self._sha512

    def as_dict(self) -> dict:
        json = {'md5': self._md5, 'sha1': self._sha1, 'sha256': self._sha256}
        if self._process_extended:
            json['sha512'] = self._sha512

        return json
