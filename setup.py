from setuptools import setup

setup(
    name='DnDSearch',
    version='1.0.0',
    py_modules=['dndsear'],
    install_requires=[
        'click',
        'requests',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'dndsear = dndsear:cli',
        ],
    },
)