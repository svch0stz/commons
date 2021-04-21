import hashlib


class Digest:

    def __init__(self, val: bytes = None, process_extended: bool = False, values_only=False) -> None:
        self.values_only = values_only

        if not values_only:
            self._process_extended = process_extended
            self._sha256 = hashlib.sha256()
            self._sha1 = hashlib.sha1()
            self._md5 = hashlib.md5()
            self._sha512 = hashlib.sha512()

            if val:
                self.update_from_bytes(data=val)
        else:
            self._process_extended = False
            self._sha256_str: str = str()
            self._sha1_str: str = str()
            self._md5_str: str = str()
            self._sha512_str: str = str()

    def update_from_string(self, string: str) -> None:
        self.update_from_bytes(string.encode(encoding='utf-8'))

    def update_from_bytes(self, data: bytes) -> None:
        if not self.values_only:
            if self.values_only:
                self._sha256.update(data)
                self._sha1.update(data)
                self._md5.update(data)
                if self._process_extended:
                    self._sha512.update(data)
        else:
            raise AttributeError()

    def sha256(self) -> str:
        if not self.values_only:
            return self._sha256.hexdigest()
        else:
            return self._sha256_str

    def sha1(self) -> str:
        if not self.values_only:
            return self._sha1.hexdigest()
        else:
            return self._sha1_str

    def md5(self) -> str:
        if not self.values_only:
            return self._md5.hexdigest()
        else:
            return self._md5_str

    def sha512(self) -> str:
        if not self.values_only:
            return self._sha512.hexdigest()
        else:
            return self._sha512_str

    def as_dict(self) -> dict:
        json = {'md5': self.md5(), 'sha1': self.sha1(), 'sha256': self.sha256()}
        if self._process_extended:
            json['sha512'] = self.sha512()

        return json

    @classmethod
    def from_dict(cls, doc: dict):
        obj = cls(values_only=True)
        if 'md5' in doc:
            obj._md5_str = doc['md5']
        if 'sha1' in doc:
            obj._sha1_str = doc['sha1']
        if 'sha256' in doc:
            obj._sha256_str = doc['sha256']
        if 'sha512' in doc:
            obj._sha512_str = doc['sha512']
        return obj


def calc_bytes_digests(data: bytes, process_extended: bool = False) -> Digest:
    return Digest(data, process_extended=process_extended)


def calc_string_digests(string: str, process_extended: bool = False) -> Digest:
    return calc_bytes_digests(string.encode(encoding='utf-8'), process_extended=process_extended)


def calc_file_digests(filename: str, process_extended: bool = False) -> Digest:
    digest = Digest(process_extended=process_extended)
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            digest.update_from_bytes(byte_block)
    return digest
