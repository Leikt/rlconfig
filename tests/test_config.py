import unittest

from lsconfig import *
from lsconfig.config_item import ConfigItem


class TestConfig(unittest.TestCase):
    def setUp(self) -> None:
        Config.clear()

    def test_001_simple(self):
        self.assertFalse(Config.is_loaded('test_001'))
        Config.load('test_001', 'config/test_001.yml')
        self.assertTrue(Config.is_loaded('test_001'))
        self.assertEqual('data/test_001.yml', Config('test_001').directory)
        self.assertEqual('George POMPIDOU', Config('test_001').author.full_name)

    def test_002_clear(self):
        self.assertFalse(Config.is_loaded('test_002a'))
        self.assertFalse(Config.is_loaded('test_002b'))
        Config.load('test_002a', 'config/test_dummy.yml')
        Config.load('test_002b', 'config/test_dummy.yml')
        self.assertTrue(Config.is_loaded('test_002a'))
        self.assertTrue(Config.is_loaded('test_002b'))
        Config.clear()
        self.assertFalse(Config.is_loaded('test_002a'))
        self.assertFalse(Config.is_loaded('test_002b'))

    def test_003_composition(self):
        Config.load('test_003', 'config/test_003.yml')
        self.assertEqual('A Book Title', Config('test_003').title)
        self.assertIsInstance(Config('test_003').author, ConfigItem)

    def test_004_unload(self):
        Config.load('test_004', 'config/test_dummy.yml')
        self.assertTrue(Config.is_loaded('test_004'))
        Config.release('test_004')
        self.assertFalse(Config.is_loaded('test_004'))

    def test_E001_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            Config.load('test_E001', 'config/test_file_not_found.yml')

    def test_E002_config_not_loaded(self):
        with self.assertRaises(ConfigurationNotLoadedError):
            _ = Config('not_loaded').value
