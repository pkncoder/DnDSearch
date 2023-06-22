from setuptools import setup

setup(
    name='DnDSearch',
    version='0.1.0',
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