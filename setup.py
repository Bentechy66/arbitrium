from setuptools import setup
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'arbitrium',
  packages = ['arbitrium'],
  version = '1.1.3',
  license='MIT',
  description = 'Arbitrium - The Easy Menu System For Python',
  long_description = long_description,
  long_description_content_type='text/markdown',
  author = 'Ben Griffiths',
  author_email = 'sendbenspam@yahoo.co.uk',
  url = 'https://github.com/bentechy66/arbitrium',
  download_url = 'https://github.com/bentechy66/arbitrium/archive/v_01.tar.gz',
  keywords = ['MENU', 'EASY', 'BEGGINNER-FRIENDLY'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
