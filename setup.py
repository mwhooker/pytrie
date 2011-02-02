import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

version = '0.1'

tests_require = ['nose']

setup(
    name="pytrie",
    version=version,
    description='trie structure',
    long_description=""" """,
    license='Public Domain',
    author='Matthew Hooker',
    author_email='mwhooker@gmail.com',
    url='',
    packages=find_packages(exclude=['ez_setup', 'test', 'test.*']),
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=tests_require,
)
