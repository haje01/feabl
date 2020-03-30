import os
from setuptools import setup, find_packages

with open(os.path.join('featr', 'version.py'), 'rt') as f:
    version = f.read().strip()
    version = version.split('=')[1].strip("'")

setup(
    name='featr',
    version=version,
    author='haje01',
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'featr = featr.cli:main'
        ]
    },
    install_requires=[
        'click',
        'jsonschema==3.2.0',
    ]
)
