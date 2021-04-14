import hashlib


class Digest:

    def __init__(self, val: bytes, process_extended: bool = False) -> None:
        self._process_extended = process_extended
        self._sha256 = hashlib.sha256(val)
        self._sha1 = hashlib.sha1(val)
        self._md5 = hashlib.md5(val)

        self._sha512 = 'NOT_CALCULATED'
        if self._process_extended:
            self._sha512 = hashlib.sha512(val)

    def update_from_string(self, string: str) -> None:
        self.update_from_bytes(string.encode(encoding='utf-8'))

    def update_from_bytes(self, data: bytes) -> None:
        self._sha256.update(data)
        self._sha1.update(data)
        self._md5.update(data)
        if self._process_extended:
            self._sha512.update(data)

    def sha256(self) -> str:
        return self._sha256.hexdigest()

    def sha1(self) -> str:
        return self._sha1.hexdigest()

    def md5(self) -> str:
        return self._md5.hexdigest()

    def sha512(self) -> str:
        return self._sha512.hexdigest()

    def as_dict(self) -> dict:
        json = {'md5': self.md5(), 'sha1': self.sha1(), 'sha256': self.sha256()}
        if self._process_extended:
            json['sha512'] = self.sha512()

        return json


def calc_bytes_digests(data: bytes, process_extended: bool = False) -> Digest:
    return Digest(data, process_extended=process_extended)


def calc_string_digests(string: str, process_extended: bool = False) -> Digest:
    return calc_bytes_digests(string.encode(encoding='utf-8'), process_extended=process_extended)
