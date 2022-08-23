from distutils.core import setup

from increase_version import load_version_string

NAME = 'rlconfig'
VERSION = load_version_string()
DESCRIPTION = ''
LONG_DESCRIPTION_FILE = 'README.md'
AUTHOR = 'Robin LIORET'
AUTHOR_EMAIL = 'robin.lioret@epro.com'
URL = 'link'
PACKAGES = ['your_package']
PACKAGE_DIR = {'your_package': 'src/your_package'}
PACKAGE_DATA = {'your_package': ['data/*']}
DATA_FILES = []

with open(LONG_DESCRIPTION_FILE, 'r') as file:
    long_description = file.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=PACKAGES,
    package_dir=PACKAGE_DIR,
    package_data=PACKAGE_DATA,
    data_files=DATA_FILES,
    long_description=long_description
)
