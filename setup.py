from setuptools import find_packages, setup

setup(
    name='hello_loopring',
    version='',
    description='Loopring V3 api sample with sdk',
    author='Loopring',
    python_requires='>=3.7',
    install_requires=[
        'bitstring',
        'eip712-structs @ git+https://github.com/konichuvak/py-eip712-structs.git@packaging',
        'web3',
        'ujson',
    ],
    packages=find_packages(),
)
