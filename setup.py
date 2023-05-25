from setuptools import find_packages, setup

setup(
    name='hello_loopring',
    version='',
    description='Loopring V3 api sample with sdk',
    author='Loopring',
    python_requires='>=3.7',
    install_requires=[
        'bitstring',
        'pyblake2',
        'eip712-structs',
        'web3',
        'ujson',
    ],
    packages=find_packages(),
)
