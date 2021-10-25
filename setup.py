from setuptools import find_packages, setup

setup(
    name='hello_loopring',
    version='',
    description='Loopring V3 api sample with sdk',
    author='Loopring',
    python_requires='>=3.6.1',
    install_requires=[
        'bitstring',
        'pysha3',
        'pyblake2',
        'eip712-structs',
        'py_eth_sig_utils',
        'web3',
        'ujson',
    ],
    packages=find_packages(),
)
