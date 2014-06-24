#!/usr/bin/env python
import sys

from setuptools import setup, find_packages

requires = ['botocore>=0.51.0,<0.52.0',
            'cement>=2.2.2']


setup_options = dict(
    name='nicksEB',
    version='0.1.1',
    description='Command Line Interface for AWS EB.',
    long_description=open('README.txt').read(),
    author='Nick Humrich',
    author_email='humrichn@amazon.com',
    url='eb.example.com',
    scripts=['bin/eb'],
    packages=find_packages('.', exclude=['tests*']),
    package_dir={'eb': 'eb'},
    package_data={'eb': ['data/*.json', 'examples/*/*.rst',
                             'examples/*/*/*.rst']},
    install_requires=requires,
    license="Apache License 2.0",
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ),
    )

if 'py2exe' in sys.argv:
    # This will actually give us a py2exe command.
    import py2exe
    # And we have some py2exe specific options.
    setup_options['options'] = {
        'py2exe': {
            'optimize': 0,
            'skip_archive': True,
            'packages': ['docutils', 'urllib', 'httplib', 'HTMLParser',
                         'eb', 'ConfigParser', 'xml.etree'],
            }
    }
    setup_options['console'] = ['bin/eb']


setup(**setup_options)