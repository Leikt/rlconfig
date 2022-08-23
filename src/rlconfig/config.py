import yaml

from .fernetwrapper import FernetWrapper
from .helpers import GloballyAccessible


class _ConfigItem:
    def __init__(self, obj: object):
        self._list = None

        if isinstance(obj, dict):
            self._dict = obj
            for key, value in obj.items():
                self.__setattr__(key, _ConfigItem.create(value))
        elif isinstance(obj, list):
            self._list = []
            for value in obj:
                self._list.append(_ConfigItem.create(value))
        elif isinstance(obj, object):
            self.__dict__.update(obj.__dict__)

    @staticmethod
    def create(obj: object):
        if isinstance(obj, dict):
            return _ConfigItem(obj)
        if isinstance(obj, list):
            result = []
            for item in obj:
                result.append(_ConfigItem.create(item))
            return result
        return obj

    def as_dict(self) -> dict:
        return self._dict.copy()

    def __iter__(self):
        for elt in self._list:
            yield elt


class Config(_ConfigItem, metaclass=GloballyAccessible):
    def __init__(self, filename: str, fernet_wrapper: str = None):
        if not isinstance(filename, str):
            data = filename
        elif fernet_wrapper is not None:
            data = FernetWrapper(fernet_wrapper).load_file(filename)
            data = yaml.safe_load(data)
        else:
            with open(filename, 'r') as file:
                data = file.read()
                data = yaml.safe_load(data)
        super().__init__(data)
