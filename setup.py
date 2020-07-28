from setuptools import setup, find_packages

setup(
    name='cmdchess',
    version='0.1.0',
    description='Command-line Chess - Play Chess on Command Line',
    author='simple-spherical-cow',
    email = 'leonardus.chen@gmail.com',
    url='https://github.com/simple-spherical-cow/cmdchess',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)