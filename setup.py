from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='cmdchess',
    version='0.1.0',
    description='Command-line Application Chess',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='simple-spherical-cow',
    email = 'leonardus.chen@gmail.com',
    url='https://github.com/simple-spherical-cow/cmdchess',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)