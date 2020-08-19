from setuptools import setup, find_packages

with open("README.rst") as fh:
    long_description = fh.read()

setup(
    name='cmdchess',
    version='0.1.2',
    description='A Windows command line application to play chess (specifically) using the command prompt.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='leonarduschen',
    author_email='leonardus.chen@gmail.com',
    url='https://github.com/leonarduschen/cmdchess',
    license='MIT',
    install_requires=['colorama>=0.4.3'],
    tests_require=['pytest'],
    packages=find_packages(
        exclude=(
            'tests',
            'docs')),
    entry_points={
        'console_scripts': [
            'cmdchess=cmdchess:playchess',
        ],
    },
)
