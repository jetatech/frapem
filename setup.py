from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in meeting/__init__.py
from meeting import __version__ as version

setup(
	name="meeting",
	version=version,
	description="meeting app",
	author="jetatech",
	author_email="meeting@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
