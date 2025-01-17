#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = ["numpy", "shapely", "pandas","geopandas","rasterio","fiona","rtree","matplotlib","descartes"]

setup_requirements = ['pytest-runner', 'bump2version' ]

test_requirements = ['pytest>=3', ]

setup(
    author="Ben Weinstein",
    author_email='ben.weinstein@weecology.org',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Benchmark for individual tree crown detection",
    entry_points={
        'console_scripts': [
            'neontreeevaluation_python=neontreeevaluation_python.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description="Python package for individual tree crown detection evaluation",
    include_package_data=True,
    keywords='neontreeevaluation_python',
    name='neontreeevaluation_python',
    packages=find_packages(include=['neontreeevaluation_python', 'neontreeevaluation_python.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/bw4sz/neontreeevaluation_python',
    version='0.1.0',
    zip_safe=False,
)
