from setuptools import setup

install_requires = []

with open('requirements.txt', 'r') as requirements_file:
    for line in requirements_file:
        package_name = line.strip()
        install_requires.append(package_name)
        
setup(
    name='autocore',
    version='1.0.0',
    author='Agent 1997',
    packages=['web'],
    install_requires=install_requires
)