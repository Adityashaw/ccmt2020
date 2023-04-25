"""
basic setup script
"""

from setuptools import setup

setup(
        name='ccmt2020',
        packages=['ccmt2020'],
        include_package_data=True,
        install_requires=[
            'Flask',
            'libsass',
            'requests'
        ],
)
