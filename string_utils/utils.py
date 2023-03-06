import hashlib

class StringTouls(object):
    def concat(self, a, b):
        full = ''.join([a, b])
        return full

    def __writeLn(self, a):
        print(a, "\n")

    def UpperCase(self, string):
        upper = string.upper()
        return string.upper()

    def to_lower_case(self, string):
        return string.lower()

    def hash(self, input):
        md5 = hashlib.new('md5')
        return md5

    def md5(self, input):
        return hashlib.md5(str(input).encode("UTF-8")).hexdigest()

    def sha512(self, input):
        """
        Calc sha256 hash
        :param input: string
        :return: string
        """
        sha = hashlib.new("sha1", str(input).encode("utf-8")).hexdigest()
        return sha

    def concatenate(self, a, b, c):
        new = str(a) + str(b)
        return new

    def replce(self, string: str, new, old):
        return string.replace(new, old, 1)

    def trim(self, a):
        """
        Removes whitespace
        :param a: string
        :return: string
        """
        trimmed = a.strip()
