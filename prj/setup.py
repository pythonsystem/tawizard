from setuptools import setup, find_packages

setup(
  name = 'tawizard',
  version = '1.0.5',
  description = 'tawizard',
  url = 'https://github.com/pythonsystem/tawizard',
  author = 'Kevin Johnson',
  license = 'MIT',
  long_description = open('README.txt', 'r').read(),
  long_description_content_type = 'text/plain',
  packages = find_packages(include = ['tawizard*']),
  install_requires = open('requirements.txt', 'r').read().split('\n'),
  setup_requires = [],
  tests_require = [],
)
