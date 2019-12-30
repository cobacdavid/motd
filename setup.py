from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='motd',
    version='0.1.3',
    description='Mathematicians Of The Day http://mathshistory.st-andrews.ac.uk/Day_files/Year.html Not an official package',
    long_description_content_type='text/markdown',
    long_description=long_description,
    url='https://twitter.com/david_cobac',
    author='David COBAC',
    author_email='david.cobac@gmail.com',
    keywords=['motd',
              'date',
              'math',
              'hitory'],
    license='CC-BY-NC-SA',
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages()
)
