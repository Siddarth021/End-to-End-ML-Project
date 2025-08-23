'''

The setup script is the centre of all activity in building, distributing, and installing modules using the Distutils.
The main purpose of the setup script is to describe your module distribution to the Distutils, so that the various commands
that operate on your modules do the right thing. As we saw in section A Simple Example above, the setup script consists mainly
of a call to setup(), and most information supplied to the Distutils by the module developer is supplied as keyword arguments to setup()

'''
# It will be responsible for creating my machine learning application as a package

from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path):
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            req = line.strip()
            if req and not req.startswith('-e'):
                requirements.append(req)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Siddarth',
    author_email='gundetisiddarth@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)