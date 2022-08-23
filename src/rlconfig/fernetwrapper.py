import os

from cryptography.fernet import Fernet

from .helpers import GloballyAccessible


class FernetWrapper(metaclass=GloballyAccessible):
    def __init__(self, keyfile: str, auto_generate: bool = False):
        self._load_key(keyfile, auto_generate)

    def _load_key(self, filename: str, auto_generate: bool):
        if not os.path.exists(filename):
            if not auto_generate:
                raise FileNotFoundError('Cannot find the key in "{}". Use the auto_generate parameter if you want \
the key to be automatically created')
            self.create_key(filename)

        with open(filename, 'rb') as file:
            key = file.read()
        self._fernet = Fernet(key)

    def load_file(self, filename: str) -> bytes:
        with open(filename, 'rb') as file:
            content = file.read()
        return self._fernet.decrypt(content)

    def save_file(self, filename: str, content: bytes):
        content = self._fernet.encrypt(content)
        with open(filename, 'wb') as file:
            file.write(content)

    def decrypt_file(self, source: str, destination: str):
        with open(source, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = self._fernet.decrypt(encrypted_data)
        with open(destination, 'w') as file:
            file.write(decrypted_data.decode())

    def encrypt_file(self, source: str, destination: str):
        with open(source, 'r') as file:
            source = file.read()
        encrypted = self._fernet.encrypt(source.encode())
        with open(destination, 'wb') as file:
            file.write(encrypted)

    def decrypt_string(self, message: bytes) -> str:
        return self._fernet.decrypt(message).decode()

    def encrypt_string(self, message: str) -> bytes:
        return self._fernet.encrypt(message.encode())

    @staticmethod
    def create_key(filename: str):
        if not os.path.isdir(os.path.dirname(filename)):
            os.mkdir(os.path.dirname(filename))
        key = Fernet.generate_key()
        with open(filename, 'wb') as file:
            file.write(key)
