from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in registration_system/__init__.py
from registration_system import __version__ as version

setup(
	name='registration_system',
	version=version,
	description='user registration',
	author='Monika',
	author_email='monika.p@indictrans.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
