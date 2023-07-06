from setuptools import setup

install_requires = []

with open('requirements.txt', 'r', encoding='utf-16') as requirements_file:   
    install_requires = requirements_file.readlines()
      
setup(
    name='autocore',
    version='1.0.0',
    author='Agent 1997',
    packages=['','web'],
    install_requires=install_requires
)

