from setuptools import setup, find_packages

package_name = 'svo'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'setuptools',
        'nltk',
    ],
    author='Andreas Klintberg',
    maintainer='Andreas Klintberg',
    description='NLTK SVO',
    license='Apache License, Version 2.0',
    test_suite='pytest'
)
