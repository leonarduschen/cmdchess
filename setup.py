"""Setup

"""

from setuptools import setup, find_packages

with open("README.rst") as fh:
    long_description = f.read()

with open('LICENSE') as f:
    licensefile = f.read()

setup(
    name='cmdchess',
    version='0.1.1',
    description='Command-line Application Chess',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='leonarduschen',
    author_email='leonardus.chen@gmail.com',
    url='https://github.com/leonarduschen/cmdchess',
    license=licensefile,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': [
            'cmdchess=cmdchess:playchess',
        ],
    },
)
