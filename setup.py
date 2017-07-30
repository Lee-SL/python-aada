#!/usr/bin/env python
from setuptools import find_packages, setup

dependencies = ['awscli', 'botocore', 'boto3', 'requests', 'selenium']

setup(
    name='aada',
    version='0.1.0',
    url='https://github.com/piontas/python-aada',
    license='MIT',
    author='Marek Piatek',
    author_email='piatek.marek@gmail.com',
    description='Generates STS Tokens based on SAML Assertion from Azure AD',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'aada = aada.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)