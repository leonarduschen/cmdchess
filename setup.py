"""Setup"""

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('LICENSE') as f:
    licensefile = f.read()

setup(
    name='cmdchess',
    version='0.1.1',
    description='Command-line Application Chess',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='simple-spherical-cow',
    author_email='leonardus.chen@gmail.com',
    url='https://github.com/simple-spherical-cow/cmdchess',
    license=licensefile,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': [
            'cmdchess=cmdchess:playchess',
        ],
    },
)
