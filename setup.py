from setuptools import setup

install_requires = [
    'scikit-image',
]

setup( install_requires=install_requires, use_scm_version = lambda: {"local_scheme":lambda version: ""},)
