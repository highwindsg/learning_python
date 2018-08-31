try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Lexicon Tests',
    'author': 'Caven Yip',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'email@email.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['lexicon'],
    'scripts': [],
    'name': 'lexicon_tests'
}

setup(**config)
