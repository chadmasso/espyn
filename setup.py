from distutils.core import setup
setup(
    name = 'espyn',
    packages = ['espyn'],
    version = '0.0.2',
    description = 'ESPN Python API',
    author='Chad Masso',
    author_email='chad.m.masso@gmail.com',
    maintainer='Chad Masso',
    maintainer_email='chad.m.masso@gmail.com',
    install_requires=['requests==0.10.8']
)