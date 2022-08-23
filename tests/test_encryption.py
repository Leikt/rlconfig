import os
import unittest

from rlconfig import FernetWrapper


class TestEncryption(unittest.TestCase):
    def setUp(self) -> None:
        FernetWrapper.__clear__()

    def test_generate_key(self):
        keyfile = 'data/encryption/key001.key'
        if os.path.exists(keyfile):
            os.remove(keyfile)

        FernetWrapper.create_key(keyfile)
        self.assertTrue(os.path.exists(keyfile))

    def test_load_key_auto_generation_success(self):
        keyfile = 'data/encryption/key002.key'

        FernetWrapper('test', keyfile, auto_generate=True)
        self.assertTrue(os.path.exists(keyfile))

    def test_load_key_auto_generation_failure(self):
        keyfile = 'data/encryption/key003.key'

        with self.assertRaises(FileNotFoundError):
            FernetWrapper('test', keyfile, auto_generate=False)
        self.assertFalse(os.path.exists(keyfile))

    def test_load_key_success(self):
        keyfile = 'data/encryption/key004.key'

        FernetWrapper.create_key(keyfile)
        self.assertTrue(os.path.exists(keyfile))
        FernetWrapper('test', keyfile, auto_generate=False)

    def test_encrypt_message(self):
        keyfile = 'data/encryption/key005.key'
        encryption = FernetWrapper('test', keyfile, True)
        message = 'Hello World!'

        encrypted_msg = encryption.encrypt_string(message)
        self.assertTrue(isinstance(encrypted_msg, bytes))
        decrypted_msg = encryption.decrypt_string(encrypted_msg)
        self.assertTrue(isinstance(decrypted_msg, str))
        self.assertEqual(decrypted_msg, message)

    def test_save_file(self):
        keyfile = 'data/encryption/key006.key'
        encryption = FernetWrapper('test', keyfile, True)
        content = 'Content\nIs\nOverrated'
        filename = 'data/encryption/test_save_file.fer'

        encryption.save_file(filename, content.encode())
        self.assertTrue(os.path.exists(filename))
        decrypted_content = encryption.load_file(filename).decode()
        self.assertTrue(isinstance(decrypted_content, str))
        self.assertEqual(decrypted_content, content)

    def test_encrypt_file(self):
        keyfile = 'data/encryption/key006.key'
        encryption = FernetWrapper('test', keyfile, True)
        content = 'Content\nIs\nOverrated'
        content_filename = 'data/encryption/test_encrypt_file.txt'
        encrypted_filename = 'data/encryption/test_encrypt_file.fer'
        decrypted_filename = 'data/encryption/test_encrypt_file.fer.txt'
        with open(content_filename, 'w') as file:
            file.write(content)

        encryption.encrypt_file(content_filename, encrypted_filename)
        self.assertTrue(os.path.exists(encrypted_filename))
        encryption.decrypt_file(encrypted_filename, decrypted_filename)
        self.assertTrue(os.path.exists(decrypted_filename))
        with open(decrypted_filename, 'r') as file:
            decrypted_content = file.read()
        self.assertTrue(isinstance(decrypted_content, str))
        self.assertEqual(decrypted_content, content)

    def test_singleton(self):
        keyfile = 'data/encryption/key007.key'
        message = 'Hello World!'

        FernetWrapper('test', keyfile, True)
        self.assertTrue(os.path.exists(keyfile))
        encrypted_message = FernetWrapper('test').encrypt_string(message)
        decrypted_message = FernetWrapper('test').decrypt_string(encrypted_message)
        self.assertEqual(decrypted_message, message)

    def test_multiple_keys(self):
        keyfile_1 = 'data/encryption/key008a.key'
        keyfile_2 = 'data/encryption/key008b.key'
        message = 'Hello World!'

        FernetWrapper('a', keyfile_1, True)
        FernetWrapper('b', keyfile_2, True)
        self.assertEqual(FernetWrapper('a'), FernetWrapper('a'))
        self.assertNotEqual(FernetWrapper('a'), FernetWrapper('b'))
        self.assertNotEqual(FernetWrapper('a').encrypt_string(message), FernetWrapper('b').encrypt_string(message))


if __name__ == '__main__':
    unittest.main()
