import hashlib
from functools import partial


class StringTools:

    HASH_FUNCS = ['md5', 'sha256', 'sha512', 'sha1']

    @staticmethod
    def concat(*args) -> str:
        """Concatenate arguments."""

        args_to_str = map(str, args)
        return ''.join(args_to_str)

    @staticmethod
    def print_ln(data: str) -> None:
        """Print value with additional new line."""

        print(f"{data}\n")

    @staticmethod
    def to_upper_case(data: str) -> str:
        """Convert string to upper case."""

        return data.upper()

    @staticmethod
    def to_lower_case(data: str) -> str:
        """Convert string to lower case."""

        return data.lower()

    @staticmethod
    def hash(hash_func_name: str, data: str) -> str:
        """Calculate hash.

        NOTE: Named constructor functions are faster than using new(hash_func_name)
        """

        return hashlib.new(
            hash_func_name,
            data.encode("UTF-8"),
        ).hexdigest()

    @staticmethod
    def _prepare_hash_func(constructor_name: str, data: str) -> str:
        hash_func = getattr(hashlib, constructor_name)
        return hash_func(
            data.encode("utf-8"),
        ).hexdigest()

    def __getattr__(self, name):
        if hasattr(hashlib, name):
            if name in self.HASH_FUNCS:
                return partial(
                    self._prepare_hash_func, name,
                )
            else:
                raise AttributeError(
                    f"{self.__class__.__name__} object has no attribute {name}. "
                    f"If you try to use hash func of hashlib then please add it to HASH_FUNCS",
                )
        raise AttributeError(
            f"{self.__class__.__name__} object has no attribute {name}.",
        )

    @staticmethod
    def replace(data: str, old: str, new: str, count: int = -1):
        """Replace old value with new."""

        return data.replace(old, new, count)

    @staticmethod
    def remove_whitespace(data: str) -> str:
        """Removes whitespace."""

        return data.replace(' ', '')


def main():
    tool = StringTools()
    result = tool.md5("eee")
    print(result)


if __name__ == '__main__':
    main()

