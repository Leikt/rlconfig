import unittest

from rlconfig import FernetWrapper, Config


class TestConfig(unittest.TestCase):
    def setUp(self) -> None:
        Config.__clear__()

    def test_load(self):
        config_file_yaml = 'data/config/config001.yml'
        config_file = config_file_yaml + '.fer'
        keyfile = 'data/config/key001.key'
        FernetWrapper('test', keyfile, True).encrypt_file(config_file_yaml, config_file)

        Config('test', config_file, fernet_wrapper='test')
        self.assertEqual(Config('test').var1, 'VARIABLE_1')
        self.assertEqual(Config('test').cat1.var2, 'VARIABLE_2')
        self.assertEqual(Config('test').report.formats[0].align, 'center')

    def test_multiple(self):
        config_file_yaml = 'data/config/config001.yml'
        config_file_yaml_2 = 'data/config/config002.yml'
        config_file = config_file_yaml + '.fer'
        config_file_2 = config_file_yaml_2 + '.fer'
        keyfile = 'data/config/key002.key'
        FernetWrapper('test', keyfile, True).encrypt_file(config_file_yaml, config_file)
        FernetWrapper('test').encrypt_file(config_file_yaml_2, config_file_2)

        Config('test1', config_file, fernet_wrapper='test')
        Config('test2', config_file_2, fernet_wrapper='test')
        self.assertEqual(Config('test1').var1, 'VARIABLE_1')
        self.assertEqual(Config('test2').var1, 'VARIABLE_1_CONFIG_2')

    def test_nesting(self):
        config_file_yaml = 'data/config/config003.yml'
        config_file = config_file_yaml + '.fer'
        keyfile = 'data/config/key003.key'
        FernetWrapper('test', keyfile, True).encrypt_file(config_file_yaml, config_file)

        Config('global', config_file, fernet_wrapper='test')
        Config('cat1', Config('global').cat1, fernet_wrapper='test')

        self.assertEqual(Config('global').cat1.var2, Config('cat1').var2)

    def test_not_encrypted(self):
        config_file = 'data/config/config004.yml'

        Config('test', config_file)
        self.assertEqual(Config('test').var1, 'VARIABLE_1_CONFIG_4')
