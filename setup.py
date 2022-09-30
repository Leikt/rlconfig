from distutils.core import setup

with open('C:\\Users\\rlioret\\IdeaProjects\\Tools\\config\\version', 'r') as file:
    VERSION=file.read()

NAME = 'lsconfig'
DESCRIPTION = ''
LONG_DESCRIPTION_FILE = 'README.md'
AUTHOR = 'Leikt SOLREIHIN'
AUTHOR_EMAIL = 'leikt.solreihin@epro.com'
URL = 'https://github.com/Leikt/lsconfig'
PACKAGES = ['rlconfig']
PACKAGE_DIR = {'lsconfig': 'src/lsconfig'}
PACKAGE_DATA = {}
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
