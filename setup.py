from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='cmdchess',
    version='0.1.0',
    description='Command-line Application Chess',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='simple-spherical-cow',
    author_email = 'leonardus.chen@gmail.com',
    url='https://github.com/simple-spherical-cow/cmdchess',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={  # Optional
        'console_scripts': [
            'cmdchess=cmdchess:cmdchess',
        ],
    },
)